from tkinter import *
from random import randint
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Rock Paper Scissors")
root.iconphoto(False, PhotoImage(file="assets/rock_paper_scissors.png"))
root.resizable(False, False)


options = [
    "Rock",
    "Paper",
    "Scissors"
]

clicked = StringVar()
clicked.set(options[0])


def play():
    choice = clicked.get()
    num = randint(0, 2)  # 0-Rock; 1-Paper; 2-Scissors
    computer = options[num]
    if choice == computer:
        messagebox.showinfo("Tie!", "The computer played " + computer + " and you played " + choice + "!")
    elif choice == "Rock" and computer == "Paper":
        messagebox.showinfo("You lost!", "The computer played " + computer + " and you played " + choice + "!")
    elif choice == "Rock" and computer == "Scissors":
        messagebox.showinfo("You won!", "The computer played " + computer + " and you played " + choice + "!")
    elif choice == "Paper" and computer == "Rock":
        messagebox.showinfo("You won!", "The computer played " + computer + " and you played " + choice + "!")
    elif choice == "Paper" and computer == "Scissors":
        messagebox.showinfo("You lost!", "The computer played " + computer + " and you played " + choice + "!")
    elif choice == "Scissors" and computer == "Rock":
        messagebox.showinfo("You lost!", "The computer played " + computer + " and you played " + choice + "!")
    elif choice == "Scissors" and computer == "Paper":
        messagebox.showinfo("You won!", "The computer played " + computer + " and you played " + choice + "!")


l1 = Label(root, text="Your choice:")
l1.grid(row=0, column=0, padx=15)

menu = OptionMenu(root, clicked, *options)
menu.grid(row=0, column=1)

play = Button(root, width=5, text="Play", command=play)
play.grid(row=1, column=0, columnspan=2)

my_img = ImageTk.PhotoImage(Image.open("assets/rock_paper_scissors_resized.png"))
my_label = Label(root, image=my_img)
my_label.grid(row=0, column=2, rowspan=2)


root.mainloop()
