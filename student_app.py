import json
import os
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Win With Us",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Aggressive CSS to hide headers, toolbars, and footers completely
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {visibility: hidden; display: none;}
    [data-testid="stFooter"] {visibility: hidden; display: none;}
    [data-testid="stToolbar"] {visibility: hidden; display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. Data Management Functions
DATA_FILE = "questions.json"


def load_questions():
  if os.path.exists(DATA_FILE):
    try:
      with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    except Exception:
      return {}
  return {}


def append_question_to_json(
    chapter_name,
    stem,
    options,
    correct_option,
    youtube_link,
    difficulty="Moderate",
):
  data = load_questions()

  if chapter_name not in data:
    data[chapter_name] = []

  existing_ids = [q.get("id", 0) for q in data[chapter_name]]
  next_id = max(existing_ids) + 1 if existing_ids else 1

  new_question = {
      "id": next_id,
      "difficulty": difficulty,
      "stem": stem,
      "options": options,
      "correct": correct_option.strip(),
      "youtube_url": youtube_link.strip(),
  }

  data[chapter_name].append(new_question)

  with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

  return next_id


# 4. Load Question Bank
data = load_questions()

st.title("🏆 Win With Us")
st.subheader("Maths Tricks & Logics and Aptitude Practice Portal")
st.markdown("---")

if not data:
  st.warning(
      "No questions found yet! Open the sidebar Admin Panel to add your first"
      " chapter and questions."
  )
else:
  # Chapter Selection
  chapters = list(data.keys())
  selected_chapter = st.selectbox("📚 Select Chapter / Topic", chapters)

  if selected_chapter and data[selected_chapter]:
    questions_list = data[selected_chapter]

    st.markdown(
        f"### Practice: {selected_chapter} ({len(questions_list)} Questions)"
    )

    # Render Question Cards
    for idx, q in enumerate(questions_list):
      with st.container():
        st.markdown(
            f"**Q{idx+1}) [{q.get('difficulty', 'Moderate')}]** {q['stem']}"
        )

        user_choice = st.radio(
            "Choose option:", q["options"], key=f"q_{selected_chapter}_{q['id']}"
        )

        if st.button("Check Answer", key=f"btn_{selected_chapter}_{q['id']}"):
          if user_choice.startswith(q["correct"]):
            st.success("✅ Correct! Great logic.")
          else:
            st.error(f"❌ Incorrect. The correct answer is {q['correct']}")

          if q.get("youtube_url"):
            st.markdown(
                f"💡 [Watch Video Explanation & Shortcut]"
                f"({q['youtube_url']})"
            )
        st.markdown("---")

# 5. Secure Admin Panel (Sidebar)
with st.sidebar.expander("🛠️ Admin: Add Question"):
  admin_pass = st.text_input("Admin Passcode", type="password")
  if admin_pass == "1234":  # Change to your preferred passcode
    existing_topics = list(data.keys()) if data else []
    target_topic = st.selectbox(
        "Target Chapter", existing_topics + ["➕ Add New Chapter"]
    )

    if target_topic == "➕ Add New Chapter":
      target_topic = st.text_input("New Chapter Name")

    new_stem = st.text_area("Question Stem / Text")
    diff = st.selectbox("Difficulty", ["Easy", "Moderate", "Difficult"])

    opt_a = st.text_input("Option A", value="(A) ")
    opt_b = st.text_input("Option B", value="(B) ")
    opt_c = st.text_input("Option C", value="(C) ")
    opt_d = st.text_input("Option D", value="(D) ")

    correct_ans = st.selectbox(
        "Correct Option Prefix", ["(A)", "(B)", "(C)", "(D)"]
    )
    yt_url = st.text_input("YouTube Solution URL")

    if st.button("Save & Append Question"):
      if target_topic and new_stem:
        options_list = [opt_a, opt_b, opt_c, opt_d]
        new_id = append_question_to_json(
            target_topic, new_stem, options_list, correct_ans, yt_url, diff
        )
        st.success(
            f"Successfully added Q{new_id} to {target_topic}! Refresh page to"
            " view."
        )
      else:
        st.error("Please provide a chapter name and question text.")
  elif admin_pass:
    st.error("Incorrect Passcode")
