"""
NSE Symbol Resolver

Maps Claude-extracted company symbols/names to correct NSE codes using:
  1. Exact match on NSE Code
  2. Fuzzy symbol match (difflib, Levenshtein-like)
  3. Exact normalized name match
  4. Fuzzy name match
  5. Token-overlap name match

Non-NSE companies (e.g. US-listed Yellow Cake, Centrus) get confidence=0.

Usage:
  from telegram_symbol_resolver import Resolver
  r = Resolver()
  nse_code, conf, method = r.resolve("PGRD", "Power Grid Corporation of India")
  # → ("POWERGRID", 0.91, "fuzzy_name")
"""

from __future__ import annotations

import csv
import difflib
import json
import re
from functools import cached_property
from pathlib import Path

_HERE = Path(__file__).parent
_UNIVERSE_CSV = _HERE / "NSE_500cr_15CrNotional10D_50rs_sector_industry.csv"
_LABELS_JSON = _HERE / "tools" / "stock_labels.json"

# Suffixes stripped before name comparison — only true legal/corporate forms,
# NOT domain words (energy, power, tech, bank …) that distinguish company identity.
_SUFFIX_RE = re.compile(
    r"\b(ltd\.?|limited|pvt\.?|private|corp\.?|corporation|co\.?|"
    r"inc\.?|plc\.?|llp|llc|"
    r"india|indian|international|global|"
    r"holding(?:s)?|group|venture(?:s)?)\b",
    re.IGNORECASE,
)

# Known non-NSE exchange indicators in the symbol
_NON_NSE_RE = re.compile(r"\.(L|AX|TO|HK|PA|T|F|DE|SW)$", re.IGNORECASE)

# US ticker heuristics: 1-4 UPPER letters with no digit, common US tickers
_US_TICKERS = {
    "HON",
    "UEC",
    "CNTRF",
    "CCJ",
    "NXE",
    "DNN",
    "URG",
    "LEU",
    "UUUU",
    "GE",
    "BA",
    "LMT",
    "RTX",
    "NOC",
    "HII",
    "GD",
}


def _normalize(name: str) -> str:
    """Lowercase, strip legal suffixes and punctuation, collapse spaces."""
    name = name.lower().strip()
    name = _SUFFIX_RE.sub(" ", name)
    name = re.sub(r"[^a-z0-9 ]", " ", name)
    return re.sub(r"\s+", " ", name).strip()


def _clean_sym(symbol: str) -> str:
    """Remove .BO/.NS/exchange suffixes, uppercase."""
    s = re.sub(r"\.(BO|NS|NSE|BSE|NM)$", "", symbol.strip(), flags=re.IGNORECASE)
    return s.upper()


