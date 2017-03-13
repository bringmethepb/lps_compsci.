class Player(object):
# objects are created for this class
	def __init__(self, name, age, goals, jerseyNumber, position): 
		self.name = name 
		self.age = age 
		self.goals = goals 
		self.jerseyNumber = jerseyNumber
		self.position = position 

	def getStats(self):
		summary = "Name: " + self.name + "\n"
		summary = summary + "Age: " + self.age + "\n"
		summary = summary + "Goals: " + self.goals + "\n"
		summary = summary + "Jersey Number: " + self.jerseyNumber + "\n" 
		summary = summary + "Position: " + self.position + "\n"  
		return summary 

#an empty list for the team players is made here
myPlayers = [] 

#a boolean is made here for the choices of the suer to choose from
Tom3 = True 
#this while loop is true and prints the options for the user 
while Tom3: 
	print("Welcome to the new ultimate Team Manager Deluxe.") 
	print("What would you like to do? Enter your choice and press 'enter'.")
	print("(1) Add a player")
	print("(2) Print all players")
	print("(3) Save your player list to a file")
	print("(0) Leave the program (save first to avoid losing your data!)")
  
 	response = input()
# the while loop doesn't run if the user inputs 0, making the boolean 'false'  
	if response == 0: 
		Tom3 = False 

#if the user chooses option 1 the loop is ran for the user put in a player of their own which then adds the player to the empty list from above
	elif response == 1: 
		print("Enter name: ")
		userPlayer = raw_input() 
		print("Enter Age: ")
		userAge = raw_input() 
		print("Enter number of goals scored this season: ") 
		userGoals = raw_input() 
		print("Enter jersey number: ") 
		userJerseyNum = raw_input()
		print("Enter the position: ") 
		userPosition = raw_input() 

		userPlaya = Player(userPlayer, userAge, userGoals, userJerseyNum, userPosition)
    
		myPlayers.append(userPlaya) 
		print("Okay, player entered!") 
# if the user chooses this optin, then whatever players are in the list then their stats will be printed to the user     
	elif response == 2: 
		for m in myPlayers:
			print(m.getStats())
	elif response == 3: 
		print("Where'd you like to save your players? Enter a file name, we'll add the '.txt' for ya.")
		user_filename = raw_input() 
		filename = user_filename + ".txt"
		filename = open((filename), "w") 

# takes the playerList and the user's desired filename
# writes each Player to file
def saveTeam(playerList, filename):
    # open the file
	filename = open((filename), "r")
    # write to the file
	filename = open((filename), "a")
	filename.write(userPlaya)
	filename.readline()
    # close the file
	filename.close()
    # placeholder - delete once the function is complete
 
# takes a filename for a file of players
# returns a list of Players
def loadTeam(filename):
 
    # create empty list
	myList = [] 
    # open the file
        my_File = open((filename), "r") 
    # read each line and create Player from it (use a loop)
 	for f in file:
		line = my_File.readline()
        # split each line into a list of the variables
		myList = myList.split(" ") 
        # read each next line
		myList.readline() 
    # close the file
	my_File.close() 
    # return the completed list
	print(my_List) 
    # placeholder - delete once the function is complete
