from tkinter import *
from PIL import ImageTk,Image
import mysql.connector #Import the MYSQL module
import csv
from tkinter import ttk #For the drop menu usage


root = Tk()
root.title('CRM Database Tool')
root.iconbitmap("C:/Users/plantadmin_HS_CM/test/Python/images/test.ico")
root.geometry("400x500") #Define the gemoetry of the window

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

#Create the table - run once to create or check if exists 
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(255), \
	last_name VARCHAR(255),\
	zipcode INT(10),\
	price_pay DEC(10,2),\
	user_id INT AUTO_INCREMENT PRIMARY KEY)")  

#If you need to delete the table
#my_cursor.execute("DROP TABLE customers")

'''
#Alter the table - Add more
my_cursor.execute("ALTER TABLE customers ADD (\
	email VARCHAR(225),\
	adress_1 VARCHAR(255),\
	adress_2 VARCHAR(255),\
	city VARCHAR(50),\
	state VARCHAR(50),\
	country VARCHAR(255),\
	phone VARCHAR(255),\
	payment_method VARCHAR(50),\
	discount_code VARCHAR(255))")

'''


#Show the table
#my_cursor.execute("SELECT * FROM customers")
#print(my_cursor.description)
#for things in my_cursor.description:
#	print(things)

#Create the clear filds function
def clear_filds():
	first_name_box.delete(0,END)
	last_name_box.delete(0,END)
	address1_box.delete(0,END)
	address2_box.delete(0,END)
	city_box.delete(0,END)
	state_box.delete(0,END)
	zipcode_box.delete(0,END)
	country_box.delete(0,END)
	phone_box.delete(0,END)
	email_box.delete(0,END)
	payment_method_box.delete(0,END)
	discount_code_box.delete(0,END)
	price_paid_box.delete(0,END)


#create the add customer function for the button
def add_customer():
	sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_pay, email, adress_1, adress_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
	my_cursor.execute(sql_command, values)

	#commit changes
	mydb.commit()
	#clear the filds
	clear_filds()


#write to CSV file
def write_to_csv(result):
	with open("customers.csv","a", newline='') as f: 
		w = csv.writer(f, dialect='excel')
		for record in result:
			w.writerow(record)

#create a function to shows the customers
def list_customers():
	#create a new windows
	list_customers_querry = Tk()
	list_customers_querry.title('CRM Database Tool')
	list_customers_querry.iconbitmap("C:/Users/plantadmin_HS_CM/test/Python/images/test.ico")
	list_customers_querry.geometry("800x600") #Define the gemoetry of the window
	#Query the database and loop trough
	my_cursor.execute("SELECT * FROM customers")
	result = my_cursor.fetchall()
	#we loot twice . ince trought the rows and then trough the columns 
	for index,x in enumerate(result):
		num = 0
		for y in x:
			look_up_label = Label(list_customers_querry,text=y)
			look_up_label.grid(row=index,column=num)
			num +=1

	csv_button = Button(list_customers_querry,text="Save to Excel",command=lambda: write_to_csv(result))
	csv_button.grid(row=index+1,column=0)

#Search customers function
def search_customer():
#create a new windows
	search_customers = Tk()
	search_customers.title('Search Customers')
	search_customers.iconbitmap("C:/Users/plantadmin_HS_CM/test/Python/images/test.ico")
	search_customers.geometry("800x600") #Define the gemoetry of the window

	def search_now():
		selected = drop.get()
		if selected == "Search by...":
			test = Label(search_customers,text="You forgot to select from the drop menu")
			test.grid(row=2,column=0)
		if selected == "Last Name":
			sql = "SELECT * FROM customers WHERE last_name = %s"
		if selected == "Email Adress":
			sql = "SELECT * FROM customers WHERE email = %s"
		if selected == "Customer ID":
			sql = "SELECT * FROM customers WHERE user_id = %s"

		
		searched = search_box.get()
		#sql = "SELECT * FROM customers WHERE last_name = %s"
		name = (searched, )
		result = my_cursor.execute(sql,name)
		result = my_cursor.fetchall()

		if not result:
				result ='Record not found....'

		searched_label = Label(search_customers, text=result)
		searched_label.grid(row=3,column=0,padx=10,pady=10)
		


	#create a box for search for customer
	search_box= Entry(search_customers)
	search_box.grid(row=0,column=1,padx=10,pady=10)
	#create a box for search label
	search_box_label= Label(search_customers,text="Search Customer")
	search_box_label.grid(row=0,column=0,padx=10,pady=10)
	#create a button for search for customer
	search_button= Button(search_customers,text="Search Customers",command=search_now)
	search_button.grid(row=1,column=0,padx=10,pady=10)

	#Create the drop menu search box
	drop = ttk.Combobox(search_customers,value=["Search by...","Last Name","Email Adress", "Customer ID"])
	drop.current(0)
	drop.grid(row=0,column=2)

