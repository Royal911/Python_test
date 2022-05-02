from tkinter import *

root = Tk()

#Define a imput entry
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0,"Here type your name")

# Define a function for the click

def myClick():
	hello ="Hello " + e.get()
	myLabel = Label(root,text=hello)
	myLabel.pack()


myButton = Button(root,text="Enter your name", command=myClick, fg="blue", bg="yellow")
myButton.pack()

# Create the loop
root.mainloop()