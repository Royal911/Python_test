from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")


my_img=ImageTk.PhotoImage(Image.open("images/funny.jpg"))
my_label=Label(image=my_img)
my_label.pack()








button_quit = Button(text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()