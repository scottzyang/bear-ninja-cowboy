player = input("Bear, Ninja, or Cowboy? > " )
print(player)

# Import the random method from the randint module
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

print(computer)
