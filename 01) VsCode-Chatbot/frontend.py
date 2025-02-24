import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Streamlit Page Configuration
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# Detect Dark Mode
dark_mode = st.get_option("theme.base") == "dark"

# Custom Styling for Dark and Light Modes
st.markdown(f"""
    <style>
        .chat-container {{
            background-color: {'#1e1e1e' if dark_mode else '#f4f4f4'};
            padding: 20px;
            border-radius: 10px;
        }}
        .user-message {{
            background-color: {'#007BFF' if not dark_mode else '#0056b3'};
            color: white;
            padding: 10px;
            border-radius: 10px;
            text-align: right;
            margin: 5px 0;
        }}
        .bot-message {{
            background-color: {'#EAEAEA' if not dark_mode else '#333'};
            color: {'black' if not dark_mode else 'white'};
            padding: 10px;
            border-radius: 10px;
            text-align: left;
            margin: 5px 0;
        }}
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 AI Chatbot using Gemini")

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=os.getenv("key"))

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    role, text = msg
    div_class = "user-message" if role == "User" else "bot-message"
    st.markdown(f"<div class='{div_class}'>{text}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# User Input
user_input = st.text_input("Enter your message:", key="user_input")
if user_input:
    st.session_state.messages.append(("User", user_input))
    response = llm.invoke(user_input)
    formatted_response = f"\n\n**Response:**\n\n{response.content}"  # Format response nicely
    st.session_state.messages.append(("Bot", formatted_response))
    st.experimental_rerun()
