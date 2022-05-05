from tkinter import *
from PIL import ImageTk,Image
import mysql.connector #Import the MYSQL module



root = Tk()
root.title('CRM Database Tool')
root.iconbitmap("C:/Users/plantadmin_HS_CM/test/Python/images/test.ico")
root.geometry("400x400") #Define the gemoetry of the window

#Connect to the MySQL Database
mydb = mysql.connector.connect(
	host = "192.168.1.60",
	port = "49153",
	user = "royal",
	passwd = "cool911",
	database = "codemy"
	)
#Show if the connection was succesufuly in the console
#print(mydb)

#Create a cursor and initialize
my_cursor = mydb.cursor()

#Create the database
#my_cursor.execute("CREATE DATABASE codemy")  - Was run just once

#Once the database was create - we can test
#my_cursor.execute("SHOW DATABASES")

#Checked to see if the database is created
#for db in my_cursor:
#	print(db)

#Create the table
#my_cursor.execute("CREATE TABLE customers (first_name VARCHAR(255), last_name VARCHAR(255), zipcode INT(10), price_pay DEC(10,2), user_id INT AUTO_INCREMENT PRIMARY KEY)")  - run once to create


#Show the table
my_cursor.execute("SELECT * FROM customers")
print(my_cursor.description)

root.mainloop()