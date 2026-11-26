#!/usr/bin/env python3
"""
Build semantic peer groups from company description cache.

Pipeline:
  1. Load combined_description from .company_cache/*.json
  2. TF-IDF vectorize (bigrams, 5000 features)
  3. Cosine similarity matrix
     >= 0.35 → confirmed peers
     0.10-0.35 → borderline → sentence-transformers re-check (all-MiniLM-L6-v2)
     < 0.10  → not peers
  4. DBSCAN clustering on similarity graph
  5. Auto-label groups; apply manual overrides from peer_group_overrides.json
  6. Write peer_groups.json

Usage:
    python tools/peer_group_builder.py
    python tools/peer_group_builder.py --min-desc-len 30   # lower bar for short descriptions
"""

import argparse
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import DBSCAN

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_DIR))
CACHE_DIR = REPO_DIR / ".company_cache"
TOOLS_DIR = Path(__file__).parent
OVERRIDES_FILE = TOOLS_DIR / "peer_group_overrides.json"
OUT_FILE = REPO_DIR / "peer_groups.json"

# Thresholds
TFIDF_HIGH = 0.35  # confirmed peer
TFIDF_LOW = 0.10  # below this = not peers (skip embedding check)
EMBED_THRESH = 0.70  # sentence-transformer similarity to confirm borderline pair
DBSCAN_EPS = 0.60  # connectivity threshold for DBSCAN
DBSCAN_MINPTS = 2  # min members to form a cluster (singletons allowed)
MIN_DESC_LEN = 40  # skip stocks with very short descriptions


# ── Text loading ───────────────────────────────────────────────────────────────


def load_cache() -> dict[str, dict]:
    """Return {symbol: cache_entry} for all cached stocks."""
    entries = {}
    for p in CACHE_DIR.glob("*.json"):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            sym = data.get("symbol", p.stem)
            entries[sym] = data
        except Exception:
            pass
    return entries


def clean_text(text: str) -> str:
    text = re.sub(r"\[\d+\]", " ", text)  # strip citation markers [1]
    text = re.sub(r"Read More.*$", " ", text)  # strip trailing "Read More" links
    text = re.sub(r"[^\w\s]", " ", text)  # strip punctuation
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


# ── TF-IDF ────────────────────────────────────────────────────────────────────


def build_tfidf(symbols: list[str], descriptions: list[str]):
    min_df = 2 if len(descriptions) >= 10 else 1
    vec = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=5000,
        sublinear_tf=True,
        stop_words="english",
        min_df=min_df,
    )
    matrix = vec.fit_transform(descriptions)
    return vec, matrix


# ── Sentence-transformer embedding ────────────────────────────────────────────

_embed_model = None


def _get_embed_model():
    global _embed_model
    if _embed_model is None:
        try:
            from sentence_transformers import SentenceTransformer

            print("  Loading sentence-transformers model (all-MiniLM-L6-v2)...")
            _embed_model = SentenceTransformer("all-MiniLM-L6-v2")
            print("  Model loaded.")
        except ImportError:
            print(
                "  WARNING: sentence-transformers not installed. Borderline pairs will use TF-IDF mid-threshold (0.225)."
            )
            _embed_model = None
    return _embed_model


def embed_similarity(texts_a: list[str], texts_b: list[str]) -> list[float]:
    """Batch compute cosine similarity for paired (a, b) texts via sentence-transformers."""
    model = _get_embed_model()
    if model is None:
        return [0.5] * len(texts_a)  # neutral fallback: let TFIDF midpoint decide

    all_texts = list(dict.fromkeys(texts_a + texts_b))
    embeddings = model.encode(all_texts, show_progress_bar=False, batch_size=64)
    by_text = dict(zip(all_texts, embeddings))

    sims = []
    for ta, tb in zip(texts_a, texts_b):
        a, b = by_text[ta], by_text[tb]
        norm = np.linalg.norm(a) * np.linalg.norm(b)
        sims.append(float(np.dot(a, b) / norm) if norm > 0 else 0.0)
    return sims


# ── Peer graph construction ────────────────────────────────────────────────────


