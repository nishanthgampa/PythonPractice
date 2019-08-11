import random

number = random.randint(1,20)
print("I'm thinking of a number between 1 to 20")


for guessTaken in range(1,7):
	print("Take a Guess")
	x = int(input())
	if x < number:
		print("You guessed too low")
	elif x > number:
		print("You guessed too high")
	else:
		break

if x == number:
	print("You guessed it right attaboy")
else:
	print("Not very lucky, I was thinking of", str(number))