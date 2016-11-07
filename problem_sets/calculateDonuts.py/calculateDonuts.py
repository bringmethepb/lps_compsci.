print('How many people will you have at your party?') 
partypeople = int(raw_input()) 
print('How many donuts will you have at your party?')
partydonuts = int(raw_input())
print('Our party has' + str(partypeople) + 'people, and' + str(partydonuts) + 'donuts') 

donutsforperson = int(partydonuts // partypeople)  

print("Each person at the party gets" + str(donutsforperson) + "donuts") 
