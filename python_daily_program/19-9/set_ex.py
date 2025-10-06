set_data = {'rajkot','morbi','jamnagar','surat','ahmedabad','rajkot'} # duplicate values are not allowed in set
print(set_data)

"""if "rajkot" in set_data: # case sensitive
    print("yes")
else:
    print("no")"""

"""print(len(set_data))"""

"""for i in set_data: # iterate through the set
    print(i)"""

# set_data.add('baroda') # add new item to set
# print(set_data)
# set_data.update(['delhi','mumbai']) # add multiple items to set
# print(set_data)

# set_data.remove('morbi') # remove item from set, if item not found then it will give error
# print(set_data)

# set_data.pop() # remove random item from set
# print(set_data)

# set_data.clear() # clear all items from set
# print(set_data)

# del set_data # delete the set
# print(set_data) # error because set is deleted

new_set = {'delhi','mumbai','rajkot'}
print(new_set) 

"""x = set_data.union(new_set) # union of two sets
print(x)"""

y = set_data.intersection(new_set) # intersection of two sets
print(y)