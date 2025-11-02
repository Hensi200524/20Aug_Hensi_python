import re

text = "Python is a powerful programming language"
word = input("Enter word to search: ")

if re.search(word, text):
    print("Word found in the string!")
else:
    print("Word not found!")
