family = ["Josh", "Dani", "Cris", "Joanna", "Jenni"]
number = 1
for fam in family:
  print(str(number) + "." + fam)
  number = number + 1
family.append("Gabriel")
family.append("Mary")
family.append("Monce")
family.append("Ediht")
family.append("Tony")

family.sort()
family.reverse()
for fam in family:
  print(str(number) + "." + fam)
  number = number + 1
