def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True


# print(isPhoneNumber('510-378-8864'))
# print(isPhoneNumber('Harshini'))

message = 'call me at 510-378-8864 , can also reach me at 980-248-7185'

for i in range(len(message)):
	chunk = message[i:i+13]
	if isPhoneNumber(chunk):
		print('Phone Number found ' + chunk)
print("done")

