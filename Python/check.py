from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")
root.geometry("400x400") #Define the gemoetry of the window



def value():
	myLabel=Label(root,text=var.get())
	myLabel.pack()


#declare the Tkinder variable
var = StringVar()

#Declare the Checkbox
c = Checkbutton(root,text="Check this checkbox!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()


btn=Button(root,text="Get the value",command=value)
btn.pack()
root.mainloop()