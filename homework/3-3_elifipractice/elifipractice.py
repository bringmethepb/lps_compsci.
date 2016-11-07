print('How many miles do you live from Richmond State?')
milesfromRS = int(raw_input())

if milesfromRS <= 30:
	print('Sweet! Just a few more questions before you can be admitted')
else:
	print('Oh no, you may still be admitted if your GPA is high enough')

print('What is your GPA?')
theirGPA = float(raw_input())

if theirGPA >= 2.0:
	print('Nice! One more question before you can be accepted')
else:
	if theirGPA >= 2.5:
		print('YOu still might make it in, bud')

print('What is your ACT score?')
theirACT = int(raw_input())

if theirACT >= 18:
	print('Hooray! You have now been admitted to Richmond State')
else:
	print('Sorry bud, you are not llegible for Richmond State')
