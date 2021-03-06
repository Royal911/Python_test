from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")
root.geometry("400x200") #Define the gemoetry of the window

def graph():
	house_prices = np.random.normal(200000, 25000, 5000)
	plt.hist(house_prices,50)
	plt.show()

my_button=Button(root,text="Graph it !", command=graph)
my_button.pack()

root.mainloop()