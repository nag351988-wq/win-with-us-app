import streamlit as st
import json
import os

st.set_page_config(
    page_title="Win With Us",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject PWA Manifest and Icon directly into Streamlit's HTML head
st.markdown("""
<link rel="manifest" href="https://raw.githubusercontent.com/nag351988-wq/win-with-us-app/main/manifest.json">
<link rel="apple-touch-icon" href="https://raw.githubusercontent.com/nag351988-wq/win-with-us-app/main/icon.png">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        background-color: #0b0f19 !important;
        color: #f8fafc !important;
    }
    .stApp {
        background-color: #0b0f19 !important;
    }
    .brand-header {
        text-align: center;
        padding: 10px 0 20px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 20px;
    }
    .brand-title {
        font-size: 26px;
        font-weight: 900;
        background: linear-gradient(90deg, #fbbf24 0%, #f59e0b 50%, #f43f5e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-transform: uppercase;
    }
    .brand-sub {
        color: #94a3b8;
        font-size: 13px;
        font-weight: 600;
    }
    .question-card {
        background-color: #131c2e;
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)