class Resolver:
    def __init__(self, threshold: float = 0.72):
        self.threshold = threshold

    @cached_property
    def _universe(self) -> tuple[dict[str, str], dict[str, str], list[str]]:
        """
        Returns:
          nse_to_name : {NSE_CODE: "Stock Name"}
          norm_to_nse : {normalized_name: NSE_CODE}
          all_codes   : sorted list of NSE codes (for difflib)
        """
        nse_to_name: dict[str, str] = {}
        norm_to_nse: dict[str, str] = {}

        if not _UNIVERSE_CSV.exists():
            return nse_to_name, norm_to_nse, []

        with open(_UNIVERSE_CSV, encoding="cp1252") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                code = (row.get("NSE Code") or "").strip().upper()
                name = (row.get("Stock Name") or "").strip()
                if code and name:
                    nse_to_name[code] = name
                    norm = _normalize(name)
                    if norm:
                        norm_to_nse[norm] = code

        # Also pull any codes from stock_labels.json not in CSV
        if _LABELS_JSON.exists():
            with open(_LABELS_JSON, encoding="utf-8") as fh:
                labels: dict[str, str] = json.load(fh)
            for code, desc in labels.items():
                if code not in nse_to_name:
                    nse_to_name[code] = desc[:60]
                    norm = _normalize(desc[:60])
                    if norm:
                        norm_to_nse.setdefault(norm, code)

        all_codes = sorted(nse_to_name.keys())
        return nse_to_name, norm_to_nse, all_codes

    def resolve(
        self,
        symbol: str,
        name: str = "",
    ) -> tuple[str | None, float, str]:
        """
        Resolve to (nse_code, confidence, method).
        confidence 0–1; method is a short tag.
        Returns (None, 0.0, "non_nse") if likely not an NSE stock.
        """
        nse_to_name, norm_to_nse, all_codes = self._universe
        if not nse_to_name:
            return None, 0.0, "no_universe"

        # ── 0. Likely non-NSE signals ──────────────────────────────────────
        clean = _clean_sym(symbol)
        if _NON_NSE_RE.search(symbol):
            return None, 0.0, "non_nse"
        if clean in _US_TICKERS:
            return None, 0.0, "non_nse"

        # ── 1. Exact symbol match ──────────────────────────────────────────
        if clean in nse_to_name:
            return clean, 1.0, "exact"

        # ── 2. Fuzzy symbol match ──────────────────────────────────────────
        sym_matches = difflib.get_close_matches(
            clean, all_codes, n=3, cutoff=self.threshold
        )
        best_sym_score = 0.0
        best_sym_code = None
        for cand in sym_matches:
            score = difflib.SequenceMatcher(None, clean, cand).ratio()
            if score > best_sym_score:
                best_sym_score = score
                best_sym_code = cand

        # ── 3. Name-based matching ─────────────────────────────────────────
        norm_extracted = _normalize(name) if name else ""
        best_name_score = 0.0
        best_name_code = None

        if norm_extracted:
            # 3a. Exact normalized name
            if norm_extracted in norm_to_nse:
                best_name_score = 0.97
                best_name_code = norm_to_nse[norm_extracted]

            # 3b. Fuzzy normalized name
            if best_name_score < 0.9:
                norm_keys = list(norm_to_nse.keys())
                name_matches = difflib.get_close_matches(
                    norm_extracted, norm_keys, n=3, cutoff=self.threshold
                )
                for cand_norm in name_matches:
                    score = difflib.SequenceMatcher(
                        None, norm_extracted, cand_norm
                    ).ratio()
                    if score > best_name_score:
                        best_name_score = score * 0.93  # slight penalty vs exact
                        best_name_code = norm_to_nse[cand_norm]

            # 3c. Token overlap (handles partial name matches)
            if best_name_score < 0.80:
                ext_tokens = set(norm_extracted.split()) - {""}
                if len(ext_tokens) >= 2:
                    for norm_key, code in norm_to_nse.items():
                        key_tokens = set(norm_key.split()) - {""}
                        if not key_tokens:
                            continue
                        overlap = len(ext_tokens & key_tokens)
                        if overlap == 0:
                            continue
                        score = overlap / max(len(ext_tokens), len(key_tokens))
                        # Bonus if all extracted tokens hit
                        if ext_tokens <= key_tokens:
                            score = min(score * 1.2, 1.0)
                        if score > best_name_score and score >= 0.55:
                            best_name_score = score * 0.88
                            best_name_code = code

        # ── 4. Pick winner: name match wins if significantly better ────────
        if best_name_code and best_name_score >= best_sym_score:
            method = (
                "name_exact"
                if best_name_score > 0.93
                else "fuzzy_name" if best_name_score > 0.78 else "token_name"
            )
            if best_name_score >= self.threshold * 0.85:
                return best_name_code, best_name_score, method

        if best_sym_code and best_sym_score >= self.threshold:
            return best_sym_code, best_sym_score, "fuzzy_symbol"

        # ── 5. No confident match ──────────────────────────────────────────
        return None, 0.0, "unresolved"

    def resolve_company(self, company: dict) -> dict:
        """Enrich a company dict with nse_code + resolver metadata."""
        sym = company.get("symbol") or ""
        name = company.get("name") or ""
        nse_code, conf, method = self.resolve(sym, name)
        return {
            **company,
            "nse_code": nse_code,
            "res_conf": round(conf, 3),
            "res_method": method,
        }


# ── CLI for quick testing ──────────────────────────────────────────────────────
if __name__ == "__main__":

    r = Resolver()
    test_cases = [
        ("CAPILLAR", "Capillary Technologies India"),
        ("SOIL", "Solar Industries India"),
        ("NTPC", "NTPC Limited"),
        ("PGRD", "Power Grid Corporation of India"),
        ("TTPW", "Tata Power"),
        ("JSWE", "JSW Energy"),
        ("UEC", "Yellow Cake"),
        ("HON", "SOLS (Honeywell spinoff)"),
        ("CNTRF", "Centrus"),
        ("HITACHIENERGY", "Hitachi Energy India"),
        ("SHADOWF", "ShadowFax Technologies"),
        ("DELHIVERY", "Delhivery"),
    ]
    print(f"{'Sym':<16} {'Name':<38} {'-> NSE Code':<14} {'Conf':>5}  Method")
    print("-" * 90)
    for sym, name in test_cases:
        code, conf, method = r.resolve(sym, name)
        display = code or "—"
        flag = "OK" if conf >= 0.85 else ("~" if conf >= 0.6 else "X")
        print(f"{sym:<16} {name:<38} {flag} {display:<12} {conf:>5.2f}  {method}")
