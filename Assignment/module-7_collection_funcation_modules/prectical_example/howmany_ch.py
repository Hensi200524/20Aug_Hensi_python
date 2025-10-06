"""Write a Python program to count how many times each
character appears in a string."""

string = "hello world" # Example string

char_count = {} # Dictionary to store character counts
for char in string: 
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

# Print the character counts
for char, count in char_count.items():
    print(f"'{char}': {count}")
