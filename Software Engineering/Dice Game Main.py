import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

#Current mainframe for the final design of the Dice Game

root = tk.Tk()
root.geometry("700x300")
root.title("Dice Game")
mainframe = tk.Frame(root, background="white")
mainframe.pack(fill="both", expand=True)
img = Image.open("Software Engineering\Images\Dice.png")
photo = ImageTk.PhotoImage(img)
root.iconphoto(True, photo)

text = tk.Label(mainframe, text="Totally Original Dice Game", background=("white"), font=("Brass Mono", 30), foreground=("dark orange"))
text.pack()

dice_frame = tk.Frame(mainframe, borderwidth=5, background=("red"))

root.mainloop()

def roll_dice():
    return random.randint(1,6)