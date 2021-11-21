#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

try:
    while True:
        user_choice = input("Enter a choice (rock, paper, scissors): ")
        possible_choice = ["rock", "paper", "scissors"]
        computer_choice = random.choice(possible_choice)
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
 
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
    
        
    
        
except:
    print("Error in code")
    


# In[ ]:




