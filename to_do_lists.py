import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")


def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")


def remove_task(event):
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")


def delete_all_tasks():
    confirm = messagebox.askyesno("Delete All", "Are you sure you want to delete all tasks?")
    if confirm:
        task_listbox.delete(0, tk.END)


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")


task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)


add_task_button = tk.Button(root, text="Add Task", bg="#4caf50", command=add_task)
add_task_button.pack(pady=5)


delete_task_button = tk.Button(root, text="Delete Task", bg="#ADD8E6", command=delete_task)
delete_task_button.pack(pady=5)


delete_all_button = tk.Button(root, text="Delete All Tasks",bg="#DEF4FC", command=delete_all_tasks)
delete_all_button.pack(pady=5)


task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)


task_listbox.bind("<Double-Button-1>", remove_task)


root.mainloop()
