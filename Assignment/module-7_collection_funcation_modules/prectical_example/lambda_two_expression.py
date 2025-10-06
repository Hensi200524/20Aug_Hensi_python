"""Write a Python program to create a lambda function with two expressions."""
add = lambda x, y: (x + y, x * y)

result = add(3, 5)
print("The sum is:", result[0])
print("The product is:", result[1])