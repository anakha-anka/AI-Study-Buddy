import streamlit as st
from huggingface_hub import InferenceClient
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Study Buddy", layout="centered")
st.title("📚 AI Study Buddy")
st.write("AI-powered explanations, quizzes and flashcards for students")

# ---------------- LOAD HF TOKEN ----------------
HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=HF_TOKEN
)

# ---------------- PDF FUNCTION ----------------
def generate_pdf(content_text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for line in content_text.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 8))

    doc.build(story)
    buffer.seek(0)
    return buffer

# ---------------- AI FUNCTION ----------------
def ask_ai(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful study assistant for students."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat_completion(
        messages=messages,
        max_tokens=700,
        temperature=0.7
    )

    return response.choices[0].message.content

# ---------------- USER INPUT ----------------
topic = st.text_area(
    "📘 Enter your topic or question",
    placeholder="Eg: Water Cycle, AI, Climate Change"
)

option = st.selectbox(
    "What do you want?",
    ["Explain", "Summarize", "Generate Quiz", "Generate Flash Cards"]
)

# ---------------- GENERATE BUTTON ----------------
if st.button("Generate"):

    if topic.strip() == "":
        st.error("Please enter a topic")
        st.stop()

    st.success("AI Generated Successfully ✅")
    pdf_text = ""

    # ---------------- PROMPT LOGIC ----------------
    if option == "Explain":
        prompt = f"Explain {topic} clearly with examples for students."

    elif option == "Summarize":
        prompt = f"Summarize {topic} in simple bullet points."

    elif option == "Generate Quiz":
        prompt = f"Create 5 quiz questions with answers about {topic}."

    else:
        prompt = f"""
Create 6 short important key points about {topic}.
Each point should be ONE short sentence.
Return each point on a new line only.
Do not add numbering or extra text.
"""

    # ---------------- AI CALL ----------------
    try:
        with st.spinner("Thinking... 🤖"):
            result = ask_ai(prompt)

        st.subheader("🧠 AI Output")
        pdf_text += f"{option.upper()} OUTPUT\n\n{result}\n\n"

        # ---------------- FLASHCARD UI ----------------
        if option == "Generate Flash Cards":
            cards = [c.strip() for c in result.split("\n") if c.strip()]
            colors = ["#2563eb", "#7c3aed", "#059669", "#db2777"]
            card_no = 1

            for card in cards:
                bg_color = colors[card_no % len(colors)]

                st.markdown(
                    f"""
                    <div style="
                        background:{bg_color};
                        padding:18px;
                        border-radius:15px;
                        margin-bottom:15px;
                        color:white;
                        font-size:17px;
                        box-shadow:2px 2px 12px rgba(0,0,0,0.4);
                    ">
                    <b>Flash Card {card_no}</b><br><br>
                    {card}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                card_no += 1

        else:
            st.write(result)

    except Exception as e:
        st.error(f"AI Error: {e}")

    # ---------------- DOWNLOAD PDF ----------------
    st.markdown("---")
    st.subheader("⬇️ Download Notes as PDF")

    pdf_file = generate_pdf(pdf_text)

    st.download_button(
        label="Download PDF",
        data=pdf_file,
        file_name="AI_Study_Notes.pdf",
        mime="application/pdf"
    )
