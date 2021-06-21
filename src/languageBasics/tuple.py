"""
A Tuple is a ordered collection of Python objects that is iterable, 
immutable, separated by commas surrounded by ()。圆数组

t1 = (1,2,3,4,5)
"""
# Create a tuple
t = ()  # empty tuple
t = tuple()
t = (1,2,3,4,5,6,3,4,5,)
print(t)
print(type(t))
print(len(t))
t = 1,2,3,4,"John","Terry"
print(t)
print(type(t))

t1 = tuple(i for i in range(10))
print(t1)

faces = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("Spade", "Club", "Diamond", "Heart")

# nested tuple
t1 = ((1,2), (3,4))
cards = tuple((face, suit) for face in faces for suit in suits)
print(cards)

# tuple is iterable
for item in t:
    print(item, end=", ")
print()

# tuple slicing (item in tuple is ordered)
t1 = t[4:7]
print(t1)
t1 = t[:4]
print(t1)
t1 = t[4:]
print(t1)
t1 = t[1:7:2]  # t[[start]:[end]:[step]
print(t1)
t1 = t[::-1] # reverse the order 
print(t1)

# tuple can hold different data type data
student = ("Amy", "Huang", 13)
print("Student %s %s is %d years old." %student)
point = (4, 5)
line = ((2, 3), (5, 6))
print(line)
square = ((2, 2), (2, 12), (12, 12), (12, 2))
print(square)
card = ("2", "Heart")
temperaturs = (("Houston", 92, "2021-06-20"), ("New York", 89))

# tuple is immutable (cannot be changed)
# t.append(4)
# t[4]=9

# tuple operator +, *
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t = t1 + t2
print(t)

t = t1 * 2
print(t)

# tuple rebuild: slicing and +
t1 = (1, 2, 3, 4, 5, 6)
t2 = ("a", "b", "c", "d")
t = (9, 8, 7) + t1[2:4] + t2[1:3]
print(t)

# sort tuple
t = (3, 2, 5, 6, 11, 21, 3, 9)
print(t)
t1 = sorted(t) # built in function, return sorted tuple
print(t1)

