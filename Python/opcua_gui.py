from tkinter import *
import asyncio
from asyncua import Client, Node, ua

root = Tk()
root.title('OPC UA read')
root.iconbitmap("images/test.ico")
root.geometry("400x400")


async def main():
    url = "opc.tcp://UMTM14CUJ2501:4840"
    async with Client(url=url) as client:
        var = client.get_node("ns=4;s=DOPAC.CU_INF_RedLamp_L")
        global value
        value = (var, await var.read_value())

def clin():
	asyncio.run(main())
	global myLabel
	myLabel=Label(root)
	myLabel.grid_forget()
	myLabel = Label(root, text =value[1])
	myLabel.grid(row=0,column=0, pady=20,padx=20)


myButton = Button(root,text="Click me ", command=clin)
myButton.grid(row=0,column=1, pady=20,padx=20)



root.mainloop()