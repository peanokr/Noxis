from tkinter import *

from beepyboard import *
from turtleButton import *

if __name__ == '__main__':


    root = Tk()
    root.title("Main")
    root.geometry('200x250')

    lbl = Label(root, text = "Arses")
    lbl.grid()

    btn1 = Button(root, text = "BeepyBoard", command=lambda:(beepyBoard()))
    btn1.grid()
    btn2 = Button(root, text = "TurtleButton", command=lambda:(turtleButton()))
    btn2.grid()

    root.mainloop()

