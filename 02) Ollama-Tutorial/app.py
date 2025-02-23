import ollama
prompt=input("enter your prompt : ")
Model = "llama3.2"
messages = [
    {"role": "user",
     "content": prompt}
]

response = ollama.chat(model=Model, messages=messages)
print(response["message"]["content"])
