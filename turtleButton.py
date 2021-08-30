import turtle
import tkinter as tk


def do_stuff():
    for color in ["red", "yellow", "green"]:
        my_lovely_turtle.color(color)
        my_lovely_turtle.right(120)


def press():
    do_stuff()


def turtleButton():
    screen = turtle.Screen()
    screen.bgcolor("cyan")
    canvas = screen.getcanvas()
    button = tk.Button(canvas.master, text="Press me", command=press)
    canvas.create_window(-200, -200, window=button)
    my_lovely_turtle = turtle.Turtle(shape="turtle")
    turtle.done()