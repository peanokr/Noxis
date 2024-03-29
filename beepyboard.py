from tkinter import *
import beepy
import threading

def play_sound(selection):
    threading.Thread(target=lambda: (beepy.beep(selection))).start()
    print(selection)

def beepyBoard():
    root = Tk()
    root.title("Beepy Board")
    root.geometry('200x250')

    lbl = Label(root, text="Arses")
    lbl.grid()

    btn1 = Button(root, text="Coin", command=lambda: (play_sound(1)))
    btn1.grid()
    btn2 = Button(root, text="DNC", command=lambda: (play_sound(2)))
    btn2.grid()
    btn3 = Button(root, text="Error", command=lambda: (play_sound(3)))
    btn3.grid()
    btn4 = Button(root, text="Bell", command=lambda: (play_sound(4)))
    btn4.grid()
    btn5 = Button(root, text="Flourish", command=lambda: (play_sound(5)))
    btn5.grid()
    btn6 = Button(root, text="Pomp", command=lambda: (play_sound(6)))
    btn6.grid()
    btn7 = Button(root, text="Scream", command=lambda: (play_sound(7)))
    btn7.grid()
