from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")

#Define the function that open the second windows with a close button

def open():
	global my_img
	top = Toplevel()
	top.title('Second window')
	top.iconbitmap("images/test.ico")	
	my_img=ImageTk.PhotoImage(Image.open("images/funny.jpg"))
	my_label=Label(top,image=my_img).pack()
	btn2=Button(top,text="Close window",command=top.destroy).pack()

btn=Button(root,text="Open Second window", command=open)
btn.pack()


root.mainloop()