import streamlit as st
from langchain_core.messages import AIMessage,HumanMessage

def get_response(user_input):
    return "Yet to develop"

st.title('WebChat - Insert an URL of any web page and start asking your queries')

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content = "Hello, I'm a Website Bot, How can I help you?"),
    ]
    
with st.sidebar:
    st.header('Settings')
    website_url = st.text_input("Enter any URL")

    
if website_url is None or website_url == "":
    st.info("Please Enter a URL")

else:
    user_query = st.chat_input("Ask a query")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content = user_query))
        st.session_state.chat_history.append(AIMessage(content = response))
    for message in st.session_state.chat_history:
        if isinstance(message,AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message,HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
