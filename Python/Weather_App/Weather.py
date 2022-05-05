from tkinter import *
from PIL import ImageTk,Image
import requests  #Import the requests - in order to get from web
import json  #Import json objects


root = Tk()
root.title('Learn to code')
root.iconbitmap("C:/Users/plantadmin_HS_CM/test/Python/images/test.ico")
root.geometry("430x200")



#API Link :  https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=29154&distance=10&API_KEY=2DCAE2B4-33C9-4B6F-8B1C-DD07298C8DFE


#Define the zipLookup function for the Look Up button
def zipLookup():
	#zip.get()
	#zip_label=Label(root,text=zip.get())
	#zip_label.grid(row=1,column=0, columnspan=2)

	#Error handle - try to get the info and post the content . If error...show Error...
	try:
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=10&API_KEY=2DCAE2B4-33C9-4B6F-8B1C-DD07298C8DFE")
		api = json.loads(api_request.content)
		city = api[0]["ReportingArea"]
		quality = api[0]["AQI"]
		category = api[0]["Category"]["Name"]

		#Create a if statement to check for the Category name
		if category == "Good":
			wheater_color = "#07b307"
		elif category == "Moderate":
			wheater_color = "#989807"
		elif category == "Unhealthy for Sensitive Groups":
			wheater_color = "#c86606"
		elif category == "Unhealthy":
			wheater_color = "#c40202"
		elif category == "Very Unhealthy":
			wheater_color = "#703376"
		elif category == "Hazardous":
			wheater_color = "#61011c"


		#Create a label to show the api

		myLabel = Label(root, text = city + " Air Quality : " + str(quality) + " " + category, font=("Helvetica",0), background=wheater_color)
		myLabel.grid(row=1,column=0, columnspan=2)
		#Configure the background
		root.configure(background=wheater_color) 

	except Exception as e:
		api = "Error..."


#Create the zip Entry
zip = Entry(root)
zip.grid(row=0,column=0,sticky=W+E+N+S)

#Create the zip Look Up button - attach to the zipLookup function
zipBtn = Button(root,text="Search by ZipCode", command=zipLookup)
zipBtn.grid(row=0,column=1,sticky=W+E+N+S)



root.mainloop()