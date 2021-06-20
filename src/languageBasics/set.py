""" 
A Set is an unordered collection Python object that is iterable, 
mutable and has no duplicate elements, surrounded by {}. 

set1 = {1,2,3,4,5}
"""

# Creating two sets
set1 = set()
set2 = set()

# Adding elements to set1
for i in range(1, 6):
    set1.add(i)

# Adding elements to set2
for i in range(3, 8):
    set2.add(i)

print("Set1 = ", set1)
print("Set2 = ", set2)
print(len(set1))
print(len(set2))
print("\n")

# Union of set1 and set2
set3 = set1 | set2  # set1.union(set2)
print("Union of Set1 & Set2: Set3 = ", set3)

# Intersection of set1 and set2
set4 = set1 & set2  # set1.intersection(set2)
print("Intersection of Set1 & Set2: Set4 = ", set4)
print("\n")

# Checking relation between set3 and set4
if set3 > set4:  # set3.issuperset(set4)
    print("Set3 is superset of Set4")
elif set3 < set4:  # set3.issubset(set4)
    print("Set3 is subset of Set4")
else:  # set3 == set4
    print("Set3 is same as Set4")

# displaying relation between set4 and set3
if set4 < set3:  # set4.issubset(set3)
    print("Set4 is subset of Set3")
    print("\n")

# difference between set3 and set4
set5 = set3 - set4
print("Elements in Set3 and not in Set4: Set5 = ", set5)
print("\n")

# checkv if set4 and set5 are disjoint sets
if set4.isdisjoint(set5):
    print("Set4 and Set5 have nothing in common\n")

print(set5)
x = set5.pop()  # Remove and return an arbitrary set element.
print(x)
print(set5)
set5.remove(6)
print(set5)
set5.discard(6)

# Removing all the values of set5
set5.clear()

print("After applying clear on sets Set5: ")
print("Set5 = ", set5)

set5 = set([1, 2, 4, True, "hello", "world"])  # True is treated as 1
print(len(set5))
print(set5)

set5 = set([0, 2, 4, False, "hello", "world"])  # False is treated as 0
print(len(set5))
print(set5)

odds = set((1,3,5,7,9))
evens = set((2,4,6,8,10))
primes = set((2,3,5,7))
for o in odds: # set is iterable
    print(o)
print(odds)
print(evens.union(odds))
print(odds.union(evens))

print(odds.intersection(primes))
print(evens.intersection(primes))
print(evens.intersection(odds)) # empty set

print(2 in primes)
print(1 in evens)
print(9 not in evens) 