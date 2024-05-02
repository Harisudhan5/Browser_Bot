import streamlit as st

st.title('WebChat')

with st.sidebar:
    st.header('Settings')
    website_url = st.text_input("Enter any URL")

user_query = st.chat_input("Ask a query")

if user_query is not None and user_query != "":
    with st.chat_message("Human"):
        st.write(user_query)
    with st.chat_message("AI"):
        st.write("Yet to develop")



