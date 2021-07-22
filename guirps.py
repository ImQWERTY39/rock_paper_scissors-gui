import tkinter as tk
from tkinter import messagebox
from random import choice


window = tk.Tk()
window.title("Stone, Paper, Scissors")
window.geometry("350x150")

this = ("stone", "paper", "scissors")
wincount = 0
losecount = 0
drawcount = 0


def Stone(wincount, losecount, drawcount):
    computerChoise = choice(this)

    if computerChoise == "stone":
        user_message.config(text = f"Draw. You chose stone and computer chose {computerChoise}")
        drawcount += 1
        drawcount_label.config(text = drawcount)

    if computerChoise == "paper":
        user_message.config(text = f"You lost. You chose stone and computer chose {computerChoise}")
        losecount += 1
        losecount_label.config(text = losecount)

    if computerChoise == "scissors":
        user_message.config(text = f"You won. You chose stone and computer chose {computerChoise}")
        wincount += 1
        wincount_label.config(text = wincount)
    

def Paper(wincount, losecount, drawcount):
    computerChoise = choice(this)

    if computerChoise == "paper":
        user_message.config(text = f"Draw. You chose paper and computer chose {computerChoise}")
        drawcount += 1
        drawcount_label.config(text = drawcount)

    if computerChoise == "scissors":
        user_message.config(text = f"You lost. You chose paper and computer chose {computerChoise}")
        losecount += 1
        losecount_label.config(text = losecount)

    if computerChoise == "stone":
        user_message.config(text = f"You won. You chose paper and computer chose {computerChoise}")
        wincount += 1
        wincount_label.config(text = wincount)


def Scissors(wincount, losecount, drawcount):
    computerChoise = choice(this)   

    if computerChoise == "scissors":
        user_message.config(text = f"Draw. You chose scissors and computer chose {computerChoise}")
        drawcount += 1
        drawcount_label.config(text = drawcount) 

    if computerChoise == "stone":
        user_message.config(text = f"You lost. You chose scissors and computer chose {computerChoise}")
        losecount += 1
        losecount_label.config(text = losecount)

    if computerChoise == "paper":
        user_message.config(text = f"You won. You chose scissors and computer chose {computerChoise}")
        wincount += 1
        wincount_label.config(text = wincount)


def QuitGame():
    response = messagebox.askyesno("Quit game", "Are you sure you want to quit?")
    if response == 1:
        window.destroy()

user_message = tk.Label(window, text = "")
user_message.place(x = 0, y = 65)

label = tk.Label(window, text = "Stone, Paper, Or Scissors?")
label.place(x = 0, y = 0)

win_label = tk.Label(window, text = "Wins")
win_label.place(x = 175, y = 0)
wincount_label = tk.Label(window, text = "")
wincount_label.place(x = 175, y = 15)

lose_label = tk.Label(window, text = "Loses")
lose_label.place(x = 225, y = 0)
losecount_label = tk.Label(window, text = "")
losecount_label.place(x = 225, y = 15)

draw_label = tk.Label(window, text = "Draws")
draw_label.place(x = 275, y = 0)
drawcount_label = tk.Label(window, text = "")
drawcount_label.place(x = 275, y = 15)  

stone_button = tk.Button(window, text = "Stone", command= lambda: Stone(wincount, losecount, drawcount)).place(x = 0, y = 25)
paper_button = tk.Button(window, text = "Paper", command= lambda: Paper(wincount, losecount, drawcount)).place(x = 50, y = 25)
scissors_button = tk.Button(window, text = "Scissors", command= lambda: Scissors(wincount, losecount, drawcount)).place(x = 100, y = 25)

quit_button = tk.Button(window, text = "Quit", command = QuitGame)
quit_button.place(x = 50, y = 100)

window.mainloop()