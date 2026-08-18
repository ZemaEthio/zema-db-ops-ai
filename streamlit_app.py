"""Streamlit entry point for the ZEMA DB Operations AI MVP."""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


ROOT = Path(__file__).parent


def build_embedded_app() -> str:
    """Inline the dependency-free frontend for Streamlit Community Cloud."""
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    javascript = (ROOT / "app.js").read_text(encoding="utf-8")
    html = html.replace('<link rel="stylesheet" href="styles.css" />', f"<style>{css}</style>")
    html = html.replace('<script src="app.js"></script>', f"<script>{javascript}</script>")
    return html


st.set_page_config(
    page_title="ZEMA DB Operations AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, header, footer { visibility: hidden; }
      .stApp, [data-testid="stAppViewContainer"] { background: #07111f; }
      .block-container { padding: 0; max-width: 100%; }
      iframe { border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(build_embedded_app(), height=1240, scrolling=True)
