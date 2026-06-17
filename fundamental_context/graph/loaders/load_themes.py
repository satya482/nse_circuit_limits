"""
Load Theme nodes with SUBTHEME_OF hierarchy into Neo4j.
Also seeds BENEFITS_FROM edges for a starter set of companies.
Writes graph_data/event_classifier.json (keyword -> theme map) for mobile Macro Simulator.

Run     : python load_themes.py
Re-run  : safe — idempotent via MERGE
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase

# ── Config ────────────────────────────────────────────────────────────────────
_HERE = Path(__file__).parent
_ENV = _HERE.parent.parent / ".env"
load_dotenv(_ENV)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "")

# Event classifier JSON output path (served by GitHub Pages)
EVENT_CLASSIFIER_PATH = (
    Path(__file__).parent.parent.parent.parent / "graph_data" / "event_classifier.json"
)


# ── Theme hierarchy ───────────────────────────────────────────────────────────
# Format: {name: {parent: str|None, maturity: str, thesis: str}}
THEMES: dict[str, dict] = {
    # Root themes
    "GovernmentCapex": {
        "parent": None,
        "maturity": "Growing",
        "thesis": "India's infrastructure push — multi-decade capex cycle across roads, railways, defence, and power. Government remains the primary demand driver.",
    },
    "ManufacturingTailwind": {
        "parent": None,
        "maturity": "Growing",
        "thesis": "PLI schemes + China+1 supply chain diversification driving domestic manufacturing across electronics, chemicals, and textiles.",
    },
    "FutureEconomy": {
        "parent": None,
        "maturity": "Emerging",
        "thesis": "Digital infrastructure, EV transition, speciality materials, and healthcare infrastructure — long runway, early innings.",
    },
    # GovernmentCapex sub-themes
    "InfraCapex": {
        "parent": "GovernmentCapex",
        "maturity": "Growing",
        "thesis": "Road, rail, port, and urban infra build-out. Order books visible 2–3 years ahead. Execution risk is the key variable.",
    },
    "Defence": {
        "parent": "GovernmentCapex",
        "maturity": "Growing",
        "thesis": "Atmanirbhar Bharat defence indigenisation. DPP + export ambitions. Long order visibility. DRDO transfers to private sector accelerating.",
    },
    "PowerCapex": {
        "parent": "GovernmentCapex",
        "maturity": "Growing",
        "thesis": "Transmission + renewable addition target 500 GW by 2030. T&D capex and generation build-out running in parallel.",
    },
    # InfraCapex sub-themes
    "Railways": {
        "parent": "InfraCapex",
        "maturity": "Growing",
        "thesis": "₹2.5L Cr annual railway budget. Dedicated freight corridors, Vande Bharat, metro rail. Multi-year order pipeline for rolling stock, signalling, and infra.",
    },
    "Roads": {
        "parent": "InfraCapex",
        "maturity": "Mature",
        "thesis": "NHAI + state road capex. High execution risk, competitive tendering. Prefer EPC players with strong balance sheets.",
    },
    "Ports": {
        "parent": "InfraCapex",
        "maturity": "Growing",
        "thesis": "Sagarmala programme + export-led growth. Mechanisation and capacity expansion driving equipment demand.",
    },
    # Defence sub-themes
    "Defence_Electronics": {
        "parent": "Defence",
        "maturity": "Emerging",
        "thesis": "Radars, avionics, electronic warfare, C4ISR systems. High-margin, long-cycle. Preferred route for indigenisation.",
    },
    "Defence_Platforms": {
        "parent": "Defence",
        "maturity": "Growing",
        "thesis": "Aircraft, ships, submarines, armoured vehicles. DPSU + private JVs. Long lead times but transformative order sizes.",
    },
    "Defence_MRO": {
        "parent": "Defence",
        "maturity": "Emerging",
        "thesis": "Maintenance, repair, overhaul for ageing fleet. Annuity-like recurring revenue once qualified. Under-tracked opportunity.",
    },
    # PowerCapex sub-themes
    "PowerT&D": {
        "parent": "PowerCapex",
        "maturity": "Growing",
        "thesis": "Transmission lines, substations, smart meters, cables. Demand driven by both new generation capacity and grid modernisation.",
    },
    "RenewableEnergy": {
        "parent": "PowerCapex",
        "maturity": "Growing",
        "thesis": "Solar + wind + green hydrogen. Equipment manufacturers, EPC players, and balance-of-plant suppliers all benefit.",
    },
    # ManufacturingTailwind sub-themes
    "PLI_Electronics": {
        "parent": "ManufacturingTailwind",
        "maturity": "Growing",
        "thesis": "Mobile + components + IT hardware PLI. Apple supply chain anchor. EMS players scaling to global standards.",
    },
    "PLI_Chemicals": {
        "parent": "ManufacturingTailwind",
        "maturity": "Emerging",
        "thesis": "Pharma + specialty chemical PLI. China+1 demand pull. API, CRAMS, agrochemicals benefiting from capacity addition.",
    },
    "China+1_Textiles": {
        "parent": "ManufacturingTailwind",
        "maturity": "Emerging",
        "thesis": "Global sourcing shift from China for garments + technical textiles. Requires scale and compliance infrastructure.",
    },
    "Semiconductor": {
        "parent": "ManufacturingTailwind",
        "maturity": "Emerging",
        "thesis": "India Semiconductor Mission. Early-stage but strategic. Packaging + ATMP first; fab longer-term. High geopolitical tailwind.",
    },
    # FutureEconomy sub-themes
    "DataCentre": {
        "parent": "FutureEconomy",
        "maturity": "Growing",
        "thesis": "AI + cloud + digital India driving 30%+ CAGR in data centre capacity. Power, cooling, UPS, and cable suppliers benefit.",
    },
    "EV_Components": {
        "parent": "FutureEconomy",
        "maturity": "Emerging",
        "thesis": "EV penetration accelerating in 2W, 3W, and buses first. Battery management, motors, and charging infra supply chain.",
    },
    "SpecialtyChemicals": {
        "parent": "FutureEconomy",
        "maturity": "Growing",
        "thesis": "High-complexity, low-volume chemicals with pricing power. Agrochemicals, dyes, CRAMS, fluorochemicals. China+1 + CDMO model.",
    },
    "Hospitals_HealthcareInfra": {
        "parent": "FutureEconomy",
        "maturity": "Growing",
        "thesis": "Under-bedded India building 1M+ hospital beds. Medical devices, diagnostics, and hospital chains all in multi-year capex.",
    },
}


# ── Starter BENEFITS_FROM edges ──────────────────────────────────────────────
# Map NSE code -> list of most-specific themes they benefit from
# Add more as needed; graph traversal handles upward (Railways -> InfraCapex -> GovernmentCapex)
SEED_BENEFITS: dict[str, list[str]] = {
    # Infrastructure / Railways
    "WELCORP": ["Railways", "InfraCapex"],
    "RVNL": ["Railways"],
    "IRFC": ["Railways"],
    "BEML": ["Railways", "Defence_Platforms"],
    "IRCON": ["Railways", "Roads"],
    "NBCC": ["InfraCapex"],
    "GPIL": ["InfraCapex"],
    # Defence — platforms & systems (mid-cap; BEL/HAL exceed MCap ceiling)
    "GRSE": ["Defence_Platforms"],  # frigates, patrol vessels
    "COCHINSHIP": ["Defence_Platforms"],  # naval shipbuilding
    "MIDHANI": ["Defence_Platforms"],  # superalloys for aero/defence
    "MTARTECH": ["Defence_Platforms", "Defence_Electronics"],  # precision for ISRO/DRDO
    "PARAS": ["Defence_Electronics"],  # optics, night vision
    "DATAPATTNS": ["Defence_Electronics"],  # defence electronics subsystems
    "IDEAFORGE": ["Defence_Electronics"],  # tactical drones
    "ASTRALDTX": ["Defence_Electronics"],  # radars, EW
    # Defence — electronics & cables
    "STLTECH": ["Defence_Electronics", "Railways"],
    "HFCL": ["Defence_Electronics", "Railways"],
    "KAYNES": ["Defence_Electronics", "PLI_Electronics"],
    # Power
    "HBLPOWER": ["PowerT&D", "DataCentre"],
    "KALPATPOWR": ["PowerT&D", "RenewableEnergy"],
    "POLYCAB": ["PowerT&D", "DataCentre"],
    "KEI": ["PowerT&D"],
    "TATAPOWER": ["RenewableEnergy", "PowerCapex"],
    "INOXWIND": ["RenewableEnergy"],
    "WAAREEENER": ["RenewableEnergy"],
    "CESC": ["PowerCapex"],
    # Manufacturing / PLI
    "DIXON": ["PLI_Electronics"],
    "KAYNESTECH": ["PLI_Electronics"],
    "APARINDS": ["EV_Components"],
    "MOTHERSON": ["EV_Components"],
    "MNRE": ["EV_Components"],
    "AARTIIND": ["SpecialtyChemicals", "PLI_Chemicals"],
    "DEEPAKFERT": ["SpecialtyChemicals"],
    "TATACHEM": ["PLI_Chemicals"],
    # Future economy
    "LALPATHLAB": ["Hospitals_HealthcareInfra"],
    "APOLLOHOSP": ["Hospitals_HealthcareInfra"],
    "YATHARTH": ["Hospitals_HealthcareInfra"],
}


# ── Cypher ────────────────────────────────────────────────────────────────────
_MERGE_THEME = """
MERGE (t:Theme {name: $name})
  ON CREATE SET
    t.theme_maturity = $maturity,
    t.vikram_thesis  = $thesis
  ON MATCH SET
    t.theme_maturity = $maturity,
    t.vikram_thesis  = $thesis
