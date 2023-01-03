import random

randomNo = random.randint(1,100)
guesses= None
noGuess=0
while (guesses != randomNo):
	guesses = int(input("Enter your guess: "))
	noGuess=noGuess + 1
	if guesses == randomNo:
		print("Your guess is correct!!")
	else:
		if guesses>randomNo:
			print("Please enter smaller number")
		else:
			print("Please enter bigger number")
			
print(f"The no of guesses taken are: {noGuess}")
