"""Write a generator function that generates the first 10 even numbers"""

def even_numbers():
    num = 2
    count = 0
    while count < 10:
        yield num        # produce the next even number
        num += 2
        count += 1

# Using the generator
for n in even_numbers():
    print(n)
