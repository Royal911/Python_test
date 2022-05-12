from tkinter import *

root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")
root.geometry("400x400") 

def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text = hello)
	e.delete(0,'end')  #Delete what is in the box
	myLabel.pack(pady=10)
 
e = Entry(root,width=50, font=(("Helvetica"),15)) #Increase the hight by increasing the font size
e.pack(padx=10,pady=10)

mybutton = Button(root,text="Enter your Name", command=myClick)
mybutton.pack(pady=10)

root.mainloop()