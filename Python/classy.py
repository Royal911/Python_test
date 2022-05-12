from tkinter import *



root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")
root.geometry("400x400")


class Dan:
	def __init__(self, master):
		myFrame = Frame(master)
		myFrame.pack()

		self.myButton = Button(master, text="click me!", command=self.clicker)
		self.myButton.pack(pady=20)
	def clicker(self):
		print("You click a button")	

e = Dan(root)


root.mainloop()