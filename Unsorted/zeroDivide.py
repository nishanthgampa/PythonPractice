def spam(divideBy):
	try:
		return 42/divideBy
	except ZeroDivisionError:
		print("invalid argument")

print(spam(10))
print(spam(2))
print(spam(40))
print(spam(0))