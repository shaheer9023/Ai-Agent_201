from langchain_google_genai import ChatGoogleGenerativeAI
import os
llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp" , api_key=os.getenv("KEY"))
prompt=input("enter your prompt : ")
response=llm.invoke(prompt)
print(response.content)