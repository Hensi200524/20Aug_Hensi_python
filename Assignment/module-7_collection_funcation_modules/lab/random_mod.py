"""Write a Python program to generate random numbers using the random module."""

import random

# Generate a random integer between 1 and 100
random_integer = random.randint(1, 100)
print("Random integer between 1 and 100:", random_integer)

# Generate a random float between 0 and 1
random_float = random.random()
print("Random float between 0 and 1:", random_float)

# Generate a random choice from a list
options = ['apple', 'banana', 'cherry']
random_choice = random.choice(options)
print("Random choice from list:", random_choice)