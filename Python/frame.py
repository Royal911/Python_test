from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")

frame_left = LabelFrame(root,text="Buttons",padx=50,pady=50)
frame_left.grid(row=0,column=0,padx=10,pady=10)
frame_right = LabelFrame(root,text="Inputs",padx=50,pady=50)
frame_right.grid(row=0,column=1,padx=20,pady=20)


b = Button(frame_left,text="Don't click me!!")
b.grid(row=0,column=0)

b1 = Button(frame_left,text="Here you can click!!")
b1.grid(row=1,column=0)

e = Entry(frame_right,width=10,bd=1)
e.grid(row=0,column=0,)

e1 = Entry(frame_right,width=10,bd=1)
e1.grid(row=1,column=0,pady=8)

root.mainloop()