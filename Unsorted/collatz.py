print("Please enter your number")

try:
	inputNumber = int(input())
except ValueError:
	print("Give me the number idiot")

def collatz(number):
	while True:
		if number % 2 == 0:
			number = number//2
			print(number)
			if number == 1: break
		elif number % 2 == 1:
			number = (number * 3) + 1
			print(number)
			if number == 1: break




