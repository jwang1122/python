"""
set: a set is an unordered collection of immutable Python objects that is iterable,
mutable, separated by commans, surrounded by {}, and has no duplicated elements. 集合

set1 = {1,3,5,7,9} odd number < 10
"""

# create set
set1 = set() # empty set
print(type(set1)) # <class 'set'>
print(len(set1))

l = [3,4,5]
set1 = {1,2,4,5,5,6,7,8,5,8,'hello',(3,4),3.123, 3-5j} # in set there is no duplicate elements.
print(set1)

# set is iterable
for item in set1:
    print(item)

# set is mutable
set1.remove(5)
print(set1)
set1.add(10) # dot operator
print(set1)
set1.add(10) # no duplication
print(set1)

# set cannot be sliced
# set2 = set1[3:5] TypeError: 'set' object is not subscriptable

# set Operators: &, |, >, <, ==
set1 = {1,3,5,7,9}
set2 = {2,4,6,8, 9,5}
set3 = set1 | set2 # union operator add all elements in both set
print(set3)
set4 = set1 & set2 # intersection operator get common elements in both set
print(set4)
print(set4<set2) # set4 is subset of set2
print(set4>set2)
print(set1>set2)
print(set2>set1)
print(set1==set2)
set5 = {5,9}
print(set4==set5)

## set function: remove(), add(), difference()
set1.remove(9)
print(set1)
set1.add(9)
print(set1)
set6 = set1.difference(set2)
print(set6)
set7 = set2.difference(set1)
print(set7)
print(len(set7))

# use set() as a function to convert other type to set
t1 = (1,2,3,4,4,4,4,3,3)
set8 = set(t1)
print(set8)

l1 = [1,2,3,4,4,4,4,3,3, 6,7,8,8,8]
set9 = set(l1)
print(set9)

print("Done.")
