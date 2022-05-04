from tkinter import *
from PIL import ImageTk,Image
import sqlite3 # Import the SQLLite database

root = Tk()
root.title('Learn to code')
root.iconbitmap("C:/Users/plantadmin_HS_CM/test/Python/images/test.ico")
root.geometry("350x500") #Define the gemoetry of the window

#DATABASES

#create a database or connect to one
conn = sqlite3.connect("adress_book.db")

#create a cursor
c = conn.cursor()

#create the table
'''
c.execute("""CREATE TABLE addresses(
			first_name text,
			last_name text,
			address text,
			city text,
			state text,
			zipcode integer
)
	""")
'''

def update():
	#create a database or connect to one
	conn = sqlite3.connect("adress_book.db")

	#create a cursor
	c = conn.cursor()

	record_id = delete_box.get()
	#execute the querry to update the database
	c.execute("""UPDATE addresses SET
			first_name= :first,
			last_name= :last,
			address= :adress,
			city= :city,
			state= :state,
			zipcode= :zipcode
			WHERE oid= :oid""",
			{
				'first': f_name_editor.get(),
				'last': l_name_editor.get(),
				'adress': adress_editor.get(),
				'city': city_editor.get(),
				'state': state_editor.get(),
				'zipcode': zipcode_editor.get(),
				'oid': record_id
			}
		)

	#Commit the changes
	conn.commit()

	#Close the connection
	conn.close()

	#close the window
	editor.destroy()

	
#Create the function to delete a record
def delete():
	#create a database or connect to one
	conn = sqlite3.connect("adress_book.db")

	#create a cursor
	c = conn.cursor()

	#Delete the record query
	c.execute("DELETE FROM addresses WHERE oid=" +delete_box.get())


	#Commit the changes
	conn.commit()

	#Close the connection
	conn.close()


#create the submit function
def submit():
	#create a database or connect to one
	conn = sqlite3.connect("adress_book.db")

	#create a cursor
	c = conn.cursor()

	#Insert into the table
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :adress, :city, :state, :zipcode)",
		{
			'f_name': f_name.get(),
			'l_name': l_name.get(),
			'adress': adress.get(),
			'city': city.get(),
			'state': state.get(),
			'zipcode': zipcode.get()
		}
	)


	#clear the text boxes
	f_name.delete(0,END)
	l_name.delete(0,END)
	adress.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)


	#Commit the changes
	conn.commit()

	#Close the connection
	conn.close()


#create the query function
def query():
	#create a database or connect to one
	conn = sqlite3.connect("adress_book.db")

	#create a cursor
	c = conn.cursor()

	#Query the database
	c.execute("SELECT *,oid from addresses")
	records = c.fetchall()
	#print(records)


	#Loop troght results
	print_record=''
	for record in records:
		print_record += str(record[0]) + " " + str(record[1]) + "\t "+ str(record[6]) + "\n"

	query_label=Label(root,text=print_record)
	query_label.grid(row=12,column=0,columnspan=2)

	#Commit the changes
	conn.commit()

	#Close the connection
	conn.close()

#define the delete function
def edit():
	global editor
	editor = Tk()
	editor.title('Update the records')
	editor.iconbitmap("C:/Users/plantadmin_HS_CM/test/Python/images/test.ico")
	editor.geometry("350x200") #Define the gemoetry of the window

	#create a database or connect to one
	conn = sqlite3.connect("adress_book.db")

	#create a cursor
	c = conn.cursor()

	#Query the database
	select_id = delete_box.get()
	c.execute("SELECT * from addresses WHERE oid=" +select_id)
	records = c.fetchall()

	#To be use outside of function - declare as globals
	global f_name_editor
	global l_name_editor
	global adress_editor
	global city_editor
	global state_editor
	global zipcode_editor
	
	#Define the imputs
	f_name_editor=Entry(editor, width=30)
	f_name_editor.grid(row=0,column=1,padx=20, pady=(10, 0))
	l_name_editor=Entry(editor, width=30)
	l_name_editor.grid(row=1,column=1)
	adress_editor=Entry(editor, width=30)
	adress_editor.grid(row=2,column=1)
	city_editor=Entry(editor, width=30)
	city_editor.grid(row=3,column=1)
	state_editor=Entry(editor, width=30)
	state_editor.grid(row=4,column=1)
	zipcode_editor=Entry(editor, width=30)
	zipcode_editor.grid(row=5,column=1)
	
	#Define the labels
	f_name_label=Label(editor,text="First Name")
	f_name_label.grid(row=0,column=0, pady=(10, 0))
	l_name_label=Label(editor,text="Last Name")
	l_name_label.grid(row=1,column=0)
	adress_label=Label(editor,text="Adress")
	adress_label.grid(row=2,column=0)
	city_label=Label(editor,text="City")
	city_label.grid(row=3,column=0)
	state_label=Label(editor,text="State")
	state_label.grid(row=4,column=0)
	zipcode_label=Label(editor,text="Zipcode")
	zipcode_label.grid(row=5,column=0)


	#Loop troght results
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		adress_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		zipcode_editor.insert(0, record[5])

	#define the save button
	save_btn=Button(editor,text="Save Record", command=update)
	save_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=130)


#Define the imputs
f_name=Entry(root, width=30)
f_name.grid(row=0,column=1,padx=20, pady=(10, 0))
l_name=Entry(root, width=30)
l_name.grid(row=1,column=1)
adress=Entry(root, width=30)
adress.grid(row=2,column=1)
city=Entry(root, width=30)
city.grid(row=3,column=1)
state=Entry(root, width=30)
state.grid(row=4,column=1)
zipcode=Entry(root, width=30)
zipcode.grid(row=5,column=1)
delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)

#Define the labels
f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0, pady=(10, 0))
l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
adress_label=Label(root,text="Adress")
adress_label.grid(row=2,column=0)
city_label=Label(root,text="City")
city_label.grid(row=3,column=0)
state_label=Label(root,text="State")
state_label.grid(row=4,column=0)
zipcode_label=Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)
delete_label=Label(root,text="Select ID")
delete_label.grid(row=9,column=0,pady=5)

#create Submit Button

submit_btn=Button(root,text="Add record to database", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#create a querry button
query_btn=Button(root,text="Show records", command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=127)

#create a delete button
delete_btn=Button(root,text="Delete record", command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=127)

#create an update button
edit_btn=Button(root,text="Edit record", command=edit)
edit_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=134)

#Commit the changes
conn.commit()

#Close the connection
conn.close()





root.mainloop()