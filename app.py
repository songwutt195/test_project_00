import streamlit as st
import google.generativeai as genai

try:
    # genai.configure(api_key='AIzaSyBYl0fF5LxGSI1DJ6i7GEF9oBzEO_UXu6I')
    key = st.secrets['gemini']['api_key']
    model = genai.GenerativeModel('gemini-2.0-flash-lite')

    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])
    st.title('Gemini Pro Test')

    def role_to_streamlit(role:str) -> str:
        if role == 'model':
            return 'assistant'
        else:
            return role

    for message in st.session_state.chat.history:
        with st.chat_message(role_to_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    if prompt := st.chat_input("aaaa"):
        st.chat_message('user').markdown(prompt)
        response = st.session_state.chat.send_message(prompt)
        with st.chat_message('assistant'):
            st.markdown(response.text)
except Exception as e:
    st.error(f'An error occurred {e}')