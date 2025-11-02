import re

text = "Python is a powerful programming language"
word = input("Enter word to match: ")

# match() checks only at the beginning
if re.match(word, text):
    print("Word matches at the beginning!")
else:
    print("No match at the beginning!")
