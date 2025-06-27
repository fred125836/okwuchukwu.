import streamlit as st
import time

# Set page config
st.set_page_config(page_title="Custom Chatbot", layout="centered")

# Initialize chat history in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom chatbot logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there!"
    elif "your name" in user_input:
        return "I'm your Streamlit chatbot."
    elif "who developed this website" in user_input:
        return "okwuchukwu onwuegbuna."
    elif "time" in user_input:
        return "I don't have a watch, but it's always a good time to chat!"
    elif "there" in user_input:
        return "you are there"
    elif "how are you doing" in user_input:
        return """
            I'm doing good today,
            thanks for asking
            """
    elif "who is the president of nigeria" in user_input:
        return "Jude onwuegbuna"
    elif "who is the governor of lagos state" in user_input:
        return "Peace Ejirooghene Ogosime"
    elif "how was your night" in user_input:
        return "my night went pretty well, thanks for asking"
    elif "how much can i obtain the software" in user_input:
        return "you can obtain the software for $100 annaully"
    elif "what are the names of stp staff" in user_input:
        return "Tosin, Tijani, Dorcas and Olamide"
    else:
        return "Sorry, I don't understand that yet."

# Title
st.title("💬 Custom Chatbot")

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input field + send button
user_input = st.chat_input("Ask something...")
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Simulate thinking delay
    with st.chat_message("assistant"):
        bot_placeholder = st.empty()
        bot_placeholder.markdown("loading...")
        time.sleep(1)  # Simulated delay
        response = get_bot_response(user_input)
        bot_placeholder.markdown(response)

    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
