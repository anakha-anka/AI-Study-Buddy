# 📚 AI Study Buddy

AI Study Buddy is an AI-powered web application that helps students learn effectively by generating explanations, summaries, quizzes, and colorful flash cards for any topic using Hugging Face AI models. Built with Python, Streamlit, and Hugging Face API.

## 🚀 Features
- Explain any topic clearly with examples
- Summarize topics into short notes
- Generate quiz questions with answers
- Generate colorful flash cards with important points
- Download generated notes as PDF
- Simple and clean user interface
- Runs directly in the browser

## 🛠 Technologies Used
- Python
- Streamlit
- Hugging Face API
- huggingface_hub
- reportlab
- HTML/CSS (Streamlit UI)

## 🔑 API Setup (Hugging Face)

1. Go to: https://huggingface.co/settings/tokens  
2. Click "New Token"  
3. Select "Read Access"  
4. Copy the generated token  

Create a folder named `.streamlit` inside your project directory.

Inside `.streamlit`, create a file named `secrets.toml`.

Add the following line inside the file:
HF_TOKEN = "your_huggingface_token_here"

Save the file.

## 📦 Installation

Open Terminal inside the project folder and run:
pip install streamlit huggingface_hub reportlab

## ▶️ Run the Application

Run the command:
streamlit run app.py

Open in browser:
http://localhost:8501

## 🌈 How to Use

1. Enter a topic (example: Water Cycle, Artificial Intelligence, Climate Change).
2. Select an option: Explain, Summarize, Generate Quiz, or Generate Flash Cards.
3. Click Generate.
4. View AI output and colorful flash cards.
5. Download notes as PDF if required.


##  Developed By
Anakha A
