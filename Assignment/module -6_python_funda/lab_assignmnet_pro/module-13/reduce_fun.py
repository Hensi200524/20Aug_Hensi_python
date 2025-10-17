from functools import reduce

# List of numbers
no = [1, 2, 3, 4, 5]

# Use reduce() to multiply all numbers
product = reduce(lambda a,b:a*b,no)

# Display result
print("List:", no)
print("Product:", product)
