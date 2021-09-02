import tkinter
import turtle
import time
from tkinter import *


def turtleButton():
    root = Tk()
    root.title("turtleButton")
    root.geometry('300x300')

    forward = Button(root, text="forward",command=lambda:print("poop"))

    canvas = Canvas(root, width=400, height=300)
    canvas.pack()

    screen1 = turtle.TurtleScreen(canvas)

    p = turtle.RawTurtle(screen1)

    p.forward(10)