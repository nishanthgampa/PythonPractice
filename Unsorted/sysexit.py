import sys

while True:
	print("Type exit")
	typed = input()
	if typed=='exit':
		sys.exit()
	print("I told you to type exit and you typed " + typed)
