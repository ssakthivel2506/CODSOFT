import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}
        self.selected_contact = None 
        self.create_widgets()
    
    def create_widgets(self):
        
        tk.Label(self.root, text="Name:", foreground='black').grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.name_entry = tk.Entry(self.root, width=40)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        tk.Label(self.root, text="Phone:", foreground='black').grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.phone_entry = tk.Entry(self.root, width=40)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        add_button = tk.Button(button_frame, text="Add Contact", command=self.add_contact, bg='lightgreen', fg='black')
        add_button.grid(row=0, column=0, padx=5)
        
        edit_button = tk.Button(button_frame, text="Edit Contact", command=self.edit_contact, bg='lightblue', fg='black')
        edit_button.grid(row=0, column=1, padx=5)
        
        delete_button = tk.Button(button_frame, text="Delete Contact", command=self.delete_contact, bg='lightcoral', fg='black')
        delete_button.grid(row=0, column=2, padx=5)

        
        self.contact_listbox = tk.Listbox(self.root, width=60, height=15, bg='white', fg='black')
        self.contact_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.contact_listbox.bind("<<ListboxSelect>>", self.on_select_contact)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        if not name or not phone:
            messagebox.showwarning("Input Error", "Both name and phone are required!")
            return
        if name in self.contacts:
            messagebox.showwarning("Duplicate Contact", "Contact already exists!")
            return
        self.contacts[name] = phone
        self.update_contact_listbox()
        self.clear_entries()
        messagebox.showinfo("Success", "Contact added successfully!")

    def edit_contact(self):
        if self.selected_contact is None:
            messagebox.showwarning("Selection Error", "No contact selected!")
            return
        
        new_name = self.name_entry.get().strip()
        new_phone = self.phone_entry.get().strip()
        
        if not new_name or not new_phone:
            messagebox.showwarning("Input Error", "Both name and phone are required to update the contact!")
            return
        
        
        if new_name != self.selected_contact and new_name in self.contacts:
            messagebox.showwarning("Duplicate Contact", "A contact with this name already exists!")
            return
        
        
        del self.contacts[self.selected_contact]  
        self.contacts[new_name] = new_phone  
        
        self.update_contact_listbox()
        self.clear_entries()
        self.selected_contact = None
        messagebox.showinfo("Success", "Contact updated successfully!")
    
    def delete_contact(self):
        selected = self.contact_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No contact selected!")
            return
        name = self.contact_listbox.get(selected[0])
        del self.contacts[name]
        self.update_contact_listbox()
        self.clear_entries()
        self.selected_contact = None
        messagebox.showinfo("Success", "Contact deleted successfully!")

    def on_select_contact(self, event):
        selected = self.contact_listbox.curselection()
        if selected:
            self.selected_contact = self.contact_listbox.get(selected[0])  
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, self.selected_contact)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, self.contacts[self.selected_contact])
    
    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for name in self.contacts:
            self.contact_listbox.insert(tk.END, name)
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

root = tk.Tk()
app = ContactBook(root)
root.mainloop()
