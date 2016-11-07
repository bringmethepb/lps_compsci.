print('Enter amount of purchases, in cents')
purchase = int(raw_input())

discount = float(purchase * .10)
finalpurchase = int(purchase - discount)
if purchase > 100:
	print('You spent over $10! Your final price is' + 'finalpurchase' + 'cents.')
