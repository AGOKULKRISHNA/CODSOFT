import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# --- ChatBot Initialization and Training ---
# Only initialize and train the bot once to avoid retraining on every rerun
@st.cache_resource
def initialize_chatbot():
    bot = ChatBot("Uttam")
    trainer = ListTrainer(bot)
    trainer.train(
        [
            'Hi',
            'Hello',
            'How are you?',
            'I am fine thank you. What about you?',
            'I am also fine',
            'Nice to hear that',
            'What is your name?',
            'My name is uttam',
            'Thank you',
            'You are most welcome',
            'কেমন আছেন?',
            'আমি ভালো আছি'
        ]
    )
    return bot

bot = initialize_chatbot()

# --- Streamlit Application Layout ---
st.title("Uttam ChatBot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Say something to Uttam...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response
    bot_response = str(bot.get_response(user_input)) # Ensure response is string

    # Add bot message to chat history
    st.session_state.messages.append({"role": "bot", "content": bot_response})
    with st.chat_message("bot"):
        st.markdown(bot_response)