#Create a label
title_label = Label(root,text="Codemy Customers Database",font=("Helvetica",16))
title_label.grid(row=0,column=0,columnspan=2,pady=10)

#Create Main Form to enter customer data
first_name_label = Label(root,text="First Name").grid(row=1,column=0, sticky=W,padx=10)
last_name_label = Label(root,text="Last Name").grid(row=2,column=0, sticky=W,padx=10)
address1_label = Label(root,text="Adress 1").grid(row=3,column=0, sticky=W,padx=10)
address2_label = Label(root,text="Adress 2").grid(row=4,column=0, sticky=W,padx=10)
city_label = Label(root,text="City").grid(row=5,column=0, sticky=W,padx=10)
state_label = Label(root,text="State").grid(row=6,column=0, sticky=W,padx=10)
zipcode_label = Label(root,text="ZipCode").grid(row=7,column=0, sticky=W,padx=10)
country_label = Label(root,text="Country").grid(row=8,column=0, sticky=W,padx=10)
phone_label = Label(root,text="Phone Number").grid(row=9,column=0, sticky=W,padx=10)
email_label = Label(root,text="Email Adress").grid(row=10,column=0, sticky=W,padx=10)
payment_method_label = Label(root,text="Payment Method").grid(row=11, sticky=W,padx=10)
discount_code_label = Label(root,text="Discount Code").grid(row=12, sticky=W,padx=10)
price_paid_label = Label(root,text="Price paid").grid(row=13, sticky=W,padx=10)

#Create the entry boxes
first_name_box = Entry(root)
first_name_box.grid(row=1,column=1)
last_name_box =Entry(root)
last_name_box.grid(row=2,column=1, pady=5)
address1_box = Entry(root)
address1_box.grid(row=3,column=1, pady=5)
address2_box = Entry(root)
address2_box.grid(row=4,column=1, pady=5)
city_box = Entry(root)
city_box.grid(row=5,column=1, pady=5)
state_box = Entry(root)
state_box.grid(row=6,column=1, pady=5)
zipcode_box = Entry(root)
zipcode_box.grid(row=7,column=1, pady=5)
country_box = Entry(root)
country_box.grid(row=8,column=1, pady=5)
phone_box = Entry(root)
phone_box.grid(row=9,column=1, pady=5)
email_box = Entry(root)
email_box.grid(row=10,column=1, pady=5)
payment_method_box = Entry(root)
payment_method_box.grid(row=11,column=1, pady=5)
discount_code_box = Entry(root)
discount_code_box.grid(row=12,column=1, pady=5)
price_paid_box = Entry(root)
price_paid_box.grid(row=13,column=1, pady=5)

#ADD BUTTONS

#Add the submit button
customer_add_button = Button(root,text="Add Customer to the DataBase",command=add_customer)
customer_add_button.grid(row=14,column=0,padx=10,pady=10)

#Add clear stuff button

clear_filds_button = Button(root,text="Clear Filds", command=clear_filds)
clear_filds_button.grid(row=14,column=1)

#Show customers button

show_customers_btn = Button(root,text="Show customers", command=list_customers)
show_customers_btn.grid(row=15,column=0,sticky=W,padx=10)

#Search Customers button
search_customers_button = Button(root,text="Search Customers", command=search_customer)
search_customers_button.grid(row=15,column=1,sticky=W,padx=10)

root.mainloop()