import openai
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import scrolledtext

# Set your OpenAI API key
openai.api_key = 'Your api key'#detail togenerate api key in read.me file

# Function to get response from OpenAI:
def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a personal assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

# Function to handle the sending of a message:
def send_message():
    user = user_entry.get()
    if user.strip():
        chat_display.insert(tk.END, f"You: {user}\n")
        user_entry.delete(0, tk.END)

        response = get_response(user)
        chat_display.insert(tk.END, f"ChatGPT: {response}\n")
        chat_display.yview(tk.END)

#  Main rootlication window:
root = tk.Tk()
root.title("ChatGPT with Tkinter")
root.geometry("500x500")

# Load the background image
background_image = Image.open("C:/internship task/chatbot/background.jpg") 
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas and place the background image
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Chat display area
chat_display = scrolledtext.ScrolledText(root, bg="#ADB8D6",wrap=tk.WORD)
chat_display.place(x=450,y=300)

# User input area
user_entry = tk.Entry(root, width=60,bg="#ADB8D6")
user_entry.place(x=620,y=700)

# Send button
send_button = tk.Button(root, text="Send", command=send_message,bg="#433B52",fg="#ffffff")
send_button.place(x=750, y=740, width=100)

# Start the Tkinter  loop
root.mainloop()