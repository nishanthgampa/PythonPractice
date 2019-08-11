dogNames = []
while True:
	print("Enter the Name of Dog " + str(len(dogNames)+1) + " or press enter if you are done" )
	nameOfDog = input()
	if nameOfDog == '':
		break
	dogNames = dogNames + [nameOfDog]
print("The Dog names are: ")
for i in dogNames:
	print("  "+i)
