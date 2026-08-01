import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Mini Groq Chatbot", page_icon="✨", layout="centered")

# ---------- GLASSMORPHISM CSS ----------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #1a1a2e, #0f0f1a 70%);
    color: #e0e0ff;
}

/* Title */
h1 {
    background: linear-gradient(90deg, #00f0ff, #a855f7, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 30px rgba(168, 85, 247, 0.4);
    font-weight: 800 !important;
}

/* Chat message bubbles - glass effect */
[data-testid="stChatMessage"] {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 16px;
    padding: 12px 16px;
    margin-bottom: 10px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
}
[data-testid="stChatMessage"]:hover {
    border: 1px solid rgba(168, 85, 247, 0.5);
    box-shadow: 0 0 20px rgba(168, 85, 247, 0.25);
}

/* Chat input box */
[data-testid="stChatInput"] textarea {
    background: rgba(255, 255, 255, 0.07) !important;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 240, 255, 0.3) !important;
    border-radius: 14px !important;
    color: #e0e0ff !important;
    box-shadow: 0 0 15px rgba(0, 240, 255, 0.1);
}
[data-testid="stChatInput"] textarea:focus {
    border: 1px solid rgba(0, 240, 255, 0.8) !important;
    box-shadow: 0 0 25px rgba(0, 240, 255, 0.35) !important;
}

/* Spinner glow */
.stSpinner > div {
    border-top-color: #a855f7 !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-thumb {
    background: rgba(168, 85, 247, 0.4);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("✨ Mini Groq Chatbot")
st.caption("Powered by Groq + Llama 3.3 — glass UI edition")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful, friendly assistant."}
    ]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=1024,
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
