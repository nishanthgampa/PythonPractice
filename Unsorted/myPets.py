myPets = ['Harley', 'Zorro', 'Whisky','Hercules']
print("Enter the name of your pet")
petName = input()
if petName not in myPets:
	print("I do not have a pet named ", petName)
else:
	print("I do have a pet named ", petName)