import random

heads = []
tails = []

def coinFlip():
	while True:
		resp = input("Please type FLIP to flip a coin. Type X when done.")
		if (resp=='FLIP'):
			print("Flipping coin . . . ")

			flip = random.randint(1, 2)

			if flip==1:
				print("Heads!")
				heads.append(1)
			elif flip==2:
				print("Tails!")
				tails.append(1)
			else:
				print("An error has occured.")
		elif (resp=='X'):
			break
		else:
			print("Please try again.")

def stats():
	print("Stats: ")
	print(f"You got heads {sum(heads)} times. You got tails {sum(tails)} times.")

	headsPercent = (sum(heads) / (sum(heads) + sum(tails))) * 100
	tailsPercent = (sum(tails) / (sum(heads) + sum(tails))) * 100

	print(f"Your flips were {headsPercent:.2f}% heads and {tailsPercent:.2f}% tails.")

def coinChoice():
	coin = input("Please choose a coin to flip. 'PENNY', 'NICKLE', 'DIME', 'QUARTER'")
	print(f"You chose a {coin}! Happy flipping!")

def gameChoice():
	choice = input("Would you like to flip a 'coin' or roll an 8 'ball': ")

	if (choice=='coin'):
		coinChoice()
		coinFlip()
		stats()
	elif (choice=='ball'):
		ballRoll()

def ballRoll():
	wish = input("What would you like to ask the magic 8 ball?")

	rand = random.randint(1, 3)

	if rand==1:
		print("Yes, absolutely.")
	elif rand==2:
		print("Maybe next time...")
		tails.append(1)
	else:
		print("No, definetly not.")

def main():
	gameChoice()

if __name__ == '__main__':
	main()