import pandas

data={
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}

print(data)
x = pandas.DataFrame(data)
print(x)