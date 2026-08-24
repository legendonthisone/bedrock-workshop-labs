"""The presentation layer for the streamlit app"""

import streamlit as st
import ui_demo_logic

st.set_page_config(page_title="Chatbot")
st.title("Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

chat_container = st.container()

for message in st.session_state.chat_history:
    with chat_container.chat_message(message.role):
        st.markdown(message.text)

input_text = st.chat_input("Chat with your bot here")

if input_text:
    with chat_container.chat_message("user"):
        st.markdown(input_text)

    with st.spinner("Thinking...."):
        response = ui_demo_logic.chat_with_agent(message_history=st.session_state.chat_history, new_text=input_text)

        with chat_container.chat_message("assistant"):
            st.markdown(response)
