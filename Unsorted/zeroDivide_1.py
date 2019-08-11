def spam(divideBy):
	return 42/divideBy

try:
	print(spam(10))
	print(spam(100))
	print(spam(0))
except ZeroDivisionError:
	print("Invalid Argument")