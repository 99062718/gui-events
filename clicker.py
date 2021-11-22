import tkinter
from typing import Text
number = 0

def windowChange(self):
    textLabel.configure(text=number)
    if number > 0:
        mainWindow.configure(bg="green")
    elif number < 0:
        mainWindow.configure(bg="red")
    else:
        mainWindow.configure(bg="grey")

def makeYellow(self):
    mainWindow.configure(bg="yellow")

def numUp():
    global number
    number += 1
    windowChange("")

def numDown():
    global number
    number -= 1
    windowChange("")

mainWindow = tkinter.Tk()
mainWindow.configure(
    padx=10,
    bg="grey"
)

upButton = tkinter.Button(mainWindow)
upButton.configure(
    bg="white",
    text="up",
    fg="black",
    command=numUp
)
upButton.pack(pady=10, fill="x")

textLabel = tkinter.Label(mainWindow)
textLabel.configure(
    bg="white",
    text=number,
    fg="black",
    justify="center"
)
textLabel.pack(pady=10, fill="x")
textLabel.bind("<Enter>", makeYellow)
textLabel.bind("<Leave>", windowChange)

downButton = tkinter.Button(mainWindow)
downButton.configure(
    bg="white",
    text="down",
    fg="black",
    command=numDown
)
downButton.pack(pady=10, fill="x")

mainWindow.mainloop()