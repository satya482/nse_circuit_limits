_TEXT = (
    "I am not a SEBI registered investment advisor. "
    "All content is for educational and informational purposes only and does not constitute investment advice. "
    "Please consult a SEBI registered investment advisor before making any investment decisions. "
    "Investments in securities market are subject to market risks, "
    "read all related documents carefully before investing."
)

# --- Markdown ---

SEBI_MD_HEADER = f"> ⚠️ **Disclaimer:** {_TEXT}\n"

SEBI_MD_FOOTER = f"\n---\n\n*⚠️ Disclaimer: {_TEXT}*\n"

# --- HTML ---

_HTML_STYLE = (
    "padding:12px 20px;border-radius:6px;font-size:12px;line-height:1.6;"
    "background:#1a1a1a;border:1px solid #444;color:#aaa;margin:0 0 16px 0;"
)
_HTML_FOOTER_STYLE = (
    "margin-top:40px;padding:14px 20px;border-top:1px solid #333;"
    "font-size:11px;color:#888;text-align:center;line-height:1.6;"
)

SEBI_HTML_BANNER = f'<div style="{_HTML_STYLE}">&#9888; <strong style="color:#f0c040;">Disclaimer:</strong> {_TEXT}</div>'

SEBI_HTML_FOOTER = (
    f'<footer style="{_HTML_FOOTER_STYLE}">'
    f"&#9888; <strong>Disclaimer:</strong> {_TEXT}"
    f"</footer>"
)
