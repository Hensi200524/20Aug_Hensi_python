"""Write a Python program to generate random numbers between 1 and
100 using the random module"""

import random

x = random.randint(1, 100)
print("Random number between 1 and 100:", x)

x= random.random()
print("Random float number between 0 and 1:", x)

y = random.uniform(1, 100) # generates a random float between 1 and 100
print("Random float number between 1 and 100:", y)