import random
myNum = random.randint(1, 1000)
# the variable 'userGuess' is assigned any number because it doesn't matter, the user just has to keep entering a number until they guess the computer's 
userGuess = -1000
#the user is asked to enter any number between 1 and 1000
print("I am thinking of a number between 1 and 1000. Enter your guess!")
# the while loop starts and the user variable is assigned whichever number they input 
while userGuess < 1000:
	userGuess = int(raw_input())
# if the users guess is greater than the computer's random number it'll say that they're too high and have to retry 
	if userGuess > myNum:
		print("Nope, too high! Guess again.")
# if the statement above is not true, then it'll say if the users guess is lower than the computer's guess
	elif userGuess < myNum:
		print("Nope, too low! Guess again.")
# if the user guesses the computer's number then it'll say they're correct
	elif userGuess == myNum: 
		print("Hooray, you won!")
#the variable for the users guess is reassigned a number greater than 1000 so that the while loop doesn't continue to run 
		userGuess = 1001
		
