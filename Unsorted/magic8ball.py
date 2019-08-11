import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is Certain"
	elif answerNumber ==2:
		return "It is decidedly so"
	elif answerNumber == 3:
		return "Yes"
	elif answerNumber == 4:
		return "Reply Hazy Try Agaian"
	elif answerNumber == 5:
		return "Ask Again Later"
	elif answerNumber == 6:
		return "Concentrate and ask again"
	elif answerNumber == 7:
		return "My reply is No"
	elif answerNumber == 8:
		return "Very doubtful"
	elif answerNumber == 9:
		return "Outlook not so good"

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

