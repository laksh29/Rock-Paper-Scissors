# print("...rock...")
# print("...paper...")
# print("...scissors...")

 

# from random import choice
# com = choice(['rock','paper','scissors'])



# p1 = input("Enter player's choice:")
# p2 = print(f"computer's choice is: {com}") 


# if p1 == "rock":
# 	if com == "rock":
# 		print("It's a tie!")
# 	elif com == "paper":
# 		print("computer wins!")

# 	elif com == "scissors":
# 		print("player wins!")

	

# elif p1 == "paper":
# 	if com == "rock":
# 		print("player wins!")

# 	elif com == "paper":
# 		print("It's a tie!")

# 	elif com == "scissors":
# 		print("computer wins!")


# elif p1 == "scissors":
# 	if com == "rock":
# 		print("computer wins!")

# 	elif com == "paper":
# 		print("player wins!")

# 	elif com == "scissors":
# 		print("It's a tie!")

# else:
# 	print("something went wrong!")


	#  OR

from random import randint
print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player make your move: ").lower()
rand_num = randint(0,2)

if rand_num == 0:
	computer = "rock"

elif rand_num == 1:
	computer = "paper"
	
else:
	computer = "scissors"

print(f"Computer plays {computer}" )

if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")

elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")

elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	

else:
	print("Please enter a valid move!")