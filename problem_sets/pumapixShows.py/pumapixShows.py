print("Welcome to PumaPix!") 
# here i make a variable for the list of shows to be empty then ask the user for their five fave shows 
my_list = []
print("Enter your 5 favorite TV shows.")
tvshows = raw_input()
# here i assign a variable to be 0 because it will be added as the list builds 
num = 0
while num < 4:
	print("Enter a show name:")
	num = num + 1
	tvshows = raw_input() 
	my_list.append(tvshows)
print(my_list)
# during the above while loop, the shows taht are inserted by the user are being added into the empty list variable
print("We have added two more important shows:")
my_list.append("Breaking Bad")
my_list.append("The Wire")
my_list.sort()
# above, the two shows are added into the builted tv shows list 
number = 0
for show in my_list:
	number = number + 1
	my_list.sort()
	print(str(number) + "." + show)
# above, the list of shows and shows added are listed one by one and numbered
