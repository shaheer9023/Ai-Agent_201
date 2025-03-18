import google.generativeai as genai
import PIL.Image
import tkinter as tk
from tkinter import filedialog
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API key
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

# Model load karo
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# 🎨 Tkinter window create karo
root = tk.Tk()
root.withdraw()  # Main window hide kar do

# 📂 User se image file select karne ka kehna
file_path = filedialog.askopenfilename(title="Select an Image",
                                filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

# 📸 Image load aur display karo
if file_path:
    print(f"Uploaded file: {file_path}")
    
    # 🖼 Image open karo
    img = PIL.Image.open(file_path)
    
    # 🔍 Image show karo (VS Code me ye kaam karega)
    img.show()
else:
    print("No file selected!")

prompt=input("Enter any prompt : ")
response=model.generate_content([prompt,img])
print(response.text)

