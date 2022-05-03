from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")


#This are the different kind of pop up messages : showinfo , showwarning,showerror, askquestion, askokcancel,askyesno

def popup():
	response = messagebox.askquestion("This is my popup","Hello world!")
	if response == 'yes':
		label=Label(root,text="Your response was Yes").pack()
	else:	
		label=Label(root,text="Your response was No").pack()



button=Button(root,text="Pop up", command=popup).pack()


root.mainloop()