def build_peer_graph(
    symbols: list[str],
    descriptions: list[str],
    tfidf_matrix,
) -> np.ndarray:
    """
    Return a binary adjacency matrix (n x n).
    Entry [i,j] = 1 if i and j are peers.
    """
    n = len(symbols)
    sim = cosine_similarity(tfidf_matrix).astype(np.float32)
    adj = np.zeros((n, n), dtype=np.float32)

    # Collect borderline pairs for batch embedding
    borderline_i, borderline_j = [], []
    for i in range(n):
        for j in range(i + 1, n):
            s = sim[i, j]
            if s >= TFIDF_HIGH:
                adj[i, j] = adj[j, i] = 1.0
            elif s >= TFIDF_LOW:
                borderline_i.append(i)
                borderline_j.append(j)

    if borderline_i:
        print(
            f"  Checking {len(borderline_i)} borderline pairs via sentence-transformers..."
        )
        texts_a = [descriptions[i] for i in borderline_i]
        texts_b = [descriptions[j] for j in borderline_j]
        emb_sims = embed_similarity(texts_a, texts_b)
        for i, j, es in zip(borderline_i, borderline_j, emb_sims):
            if es >= EMBED_THRESH:
                adj[i, j] = adj[j, i] = 1.0

    # Add self-loops so DBSCAN sees each node
    np.fill_diagonal(adj, 1.0)
    return adj


# ── DBSCAN clustering ─────────────────────────────────────────────────────────


def cluster(adj: np.ndarray) -> np.ndarray:
    """Convert adjacency to distance, run DBSCAN. Returns label array (-1 = noise/singleton)."""
    distance = 1.0 - adj
    np.clip(distance, 0, 1, out=distance)
    db = DBSCAN(eps=1.0 - DBSCAN_EPS, min_samples=DBSCAN_MINPTS, metric="precomputed")
    labels = db.fit_predict(distance)
    return labels


# ── Auto-labeling ──────────────────────────────────────────────────────────────

_STOP = {
    "and",
    "the",
    "of",
    "in",
    "to",
    "is",
    "are",
    "a",
    "an",
    "for",
    "with",
    "its",
    "on",
    "at",
    "by",
    "from",
    "that",
    "which",
    "it",
    "or",
    "this",
    "their",
    "as",
    "has",
    "have",
    "been",
    "be",
    "through",
    "into",
    "company",
    "limited",
    "ltd",
    "india",
    "indian",
    "services",
    "products",
    "business",
    "operations",
    "segment",
    "sector",
    "market",
    "also",
    "including",
    "under",
    "through",
    "provides",
    "offering",
    "offers",
    "engaged",
    "engaged in",
    "incorporated",
    "registered",
}


def auto_label(descriptions: list[str], max_words: int = 4) -> str:
    bigrams: list[str] = []
    for desc in descriptions:
        words = [
            w
            for w in desc.lower().split()
            if w.isalpha() and w not in _STOP and len(w) > 3
        ]
        bigrams += [f"{words[i]} {words[i+1]}" for i in range(len(words) - 1)]
    if not bigrams:
        return "Misc"
    top = Counter(bigrams).most_common(1)[0][0]
    return top.title()


# ── Main ───────────────────────────────────────────────────────────────────────


