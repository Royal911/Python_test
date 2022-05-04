from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")
root.geometry("400x400") #Define the gemoetry of the window




def slide():
	#mylabel=Label(root,text=horizontal.get()).pack()
	root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


#Define the horizontal slider
horizontal = Scale(root,from_=0,to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()

#Define the vertical slider

vertical = Scale(root,from_=0,to=200)
vertical.pack()




btn=Button(root,text="Click me", command=slide).pack()

root.mainloop()