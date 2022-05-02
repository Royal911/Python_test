from tkinter import *

root = Tk()

# Define a function for the click

def myClick():
	myLabel = Label(root,text="Look I clicked", fg="red")
	myLabel.pack()


myButton = Button(root,text="Click me!", command=myClick, fg="blue", bg="yellow")
myButton.pack()

# Create the loop
root.mainloop()