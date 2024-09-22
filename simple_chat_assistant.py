import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

# Streamlit UI
st.title("Simple Chat Assistant")

st.markdown('''This is a simple chat app using a Groq LLM model (llama3-8b-8192) for response generation.''')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What would you like to chat about?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        response = llm.invoke(prompt)
        message_placeholder.markdown(response.content)

    st.session_state.messages.append({"role": "assistant", "content": response.content})