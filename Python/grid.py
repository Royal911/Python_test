from tkinter import *

root = Tk()
# Create a label
myLabel1 = Label(root, text="Hello world")
myLabel2 = Label(root, text="My name is Dan")
# Put it on the screen as grid
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
# Create the loop
root.mainloop()