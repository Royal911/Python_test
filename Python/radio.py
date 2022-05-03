from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")

#Define a variable as int
#r = IntVar()
#r.set("2")

#Define a variab;le as String

pizza=StringVar()
pizza.set("Peperony")



#Create a list
TOPPINGS = [
	("Peperony","Peperony"),
	("Cheeze","Cheeze"),
	("Mushrooms","Mushrooms"),
	("Onions","Onions"),
]

for text,toppings in TOPPINGS:
	Radiobutton(root,text=text, variable=pizza, value=toppings).pack(anchor=W)




def clicked(value):

	myLabel=Label(root,text=value)
	myLabel.pack()


#Define the radio buttons and pack them up without a loop
#Radiobutton(root,text="Option 1", variable=r , value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option 2", variable=r , value=2, command=lambda: clicked(r.get())).pack()

#Define the radio buttons with a loop 

myButton=Button(root,text="Click me!",command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()