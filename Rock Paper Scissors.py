import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():

    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}")
    result_message_label.config(text=result)


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.configure(bg="#ADD8E6") 


button_frame = tk.Frame(root, bg="#D3D3D3")  
button_frame.pack(pady=20)


result_frame = tk.Frame(root, bg="#F08080") 
result_frame.pack(pady=10)


title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20), bg="#ADD8E6", fg="#00008B")
title_label.pack(pady=35)

rock_button = tk.Button(button_frame, text="Rock", width=10, height=2, command=lambda: play_game("Rock"), bg="#4e342e", fg="white", activebackground="#4169E1", activeforeground="white")
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, height=2, command=lambda: play_game("Paper"), bg="#ffffff", fg="black", activebackground="#4169E1", activeforeground="white")
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, height=2, command=lambda: play_game("Scissors"), bg="#800000", fg="white", activebackground="#4169E1", activeforeground="white")
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(result_frame, text="Make a choice!", font=("Arial", 14), bg="#F08080", fg="white")
result_label.pack()

result_message_label = tk.Label(result_frame, text="", font=("Arial", 14), bg="#F08080", fg="white")
result_message_label.pack()


root.mainloop()
