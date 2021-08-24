from tkinter import *
import beepy
import threading


def play_sound(selection):
    threading.Thread(target=lambda: (beepy.beep(selection))).start()
    print(selection)


if __name__ == '__main__':


    root = Tk()
    root.title("WHACK THAT GACK")
    root.geometry('200x500')

    lbl = Label(root, text = "Arses")
    lbl.grid()

    btn1 = Button(root, text = "Button 1", command=lambda:(play_sound(1)))
    btn1.grid()
    btn2 = Button(root, text = "Button 2", command=lambda:(play_sound(2)))
    btn2.grid()
    btn3 = Button(root, text = "Button 3", command=lambda:(play_sound(3)))
    btn3.grid()
    btn4 = Button(root, text = "Button 4", command=lambda:(play_sound(4)))
    btn4.grid()
    btn5 = Button(root, text = "Button 5", command=lambda:(play_sound(5)))
    btn5.grid()
    btn6 = Button(root, text = "Button 6", command=lambda:(play_sound(6)))
    btn6.grid()
    btn7 = Button(root, text = "Button 7", command=lambda:(play_sound(7)))
    btn7.grid()
    btn8 = Button(root, text = "Button 8", command=lambda:(play_sound(8)))
    btn8.grid()

    root.mainloop()

