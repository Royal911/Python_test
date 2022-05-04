from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")
root.geometry("400x400") #Define the gemoetry of the window

def show():
	myLabel=Label(root,text=clicked.get())
	myLabel.pack()


#Use a list
options = [
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
		"Saturday"
]

clicked = StringVar()
clicked.set(options[0])

#Define the dropbox menu

drop = OptionMenu(root,clicked,*options)
drop.pack()


mybtn=Button(root,text="Show Selection!", command=show)
mybtn.pack()


root.mainloop()