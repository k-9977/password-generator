import tkinter as tk
import random
import string


root = tk.Tk()
root.title("Password Generator")
root.geometry("550x450")

title_label = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)

length_label = tk.Label(
    root,
    text="Password Length:"
)
length_label.pack(pady=(10, 5))

length_entry = tk.Entry(root)
length_entry.pack(pady=5)


def generate_password():
    length = int(length_entry.get())

    letters = string.ascii_letters+string.digits+string.punctuation

    password = ""

    for i in range(length):
        random_letter = random.choice(letters)
        password += random_letter
    password_label.config(text=password)


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_label["text"])


generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password

)
generate_button.pack(pady=10)

password_label = tk.Label(
    root,
    text="Your password will appear here.",
    font=("Consolas", 14, "bold"),
    fg="blue",
    wraplength=450
)

password_label.pack(pady=15)

copy_button = tk.Button(
    root,
    text="📋 Copy Password",
    command=copy_password
)
copy_button.pack(pady=10)


root.mainloop()
