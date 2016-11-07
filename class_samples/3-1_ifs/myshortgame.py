fave = 666

print('Enter a number:')

your_number = raw_input()

if your_number > fave:
	print('Sorry, you lose. :(')
	print('Please try again')
	print('I will give you a hint, try aiming a bit lower')
if your_number < fave:
	print('Not quite, I will give you a hint, try aiming a bit higher into three digit number')
if your_number < 100:
	print('Higher!!')
if your_number < 200:
	print('Even higher!')
if your_number == fave:
	print('Hooray, you won! You must be a genius! o .o ')
 
