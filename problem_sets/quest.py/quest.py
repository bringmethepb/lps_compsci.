# here I assigned variables for the user's character and the traits that the user will be asked to input 
print("Welcome to PB's Quest!")
print("Please enter the name of your character:")
userchrtr = str(raw_input())
print("Enter strength from 1 to 10:")
userstrength = int(raw_input())
print("Enter health from 1 to 10:")
userhealth = int(raw_input())
print("Enter luck from 1 to 10:")
userluck = int(raw_input())
userstats = int(userluck) + int(userstrength) + int(userhealth)

# here the computer computes the stats of the user's character and if they exceed the amount of 15 it will default their stats  
if userstats > 15:
	print("You have given your character too many points!Default values have been assigned," + str(userchrtr) + ": strength: 5, health: 5, luck: 5") 
else: 
	print(str(userchrtr) + ":strength:" + str(userstrength) + ", health:" + str(userhealth) + ", luck:" + str(userluck))

# here, the user is asked about the fork and whether they'll go left or right then the user inputs their choice  
print(str(userchrtr) + ", you've come across a fork in the road. Do you wish to go right or left? Enter 'left' or 'right'.") 
userchoice = str(raw_input()) 
# here, the users fate is determined by which way they chose to go and based on their stats, their fate  will be determined  
if userchoice == 'left' and userluck <= 5 and userstrength <= 5 or userhealth <= 2:
	print("Oh my! Some clowns appeared out of nowhere and stabbed you to death because you were not strong enough to fight them off. YOu lose :( ")
if userchoice == 'left' and  userluck >= 6 and userstrength >= 8 or userhealth >= 7:
	print("Some clowns appeared before you and you were able to fight them off and run away! You win!...for now..")
if userchoice == 'left' and userluck >= 7 and userhealth >= 6 or userstrength >= 7:
	print("A giant dog appeared before you and you were lucky enough to find a dog biscuit for it and you were healthy enough to run away. You win! ") 

if userchoice == 'right' and userstrength >= 6 and userhealth >= 6 or userluck >= 8:
	print("An old tree fell before you and you were able to jump over it and run away from Slenderman. You win!... for now...")
if userchoice == 'right' and userstrength <= 4 and userhealth <= 4 or userluck <= 2: 
	print("An old tree fell before you and you were not healthy enough to jump over it so a troll beat you to death with its stick. You lose :( ")  
if userchoice == 'right' and userluck <= 4 and userhealth <= 5: 
	print("Oh no, Slenderman appeared before you and you were not lucky nor healthy enough to be able to run away. You lose :( ") 
