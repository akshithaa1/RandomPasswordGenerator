import secrets
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = (
        secrets.choice(string.ascii_lowercase) +
        secrets.choice(string.ascii_uppercase) +
        secrets.choice(string.digits) +
        secrets.choice(string.punctuation)
    )
    password += ''.join(secrets.choice(characters) for _ in range(length - 4))
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    return ''.join(password_list)

def generate_password_button_click():
    try:
        length = int(password_length_entry.get())
        if length < 8:
            messagebox.showerror("Invalid Length", "Password length should be at least 8 characters.")
        else:
            password = generate_password(length)
            result_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for the password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and configure GUI elements
password_length_label = tk.Label(root, text="Enter the desired password length:")
password_length_label.pack(pady=10)

password_length_entry = tk.Entry(root)
password_length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_button_click)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
