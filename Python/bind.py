from tkinter import *

root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")
root.geometry("400x400")

def clicker(event):

	myLabel= Label(root,text="You clicked a button : " + event.char)
	myLabel.pack()


myButton = Button(root,text="Click me ")
myButton.bind("<Key>", clicker)
myButton.pack(pady=20)



root.mainloop()