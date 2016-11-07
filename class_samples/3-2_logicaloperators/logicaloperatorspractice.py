# number 2

print("How old are you?")
age = int(input())
# asks the user for their age, and the input is an integer for the variable age
print("How many inches tall are you?")
height = int(input())
# asks the user for their height in inches, and the input is an integer for the variable, height 
if age > 10 and height > 50:
	print("Hooray! You're old enough and tall enough to ride.")
else:
	print("Sorry, you can't ride.")
# the computer compares the inputted age and height and wether true then it prints the first statement and if not then it prints the second statement 
