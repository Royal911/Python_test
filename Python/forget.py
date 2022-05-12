from tkinter import *

root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")
root.geometry("400x400") 

def mydelete():
	#myLabel.pack_forget()
	myLabel.destroy()
	myButton['state'] = NORMAL
	delete_button['state'] = DISABLED

def myClick():
	global myLabel
	hello = "Hello " + e.get()
	myLabel = Label(root, text = hello)
	e.delete(0,'end')  #Delete what is in the box
	myLabel.pack(pady=10)
	myButton['state'] = DISABLED
	delete_button['state'] = NORMAL
 
e = Entry(root,width=50, font=(("Helvetica"),15)) #Increase the hight by increasing the font size
e.pack(padx=10,pady=10)

myButton = Button(root,text="Enter your Name", command=myClick)
myButton.pack(pady=10)


delete_button = Button(root,text="Delete text", command=mydelete)
delete_button.pack(pady=10)
delete_button['state'] = DISABLED


root.mainloop()