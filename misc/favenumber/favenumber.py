print("Please enter your favorite number.")
fave= int(raw_input())
while fave < 14 or fave > 14:
        print("I don't like that number - try another!")
        fave = int(raw_input())
else:
        print("You got it! That is the best number ever! You win!")
