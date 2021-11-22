import tkinter
number = 0
lastPressed = None

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

def doubleClick(self):
    global number
    if lastPressed == "up":
        number *= 3
    elif lastPressed == "down":
        number /= 3
    windowChange("")

def numUp():
    global number
    global lastPressed
    number += 1
    lastPressed = "up"
    windowChange("")

def numDown():
    global number
    global lastPressed
    number -= 1
    lastPressed = "down"
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
textLabel.bind("<Double-Button-1>", doubleClick)

downButton = tkinter.Button(mainWindow)
downButton.configure(
    bg="white",
    text="down",
    fg="black",
    command=numDown
)
downButton.pack(pady=10, fill="x")

mainWindow.mainloop()