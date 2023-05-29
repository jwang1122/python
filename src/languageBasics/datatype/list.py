"""
list: a list is an ordered collection of Python objects that is iterable,
mutable, separated by commans, surrounded by []. 方数组

l1 = [1,2,3,4,5]
"""

# create a list
l = [] # create an empty list
print(type(l))
print(len(l))

l = [1,2,3]
print(l)

l = list(range(1,100,2)) # odd number within 10
print(l)

l = [1,2,"hello", (1,2,3),[4,5,6]] # list can hold any python data
print(l)

suits = ("SPADES", "CLUBS", "DIAMONDS", "HEARTS")
faces = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
deck = [(face, suit) for face in faces for suit in suits]
print(deck)
print(len(deck))

# list is iterable
for i in l:
    print(i)

# list slicing

l = deck[:4]   # see string.py
print(l)

# list operator *, +

l = [1,2,3,3,3,2,1]
print(l*3)
l1 = [5,6,7]
print(l + l1)

# list is mutable, which means you can make change on the list
l[1] = 'hello'
print(l)
l.append('hello')
print(l)
l.insert(3, 100)
print(l)
print(l.count('hello')) # how many 'hello' in the list l?

l = [12,3,4,53,67,234,11]
l.sort(reverse=True)
print(l)

print(len(l))

t=(3,4,5,6,7)
print(t)
print(list(t))
s="hello"
print(list(s))