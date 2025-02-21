from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp" , api_key=os.getenv("key"))
prompt=st.chat_input("enter your prompt : ")
response=llm.invoke(prompt)
st.write(response.content)