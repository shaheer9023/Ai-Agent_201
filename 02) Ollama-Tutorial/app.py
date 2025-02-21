import ollama

Model = "llama3.2"  
messages = [
    {"role": "user", "content": "Describe AI"}
]

response = ollama.chat(model=Model, messages=messages)
print(response["message"]["content"])
