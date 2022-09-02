# Import the random method from the randint module
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# declare a variable called play and assigned to boolean False
play = False

# initiates game logic
while play == False:
    # verifies if user input exist as valid character
    while True:
        # define roles of player and computer
        player = input("Bear, Ninja, or Cowboy? > " )
        computer = roles[randint(0,2)]

        if player not in roles:
            print("Please input a valid character")
        else:
            break
    
    # if character exists, compare the computer role with user role
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


    # prompt user if they want to play again
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      play = False
    else:
      break
