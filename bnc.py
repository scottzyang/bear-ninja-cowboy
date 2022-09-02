# Import the random method from the randint module
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Define player role
player = input("Bear, Ninja, or Cowboy? > " )

# Generate a random role using an array
computer = roles[randint(0,2)]

print(computer, player)