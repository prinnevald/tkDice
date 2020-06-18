from tkinter import *
from tkinter import ttk
import random

# these are the functions which will be drawing according dice
# sides from 1 through 6.

def draw1(canvas):
    canvas.create_oval(90, 90, 120, 120, fill="black")

def draw2(canvas):
    canvas.create_oval(50, 50, 70, 70, fill="black")
    canvas.create_oval(130, 130, 150, 150, fill="black")

def draw3(canvas):
    canvas.create_oval(50, 50, 70, 70, fill="black")
    canvas.create_oval(130, 130, 150, 150, fill="black")
    canvas.create_oval(90, 90, 120, 120, fill="black")

def draw4(canvas):
    canvas.create_oval(50, 50, 70, 70, fill="black")
    canvas.create_oval(130, 130, 150, 150, fill="black")
    canvas.create_oval(130, 50, 150, 70, fill="black")
    canvas.create_oval(50, 130, 70, 150, fill="black")

def draw5(canvas):
    canvas.create_oval(50, 50, 70, 70, fill="black")
    canvas.create_oval(130, 130, 150, 150, fill="black")
    canvas.create_oval(130, 50, 150, 70, fill="black")
    canvas.create_oval(50, 130, 70, 150, fill="black")
    canvas.create_oval(90, 90, 120, 120, fill="black")

def draw6(canvas):
    canvas.create_oval(50, 50, 70, 70, fill="black")
    canvas.create_oval(130, 130, 150, 150, fill="black")
    canvas.create_oval(130, 50, 150, 70, fill="black")
    canvas.create_oval(50, 130, 70, 150, fill="black")
    canvas.create_oval(50, 90, 70, 110, fill="black")
    canvas.create_oval(130, 90, 150, 110, fill="black")

# list of drawing functions to get a function from randomly

drawList=(draw1, draw2, draw3, draw4, draw5, draw6)

def main():
    window = Tk()
    window.title("tkDice")
    
    canvas = Canvas()
    canvas.create_rectangle(10, 10, 210, 210, fill="white")
    random.choice(drawList)(canvas)
    canvas.pack(fill=BOTH, expand=0)

    def roll():
        canvas.delete("all")
        canvas.create_rectangle(10, 10, 210, 210, fill="white")
        random.choice(drawList)(canvas)

    button = Button(window, text="Reroll", command = roll)
    button.pack(fill=BOTH, expand=0)
    
    window.geometry("220x300")
    window.resizable(width=False, height=False)
    window.mainloop()

if __name__ == "__main__":
    main()