print("Welcome to the convenience store!")
print("Enter your age:")
age = input()

age = int(age)

if age >= 18:
  print("Would you like to buy a lottery ticket?")
# if the user inputs age as 18 or higher, they will be asked this question
if age < 6:
  print("Would you like to buy a lollipop?")
# if the user puts in an age of 6 and younger, they will be asked this question 
