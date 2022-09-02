# Import the random method from the randint module
from random import randint

# game logic to determine winner 
def win_or_lose(player, computer):
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

# Intro
print("Get ready to play Bear, Ninja Cowboy!")

# Instructions to play
instructions = input("Would you like instructions on how to play? (yes/no) ")
if instructions.lower() == "yes":
    print("Select a player you'd like, and see if you can beat the computer!")
        

# Define roles 
roles = ["Bear", "Ninja", "Cowboy"]

# declare a variable called play and assigned to boolean False
player = False

# initiates game logic
while player == False:
    # verifies if user input exist as valid character
    while True:
        player = input("Bear, Ninja, or Cowboy? > " ) # Prompts user for player selection
        computer = roles[randint(0,2)]
        if player not in roles:
            print("Please input a valid character")
        else:
            break

    win_or_lose(player, computer)

    # prompt user if they want to play again
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
    else:
      break
