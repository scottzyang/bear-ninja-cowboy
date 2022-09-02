# Import the random method from the randint module
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

player = False

while player == False:
    player = input("Bear, Ninja, or Cowboy? > " )
    
    if player == computer:
        print("Draw!")
    elif computer == "Cowboy":
        if player == "Bear":
            print(f"You lose! {computer} shoots {player}")
        else: # if player is ninja
            print(f"You win! {player} beats {computer}")
    elif computer == "Bear":
        if player == "Cowboy":
            print(f"You win! {player} shoots {computer}")
        else: # if player is ninja
            print(f"You lose! {computer} eats {player}")
    elif computer == "Ninja":
        if player == "Cowboy":
            print(f"You lose! {player} is defeated by {computer}")
        else: # computer is ninja, player is bear
            print("You win!", player, "eats", computer)

    player = False
    computer = roles[randint(0,2)]
