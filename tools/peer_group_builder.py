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

sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(__file__).parent.parent
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

    all_texts = texts_a + texts_b
    embeddings = model.encode(all_texts, show_progress_bar=False, batch_size=64)
    emb_a = embeddings[: len(texts_a)]
    emb_b = embeddings[len(texts_a) :]

    sims = []
    for a, b in zip(emb_a, emb_b):
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-desc-len", type=int, default=MIN_DESC_LEN)
    args = parser.parse_args()

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
        combined = entry.get("combined_description", "").strip()
        if len(combined) >= args.min_desc_len:
            symbols.append(sym)
            descs.append(clean_text(combined))
            names.append(entry.get("name", sym))

    print(
        f"  Loaded {len(symbols)} stocks with descriptions (skipped {len(cache) - len(symbols)} short/empty)"
    )

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
        print(f"  Loaded {len(overrides)} manual overrides")

    # Build group structures
    group_members: dict[str, list[int]] = {}
    sym_to_group: dict[str, str] = {}
    next_singleton = 0

    for idx, (sym, label) in enumerate(zip(symbols, labels)):
        if sym in overrides:
            gid = overrides[sym]
        elif label == -1:
            gid = f"singleton_{next_singleton:04d}"
            next_singleton += 1
        else:
            gid = f"group_{label:04d}"
        group_members.setdefault(gid, []).append(idx)
        sym_to_group[sym] = gid

    # Build group output
    groups = {}
    for gid, idxs in group_members.items():
        member_descs = [descs[i] for i in idxs]
        member_syms = [symbols[i] for i in idxs]
        label_str = auto_label(member_descs) if len(idxs) > 1 else names[idxs[0]]
        groups[gid] = {
            "label": label_str,
            "members": member_syms,
            "size": len(member_syms),
        }

    output = {
        "version": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "n_stocks": len(symbols),
        "n_groups": len(groups),
        "n_singletons": next_singleton,
        "groups": groups,
        "stock_to_group": sym_to_group,
    }

    OUT_FILE.write_text(
        json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Written: {OUT_FILE}  ({len(groups)} groups, {len(symbols)} stocks)")

    # Show largest groups as a sanity check
    sorted_groups = sorted(groups.items(), key=lambda x: x[1]["size"], reverse=True)
    print("\nTop 10 groups:")
    for gid, g in sorted_groups[:10]:
        print(f"  {gid} [{g['size']:3d}] {g['label']}: {', '.join(g['members'][:6])}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
