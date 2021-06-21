"""
A List is a ordered collection of Python objects that is iterable, 
mutable, separated by commas, surrounded by []. 方数组

l1 = [1,2,3,4,5]
"""

# Create a list
l1 = [] # empty list
l1 = [0,1,2,3,4,5,6,7,8,9,10]
print(l1)
print(type(l1))
print(len(l1))

# list Comprehension vs. For loop
l1 = [i for i in range(20) if i%2==1]
print(l1)

faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spade", "Club", "Diamond", "Heart"]
cards = [(face, suit) for face in faces for suit in suits]
print(cards)

l1=list(range(15))
print(l1)
l1 = [i for i in range(10)]
print(l1)


# list is iterable
for i in suits:
    print(i, end=':::')
print()

# list slicing (item in list is ordered)
l2 = l1[4:7]
print(l2)
l2 = l1[:4]
print(l2)
l2 = l1[4:]
print(l2)
l2 = l1[1:7:2]  # t[[start]:[end]:[step]
print(l2)
l2 = l1[::-1] # reverse the order 
print(l2)


# mixed datatype in a list
student1=[1234, 'Amy', "Huang", 13]
print("Student with ID:%d, first name '%s', last name '%s' is %d years old." %tuple(student1))
student1[3]=11
print("Student with ID:%d, first name '%s', last name '%s' is %d years old." %tuple(student1))

# list - Add, Delete and sort
myList = [6, 3, 1, 19, 10]
print(myList)
print(myList*2)
myList.append(11)
myList.extend([6,7,8])
myList.insert(3, 11)
myList.remove(11) # where 11 is the value of the element
v = myList.pop(2) # where 2 is index
print(v)
newList = sorted(myList)
print(newList)

# nested list
l = [[1,2],[3,4,5],[6,7,8,9]]
print(l)
print(len(l))
print(len(l[0]))

# Sample of using list and tuple
movies = [("Citizen Kane", 1941),("Spirited Away",2001),("It's a Wonderful Life",1946),("Gattaca",1997),("No Country for Old Men",2007),("Rear Window",1954),("The Lord of the Rings",2001),("Groundhog Day",1993),("Close Encounters of the Third Kind",1977),("The Royal Tenenbaums",2001),("The Aviator",2004),("Raiders of the Lost Ark",1981)]
before2000 = [(title, year) for (title, year) in movies if year<2000]
print("47:",before2000)

A = (1,3,5,7)
B = (2,4,6,8)
l1 = [(a,b) for a in A for b in B]
print(l1)
l1 = list(zip(A, B))
print(l1)
l1 = list(sum(x) for x in zip(A, B)) # where sum is built in function
print(l1)
print(*l1)