# the user is welcomed and asked line by line for their haiku 
print("Welcome to the Haiku generator!" + "\n" + "Provide the first line of your haiku:")
first_Line = str(raw_input())
print("Provide the second line of your haiku:")
second_Line = str(raw_input())
print("Provide the third line of your haiku:")
third_Line = str(raw_input())

# the user is asked where they would like to put their haiku 
print("What file would you like to write your haiku to?")
userFile = str(raw_input())      

# this opens the text file that the user named and inserts line by line the haiku  
userHaiku = open((userFile), "w")
userHaiku.write(first_Line + "\n" + second_Line + "\n" + third_Line + "\n")

# this tells the user they can now check their haiku and closes the text file so it doesn't run forever 
print("Done! To view your haiku, type 'cat' and the name of your file at the command line.")
userHaiku.close()
