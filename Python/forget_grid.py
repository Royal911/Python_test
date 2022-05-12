from tkinter import *

root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")
root.geometry("400x400") 

#myLabel=Label(root)

'''
def mydelete():
	myLabel.grid_forget()
	#myLabel.destroy()
	myButton['state'] = NORMAL
	#delete_button['state'] = DISABLED
'''
def myClick():
	global myLabel
	myLabel=Label(root)
	myLabel.destroy()
	hello = "Hello " + e.get()
	myLabel = Label(root, text = hello)
	e.delete(0,'end')  #Delete what is in the box
	myLabel.grid(row=3,column=0,pady=10)
	#myButton['state'] = DISABLED
	#delete_button['state'] = NORMAL
 
e = Entry(root,width=30, font=(("Helvetica"),15)) #Increase the hight by increasing the font size
e.grid(row=0,column=0,padx=10,pady=10)

myButton = Button(root,text="Enter your Name", command=myClick)
myButton.grid(row=1,column=0,pady=10)

'''
delete_button = Button(root,text="Delete text", command=mydelete)
delete_button.grid(row=2,column=0,pady=10)
delete_button['state'] = DISABLED
'''

root.mainloop()