"""

_LINK_SUBTHEME = """
MATCH (child:Theme  {name: $child})
MATCH (parent:Theme {name: $parent})
MERGE (child)-[:SUBTHEME_OF]->(parent)
"""

_LINK_BENEFITS_FROM = """
MATCH (c:Company {nse_code: $nse_code})
MATCH (t:Theme   {name: $theme})
MERGE (c)-[r:BENEFITS_FROM]->(t)
  ON CREATE SET r.direct = true, r.magnitude = 'Medium'
"""


def load_themes(session) -> int:
    """Create Theme nodes and SUBTHEME_OF edges. Returns count of themes loaded."""
    for name, meta in THEMES.items():
        session.run(
            _MERGE_THEME, name=name, maturity=meta["maturity"], thesis=meta["thesis"]
        )
        print(f"[GRAPH] Theme MERGE | Theme | {name} | ok")

    for name, meta in THEMES.items():
        if meta["parent"]:
            session.run(_LINK_SUBTHEME, child=name, parent=meta["parent"])
            print(f"[GRAPH] SUBTHEME_OF | {name} -> {meta['parent']}")

    return len(THEMES)


def load_benefits(session) -> int:
    """Seed BENEFITS_FROM edges for starter company set. Returns edge count."""
    count = 0
    for nse_code, themes in SEED_BENEFITS.items():
        for theme in themes:
            result = session.run(_LINK_BENEFITS_FROM, nse_code=nse_code, theme=theme)
            if result.consume().counters.relationships_created > 0:
                print(f"[GRAPH] BENEFITS_FROM | {nse_code} -> {theme} | created")
            else:
                print(f"[GRAPH] BENEFITS_FROM | {nse_code} -> {theme} | exists")
            count += 1
    return count


def write_event_classifier() -> None:
    """Write keyword -> theme mapping JSON for mobile Macro Simulator."""
    classifier: dict[str, list[str]] = {
        "railway": ["Railways"],
        "railways": ["Railways"],
        "train": ["Railways"],
        "rvnl": ["Railways"],
        "irfc": ["Railways"],
        "dedicated freight": ["Railways"],
        "vande bharat": ["Railways"],
        "nhai": ["Roads"],
        "highway": ["Roads"],
        "road": ["Roads"],
        "port": ["Ports"],
        "sagarmala": ["Ports"],
        "defence": ["Defence"],
        "defense": ["Defence"],
        "drdo": ["Defence", "Defence_Electronics"],
        "dpp": ["Defence"],
        "dac": ["Defence"],
        "atmanirbhar": ["Defence", "ManufacturingTailwind"],
        "missile": ["Defence_Platforms"],
        "aircraft": ["Defence_Platforms"],
        "warship": ["Defence_Platforms"],
        "radar": ["Defence_Electronics"],
        "avionics": ["Defence_Electronics"],
        "mro": ["Defence_MRO"],
        "maintenance repair": ["Defence_MRO"],
        "power": ["PowerT&D", "RenewableEnergy"],
        "transmission": ["PowerT&D"],
        "substation": ["PowerT&D"],
        "smart meter": ["PowerT&D"],
        "cable": ["PowerT&D"],
        "solar": ["RenewableEnergy"],
        "wind": ["RenewableEnergy"],
        "green hydrogen": ["RenewableEnergy"],
        "renewable": ["RenewableEnergy"],
        "nuclear": ["PowerCapex"],
        "pli": ["PLI_Electronics", "PLI_Chemicals"],
        "production linked": ["PLI_Electronics", "PLI_Chemicals"],
        "semiconductor": ["Semiconductor"],
        "chip": ["Semiconductor"],
        "fab": ["Semiconductor"],
        "atmp": ["Semiconductor"],
        "data centre": ["DataCentre"],
        "data center": ["DataCentre"],
        "ai": ["DataCentre"],
        "cloud": ["DataCentre"],
        "ev": ["EV_Components"],
        "electric vehicle": ["EV_Components"],
        "battery": ["EV_Components"],
        "charging": ["EV_Components"],
        "specialty chemical": ["SpecialtyChemicals"],
        "speciality chemical": ["SpecialtyChemicals"],
        "agrochemical": ["SpecialtyChemicals", "PLI_Chemicals"],
        "pharma": ["PLI_Chemicals"],
        "crams": ["PLI_Chemicals", "SpecialtyChemicals"],
        "china+1": ["China+1_Textiles", "PLI_Chemicals"],
        "china plus": ["China+1_Textiles", "ManufacturingTailwind"],
        "textile": ["China+1_Textiles"],
        "hospital": ["Hospitals_HealthcareInfra"],
        "healthcare": ["Hospitals_HealthcareInfra"],
        "medical": ["Hospitals_HealthcareInfra"],
        "ems": ["PLI_Electronics"],
        "electronics": ["PLI_Electronics"],
        "capex": ["InfraCapex", "GovernmentCapex"],
        "infrastructure": ["InfraCapex"],
        "infra": ["InfraCapex"],
        "budget": ["GovernmentCapex"],
        "government": ["GovernmentCapex"],
    }

    EVENT_CLASSIFIER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(EVENT_CLASSIFIER_PATH, "w", encoding="utf-8") as fh:
        json.dump(classifier, fh, indent=2, ensure_ascii=False)
    print(f"[JSON] event_classifier.json written -> {EVENT_CLASSIFIER_PATH}")


def main() -> None:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    with driver.session() as session:
        n_themes = load_themes(session)
        n_benefits = load_benefits(session)
    driver.close()

    write_event_classifier()

    print(
        f"[GRAPH] Summary | {n_themes} themes | "
        f"{n_benefits} BENEFITS_FROM edges seeded"
    )


if __name__ == "__main__":
    main()
