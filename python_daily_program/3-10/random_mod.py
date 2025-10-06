import random

#x=random.random()  #random float number between 0 and 1

#x = random.randint(1, 100)  #random integer number between 1 and 100

# x = random.randint(1111,9999) #random integer number between 1111 and 9999
# print(x)

captcha = ["1egc5", "2hgf6", "3dfg7", "4dfg8", "5dfg9"]
# x = random.choice(captcha)  #randomly select one value from the list
# print(x)

# x = random.shuffle(captcha)  #shuffle the list randomly
# print(captcha)

# x = random.sample(captcha, 2)  #randomly select 2 values from the list
# print(x)

x = random.choices(captcha, k=3)  #randomly select 3 values from the list with replacement
print(x)