def assemble_groups(symbols, descs, names, labels, overrides, previous):
    """Retain group identities by overlap and preserve explicit symbol overrides."""
    old = previous.get('groups', {})
    old_for_symbol = {s: gid for gid, g in old.items() for s in g['members']}
    clusters = {}
    for i, label in enumerate(labels):
        key = ('singleton', symbols[i]) if label == -1 else ('cluster', int(label))
        clusters.setdefault(key, []).append(i)
    used = set()
    reserved = set(old) | {v for k, v in overrides.items() if not k.startswith('_')}
    members = {}
    next_id = 0
    # Match larger overlaps first, independent of DBSCAN's arbitrary label numbers.
    ordered = sorted(clusters.items(), key=lambda item: -len(item[1]))
    for key, indices in ordered:
        candidates = Counter(old_for_symbol[symbols[i]] for i in indices if symbols[i] in old_for_symbol)
        candidates = {gid: n for gid, n in candidates.items()
                      if gid not in used and gid.startswith('singleton_') == (key[0] == 'singleton')}
        if candidates:
            gid = max(candidates, key=lambda gid: (candidates[gid], gid))
        else:
            prefix = 'singleton_' if key[0] == 'singleton' else 'group_'
            while f'{prefix}{next_id:04d}' in reserved or f'{prefix}{next_id:04d}' in used:
                next_id += 1
            gid = f'{prefix}{next_id:04d}'
            next_id += 1
        used.add(gid)
        for i in indices:
            assigned = overrides.get(symbols[i], gid)
            members.setdefault(assigned, []).append(i)
    groups, mapping = {}, {}
    for gid, indices in members.items():
        indices.sort()
        syms = [symbols[i] for i in indices]
        label = old.get(gid, {}).get('label') or (auto_label([descs[i] for i in indices]) if len(indices) > 1 else names[indices[0]])
        groups[gid] = {'label': label, 'members': syms, 'size': len(syms)}
        mapping.update({s: gid for s in syms})
    return groups, mapping


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-desc-len", type=int, default=MIN_DESC_LEN)
    parser.add_argument('--universe', type=Path, default=TOOLS_DIR / 'sector_rotation_universe.json')
    args = parser.parse_args(argv)

    from cluster_membership import load_universe, atomic_json
    universe = load_universe(args.universe)
    eligible = {s['symbol'] for s in universe['stocks']}

    print("Loading company descriptions from cache...")
    cache = load_cache()
    if not cache:
        print(
            f"ERROR: No cache files found in {CACHE_DIR}. Run tools/company_fetcher.py first."
        )
        return 1

    # Filter stocks with usable descriptions
    symbols, descs, names = [], [], []
    for sym, entry in sorted(cache.items()):
        if sym not in eligible:
            continue
        combined = entry.get("combined_description", "").strip()
        if len(combined) >= args.min_desc_len:
            symbols.append(sym)
            descs.append(clean_text(combined))
            names.append(entry.get("name", sym))

    print(
        f"  Loaded {len(symbols)} eligible stocks with descriptions (excluded {len(cache) - len(symbols)} cached entries)"
    )
    if len(symbols) < 2:
        print('ERROR: Fewer than two usable descriptions; previous groups preserved')
        return 1

    print("Building TF-IDF matrix...")
    vec, matrix = build_tfidf(symbols, descs)

    print("Building peer adjacency graph...")
    adj = build_peer_graph(symbols, descs, matrix)

    print("Running DBSCAN clustering...")
    labels = cluster(adj)

    unique_labels = sorted(set(labels))
    n_clusters = sum(1 for l in unique_labels if l >= 0)
    n_singletons = sum(1 for l in labels if l == -1)
    print(f"  Clusters: {n_clusters}  Singletons (noise): {n_singletons}")

    # Load manual overrides
    overrides: dict[str, str] = {}
    if OVERRIDES_FILE.exists():
        overrides = json.loads(OVERRIDES_FILE.read_text(encoding="utf-8"))
        overrides = {k: v for k, v in overrides.items() if not k.startswith('_')}
        print(f"  Loaded {len(overrides)} manual overrides")

    previous = json.loads(OUT_FILE.read_text(encoding='utf-8')) if OUT_FILE.exists() else {}
    overrides = {k: v for k, v in overrides.items() if not k.startswith('_')}
    groups, sym_to_group = assemble_groups(symbols, descs, names, labels, overrides, previous)

    output = {
        "version": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "n_stocks": len(symbols),
        "n_groups": len(groups),
        "n_singletons": sum(g['size'] == 1 for g in groups.values()),
        "groups": groups,
        "stock_to_group": sym_to_group,
    }

    atomic_json(OUT_FILE, output)
    print(f"Written: {OUT_FILE}  ({len(groups)} groups, {len(symbols)} stocks)")

    # Show largest groups as a sanity check
    sorted_groups = sorted(groups.items(), key=lambda x: x[1]["size"], reverse=True)
    print("\nTop 10 groups:")
    for gid, g in sorted_groups[:10]:
        print(f"  {gid} [{g['size']:3d}] {g['label']}: {', '.join(g['members'][:6])}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
