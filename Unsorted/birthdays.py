birthdays = {'Nikhil':'Oct 29','Harshini':'Feb 21', 'Manideep':'June 5', 'Nana':'Oct 15'}

while True:
	print("Enter the Name: (enter blank to exit)")
	name = input()
	if name == '':
		break

	if name in birthdays:
		print("Birthday of "+name+ " is "+ birthdays[name])
	else:
		print("I do not have Bday info of "+name)
		print("Enter their Bday")
		bday = input()
		birthdays[name] = bday
		print("Birthday of "+ name + " is "+ birthdays[name])
