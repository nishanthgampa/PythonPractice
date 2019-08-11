while True:
	print("Enter your age")
	age = input()
	if age.isdecimal():
		break
	else:
		print('Enter only numbers')

print("Age is " + str(age))

while True:
	print("Enter your password")
	password = input()
	if password.isalnum():
		break
	else:
		print("Only numbers and text allowed")
print("Password is " + password)