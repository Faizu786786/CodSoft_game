import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to play the game
def play(choice):
    global user_score, computer_score

    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    result = ""
    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update labels
    user_choice_label.config(text=f"Your Choice: {choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="Result: ")
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

# Create main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")

# Labels for choices and result
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack(pady=5)
computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12))
computer_choice_label.pack(pady=5)
result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text=f"Score - You: {user_score}  Computer: {computer_score}", font=("Arial", 12))
score_label.pack(pady=5)

# Buttons for user choices
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Reset Button
reset_button = tk.Button(root, text="Reset Game", command=reset_game, bg="red", fg="white")
reset_button.pack(pady=10)

# Run the application
root.mainloop()
