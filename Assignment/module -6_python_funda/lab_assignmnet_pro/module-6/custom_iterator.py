class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

# List of integers
numbers = [1, 2, 3, 4, 5]

# Using the custom iterator
it = MyIterator(numbers)

for num in it:
    print(num)
