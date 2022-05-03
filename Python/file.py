from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog #Impor the file dialog 

root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")

def openfile():
	global my_img
	root.filename = filedialog.askopenfilename(initialdir="images",title="Select file name",filetypes=(("Jpeg File","*.jpg"),("All files","*")))
	#my_label=Label(root,text=root.filename).pack()
	my_img=ImageTk.PhotoImage(Image.open(root.filename))
	my_label1=Label(image=my_img)
	my_label1.pack()

mybtn=Button(root,text="Open file",command=openfile).pack()


root.mainloop()