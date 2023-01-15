import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import random

#File for developing ideas and functions to impliment into the main and final design

root = tk.Tk()
root.title("Yahtzee")

checkboxes = []
for i in range(5):
    var = tk.IntVar()
    checkbox = ttk.Checkbutton(root, variable=var)
    checkbox.grid(row=2, column=i)
    checkboxes.append(var)

def roll_dice():
    for i in range(5):
        if checkboxes[i].get() == 1:
            value = random.randint(1, 6)
            dice_labels[i].configure(image=dice_images[value - 1])

def score():
    # Add score calculation logic here
    pass

dice_images = []
for i in range(1, 6+1):
    image = Image.open(f"Dice{i}_resized.png")
    dice_images.append(ImageTk.PhotoImage(image))

dice_labels = []
for i in range(5):
    label = tk.Label(root, image=dice_images[0])
    label.grid(row=0, column=i)
    dice_labels.append(label)

roll_button = tk.Button(root, text="Roll", command=roll_dice)
roll_button.grid(row=1, column=0)

score_button = tk.Button(root, text="Score", command=score)
score_button.grid(row=1, column=1)



root.mainloop()
