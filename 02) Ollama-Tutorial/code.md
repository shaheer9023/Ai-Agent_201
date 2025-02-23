# **Step-by-Step Explanation of the Code**  

---

### **1️⃣ `ollama` Library Import Karna**  
```python
import ollama
```
✅ **Kya Ho Raha Hai?**  
- Yeh line `ollama` library ko import kar rahi hai jo AI models ke sath interact karne ke liye use hoti hai.  
- `ollama` ka use hum **chat-based AI responses** generate karne ke liye kar rahe hain.  

📌 **Agar `ollama` install nahi hai to install karne ke liye:**  
```sh
pip install ollama
```
---

### **2️⃣ User Se Input Lena**  
```python
prompt = input("enter your prompt : ")
```
✅ **Kya Ho Raha Hai?**  
- `input()` function user se **text input** leta hai.  
- `"enter your prompt : "` ek **message** hai jo user ko input dene se pehle show hota hai.  
- Jo bhi user likhta hai, woh `prompt` variable me store ho jata hai.  

📌 **Example:**  
Agar user likhta hai:  
```
Hello AI! How are you?
```
To `prompt` variable me store hoga:
```python
prompt = "Hello AI! How are you?"
```
---

### **3️⃣ AI Model Ka Naam Set Karna**  
```python
Model = "llama3.2"
```
✅ **Kya Ho Raha Hai?**  
- Yeh line ek **variable** `Model` create kar rahi hai jo AI model ka naam store karta hai.  
- `"llama3.2"` ek AI model hai jo hum **chat ke liye use** kar rahe hain.  

📌 **Agar aap doosra model use karna chahein to yeh change kar sakte hain:**  
```python
Model = "mistral"
```
---

### **4️⃣ Messages Ki List Create Karna**  
```python
messages = [
    {"role": "user",
     "content": prompt}
]
```
✅ **Kya Ho Raha Hai?**  
- Yeh ek **list** hai jo AI ke sath **conversation format** set karti hai.  
- Is list me ek **dictionary `{}`** hai jo batati hai ke yeh message kis role ka hai aur iska content kya hai.  
- `"role": "user"` → Yeh batata hai ke yeh **user ka message** hai.  
- `"content": prompt` → Yeh **user ka likha hua message** store karta hai.  

📌 **Example:**  
Agar user `Hello AI!` likhe to `messages` me yeh data store hoga:
```python
messages = [
    {"role": "user",
     "content": "Hello AI!"}
]
```
---

### **5️⃣ AI Se Response Lena**  
```python
response = ollama.chat(model=Model, messages=messages)
```
✅ **Kya Ho Raha Hai?**  
- `ollama.chat()` function AI ko **message bhejta hai** aur **uska jawab** leta hai.  
- `model=Model` → Yeh batata hai ke kaunsa **AI model** use ho raha hai (`llama3.2`).  
- `messages=messages` → Yeh **user ka message AI ko bhejta hai**.  
- `response` ek **dictionary** hoti hai jo AI ka jawab store karti hai.  

📌 **Example AI Response:**  
Agar AI ka jawab kuch aisa aaye:
```json
{
    "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
    }
}
```
---

### **6️⃣ AI Ka Response Print Karna**  
```python
print(response["message"]["content"])
```
✅ **Kya Ho Raha Hai?**  
- `response["message"]` → AI ke response ka `"message"` part access karta hai.  
- `response["message"]["content"]` → `"message"` ke andar `"content"` ko access karta hai jo AI ka **actual jawab** hota hai.  
- `print()` function AI ka jawab **screen par show** kar deta hai.  

📌 **Agar AI ka response yeh ho:**  
```json
{
    "message": {
        "role": "assistant",
        "content": "The capital of France is Paris."
    }
}
```
To **screen par output hoga:**  
```
The capital of France is Paris.
```
