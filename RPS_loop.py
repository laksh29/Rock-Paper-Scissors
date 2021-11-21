from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")

while True: 
	player = input("Player, make your move:").lower()
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"

	elif rand_num == 1:
		computer = "paper"

	else:
		computer = "scissors"

	print(f"computer plays {computer}")

	if player == computer:
		print("It's a tie!")

	elif player == "rock":
		if computer == "paper":
			print("computer wins!")

		elif  computer == "scissors":
			print("player wins!")

	elif player == "paper":
		if computer == "rock":
			print("player wins!")

		elif computer == "scissors":
			print("computer wins!")

	elif player == "scissors":
		if computer == "rock":
			print("commputer wins!")

		elif computer == "paper":
			print("player wins!")

	else:
		print("somethig went wrong !")
	ask = input("Continue playing? (y/n): ").lower()
	if ask != "y":
		print("Good playing with you!")
		break