from tkinter import *
import beepy


if __name__ == '__main__':

def play_sound():
    beep(sound=1)


    root = Tk()
    root.title("WHACK THAT GACK")
    root.geometry('350x200')

    lbl = Label(root, text = "Arses")
    lbl.grid()

    btn = Button(root, text = "Click Me", fg = "red", command = play_sound())

    root.mainloop()

