from tkinter import *
from random import randint

root = Tk()
root.title('Learn to code')
root.iconbitmap("images/test.ico")
root.geometry("400x400") #Define the gemoetry of the window



def pick():
	#89 entries
	entries = ['Sanbid Roy Chowdhury', 'The refuge Malik', 'Google India', 'DotDotCom', 'Jon Layman', 'Itz Omen', 'Roberto Picco', 'Adigun olamide', 'Saurabh Parate', 'Exceptional Faruk', 'Avinash Upadhyaya', 'Fabio F. de Aquino', 'Ganesh Hegde', 'Hardy Don', 'Trap Town NCS', 'NIRMAL SRINIVAS CHINTALA', 'Weston', 'Gavin Hou', 'Bhanumathi A', 'Faoud Mohd ', 'rocket science', 'LucaVont', 'Kristian Simko', 'LunarAtom', 'Code With Wasif', 'Shreyas shetty', 'Panagiotis V', 'Dan Esquibel', 'TechiesSpammer69', 'John Dripper', 'Barbossa', 'Sahan Eakanayaka', 'Cassio Lacaz', 'Ranga bharath', 'Kisalay Suman', 'Le Dung', 'Mildo', 'Ivan Yosifov', 'Shreyas shetty', 'pranav Bhatki', 'Atharv Nuthi', 'Tibas Tiba', 'Yash Thakkar', 'Dario', 'deranged llama', 'Tom Blackwood', 'Christian Dimayacyac', 'Shaun A', 'Tchosk', 'Ahsan Arain', 'GRANDHI NAGESHWARAO', 'Baby Daily Life', 'PERFECT IGBADUMHE', 'Amad Ahmed', 'benage andy', 'Gerald Minoza', 'Samuel Hafer', 'Augusto Sousa', 'Andreas Mls', 'Somali flame', 'GPSSerbia', 'Hima Subedi', 'Ignatus Nana Amoah', 'Videos Promoter', 'Nabil Fantes', 'collins anele', 'Utku Yucel', 'Robert Coffie', 'M Dandan', 'Hudaibia Syed', 'abdurrahman zakariya', 'sabin katwal', 'Hardy Don', 'v sr', '10 bitangaje', 'Jon Bascos', 'Gaming Hub', 'Ace Hardy', 'Arsh Bains', 'Hima Subedi', 'Samuel Hafer', 'Fake Account', 'Spider', 'Callum Telford', 'Nikola Franicevic', 'David Blankinship', 'Unison', 'ramona Saintandre', 'Mohan hari krishna']
	#convert to a sec
	entries_set = set(entries)
	#convert it back to a list  - 85
	uniq_entries = list(entries_set)

	#create our  list size variable
	our_number = len(uniq_entries)-1

	#create a random number between 0 and 84
	rando = randint(0,our_number)

	winnerLabel = Label(root,text=uniq_entries[rando] , font=("Helvetica",24))
	winnerLabel.pack(pady=50)


topLabel = Label(root,text="Win-0 Rama!", font=("Helvetica",24))
topLabel.pack(pady=20)

winButton = Button(root,text="Pick the winner",font=("Helvetica",24), command=pick)
winButton.pack(pady=20)


root.mainloop()