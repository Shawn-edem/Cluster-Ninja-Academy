import os

import streamlit as st

from open_ai_llm import llm_response

# from openai import OpenAI

st.set_page_config(
    page_title='Sport GPT',
    page_icon= "⚽️",
    layout='centered'

)

st.title("This is Sport GPT")

st.info("This is an Advance sport chatbot to analyse different sport😎")

# print("current",st.session_state)

user_prompt = st.chat_input('Please type your message here ')



if "messages" not in st.session_state:
    st.session_state.messages =  [
    {'role': 'system',
     'content': 'You are versatile Ai that knows everything about user and you chat with them naturally\n'
                'likewise you are very funny Ai you reply with emojies always and your real name is ClusterNinjaAcademy you know everyhting about Nigeria and Ai '}
]

if user_prompt:
    st.session_state.messages.append({'role':'user', 'content':user_prompt})
    # st.session_state.messages.append({'role':'assistant', "content":"Ai response"})



print("\n\ncurrent",st.session_state)

def load_messages():
    for message in st.session_state.messages:
        if message['role'] == 'system':
            continue
        with st.chat_message(message['role']):
            st.write(message['content'])


    if st.session_state.messages[-1]['role'] != 'assistant':
        with st.spinner("I am thinking...."):
            response = llm_response(user_input=user_prompt, memory=st.session_state.messages)
            st.session_state.messages.append({'role': 'assistant', "content": response})
            with st.chat_message('assistant'):
                st.write(response)

load_messages()

