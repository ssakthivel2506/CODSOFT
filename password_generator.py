import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length=7, use_uppercase=True, use_lowercase=True, use_numbers=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    
    if not characters: 
        characters = string.ascii_uppercase 
    
    return ''.join(random.choice(characters) for _ in range(length))

def show_password():
    global generated_password
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    generated_password = generate_password(length=7, use_uppercase=use_uppercase, use_lowercase=use_lowercase, use_numbers=use_numbers)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

def confirm_password():
    user_input = guess_entry.get()
    if user_input == generated_password:
        messagebox.showinfo("Success", "Password matches!")
    else:
        messagebox.showerror("Error", "Password does not match.")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.configure(bg="lightblue")  


generated_password = ""


options_frame = tk.Frame(root, bg="lightblue")  
options_frame.pack(pady=10)

uppercase_var = tk.BooleanVar(value=True)
uppercase_checkbox = tk.Checkbutton(options_frame, text="Include Uppercase Letters", variable=uppercase_var, bg="lightblue")
uppercase_checkbox.pack(anchor="w")

lowercase_var = tk.BooleanVar(value=True)
lowercase_checkbox = tk.Checkbutton(options_frame, text="Include Lowercase Letters", variable=lowercase_var, bg="lightblue")
lowercase_checkbox.pack(anchor="w")

numbers_var = tk.BooleanVar(value=True)
numbers_checkbox = tk.Checkbutton(options_frame, text="Include Numbers", variable=numbers_var, bg="lightblue")
numbers_checkbox.pack(anchor="w")


password_label = tk.Label(root, text="Generated Password:", bg="lightblue")
password_label.pack(pady=10)

password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=show_password, bg="navy", fg="white", activebackground="blue", activeforeground="white")
generate_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_password, bg="navy", fg="white", activebackground="blue", activeforeground="white")
copy_button.pack(pady=10)


guess_label = tk.Label(root, text="Enter Password to Confirm:", bg="lightblue")
guess_label.pack(pady=10)

guess_entry = tk.Entry(root, width=50)
guess_entry.pack(pady=5)

confirm_button = tk.Button(root, text="Confirm Password", command=confirm_password, bg="lightgreen", fg="black", activebackground="lightgreen", activeforeground="white")
confirm_button.pack(pady=10)

root.mainloop()
