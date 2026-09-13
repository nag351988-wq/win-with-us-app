import streamlit as st
import json
import os

st.set_page_config(
    page_title="Win With Us",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject PWA Manifest and Icon directly into Streamlit's HTML head for PWABuilder
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

# App Header
st.markdown("""
<div class="brand-header">
    <div class="brand-title">🏆 Win With Us</div>
    <div class="brand-sub">Maths Tricks & Logics | Aptitude Practice Portal</div>
</div>
""", unsafe_allow_html=True)

# Load JSON Data Safely
@st.cache_data
def load_data():
    if os.path.exists("questions.json"):
        with open("questions.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"Percentages": [{"id": 1, "difficulty": "Moderate", "stem": "Sample: If 20% of a number is 120, find 40%.", "options": ["(A) 200", "(B) 240", "(C) 300", "(D) 320"], "correct": "(B)", "youtube_url": "https://youtube.com"}]}

data = load_data()

# Topic Selector Dropdown
topic_list = list(data.keys())
selected_topic = st.selectbox("📂 Select Topic / Chapter:", topic_list)

st.divider()

# Render Questions
questions = data.get(selected_topic, [])
st.markdown(f"### 📚 Practice: {selected_topic} ({len(questions)} Questions)")

for idx, q in enumerate(questions):
    star_map = {"Easy": "⭐", "Moderate": "⭐⭐", "Difficult": "⭐⭐⭐"}
    stars = star_map.get(q.get("difficulty", "Moderate"), "⭐⭐")
    
    with st.container():
        st.markdown(f"""
        <div class="question-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 800; color: #38bdf8;">Q{idx+1})</span>
                <span style="font-size: 14px;">{stars}</span>
            </div>
            <div style="font-size: 15px; font-weight: 600; color: #ffffff; margin-bottom: 12px;">
                {q['stem']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        user_choice = st.radio(
            f"Select option for Q{idx+1}:", 
            q["options"], 
            key=f"q_{idx}", 
            label_visibility="collapsed"
        )
        
        col_btn, col_res = st.columns([1, 2])
        with col_btn:
            check_clicked = st.button("Check Answer", key=f"btn_{idx}")
            
        if check_clicked:
            clean_user = user_choice.split()[0]
            clean_correct = q["correct"].strip()
            
            if clean_user == clean_correct:
                st.success("🟢 Correct! Excellent calculation.")
            else:
                st.error(f"🔴 Incorrect. The correct answer is **{q['correct']}**.")
                
            if q.get("youtube_url"):
                st.markdown(f"""
                <div style="margin-top: 10px;">
                    <a href="{q['youtube_url']}" target="_blank" style="display: inline-block; background: #dc2626; color: white; padding: 8px 16px; border-radius: 6px; font-weight: 700; text-decoration: none; font-size: 13px;">
                        📺 Watch Detailed Solution on YouTube
                    </a>
                </div>
                """, unsafe_allow_html=True)
                
        st.write("")
        st.divider()
# Inject PWA Manifest, Favicon, and Icon directly into Streamlit's HTML head
st.markdown("""
<link rel="manifest" href="https://raw.githubusercontent.com/nag351988-wq/win-with-us-app/main/manifest.json">
<link rel="icon" type="image/png" href="https://raw.githubusercontent.com/nag351988-wq/win-with-us-app/main/icon.png">
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
