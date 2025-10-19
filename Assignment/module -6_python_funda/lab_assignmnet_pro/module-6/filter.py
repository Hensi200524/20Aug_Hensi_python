# List of numbers
no = [1,2,3,4,5,6,7,8,9,10]

# Use filter() to keep only even numbers
even_numbers = list(filter(lambda x:x%2==0,no))

# Display result
print("Original list:", no)
print("Even numbers:", even_numbers)
