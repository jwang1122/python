"""
Dictionaries are Python's implementation of a data structure 
that is more generally known as an associative array. 

A dictionary consists of a collection of key:value pairs. 
It is unordered, iterable, mutable, and each pair seperated by commas, 
surrounded by {}, and no duplicate key. The key:value pairs seperated by colon.

{'key1':1, 'key2':2}
"""

# create dictionary

d1 = {} # empty dictionary
print(type(d1))
print(len(d1))
print(d1) 

d2 = {'key1':1, 'key2':2}
print(d2)

# dict is iterable
for k in d2: # loop for dict only return key
    print(k, d2[k], sep=":::")

for value in d2.items():
    print(value)

# dict is mutable
d1["1"] = "Monday"
print(d1) 
d1[2] = "Tuesday"
print(d1) 

# get value by key from dict
print(d1[2])
print(d1.get("1"))

# dict cannot do slicing
# d2[:2] TypeError: unhashable type: 'slice'

# dict operator: **

d1 = {1:"one",2:"two"}
d2 = {2:'2', 3:'three'}
d3 = {**d2, **d1} # merge two dict to one dict
print(d3)

# dict functions: keys(), pop(), values(), items(), get(), ...

l1 = list(d3.keys())
print(l1)

print(d3)
value3 = d3.pop(3)
print(value3)
print(d3)

print(tuple(d3.values()))
print(list(d3.values()))
