from tkinter import *
from PIL import ImageTk,Image
import requests  #Import the requests - in order to get from web
import json  #Import json objects


root = Tk()
root.title('Learn to code')
root.iconbitmap("C:/Users/plantadmin_HS_CM/test/Python/images/test.ico")
root.geometry("230x20")
root.configure(background="green") #Configure the background


#API Link :  https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=29154&distance=10&API_KEY=2DCAE2B4-33C9-4B6F-8B1C-DD07298C8DFE


#Error handle - try to get the info and post the content . If error...show Error...
try:
	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=29154&distance=10&API_KEY=2DCAE2B4-33C9-4B6F-8B1C-DD07298C8DFE")
	api = json.loads(api_request.content)
	city = api[0]["ReportingArea"]
	quality = api[0]["AQI"]
	category = api[0]["Category"]["Name"]
except Exception as e:
	api = "Error..."

#Create a label to show the api

myLabel = Label(root, text = city + " Air Quality : " + str(quality) + " " + category, font=("Helvetica",0), background="green")
myLabel.pack()


root.mainloop()