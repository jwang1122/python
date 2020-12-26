# initial empty list
l = []
print(type(l))

l = [1,2,3,4,5]
print(l)

l=list(range(10))
print(l)

l = list(filter(lambda x: x%2==0, range(20)))
print(l)

l1 = [i for i in range(20) if i%2==1]
print(l1)

l1 = [i*4 for i in range(10)]
print(l1)

l1 = [i*3+j**2 for i in range(5) for j in range(3)]
print(l1)

A = (1,3,5,7)
B = (2,4,6,8)
l1 = [(a,b) for a in A for b in B]
print(l1)

l = [False]*6 # create a default boolean list
print(l)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(f"The number of apples is {fruits.count('apple')}.")
print(f"The number of tangerine is {fruits.count('tangerine')}.")
print(f"The index of banana is {fruits.index('banana')}.")
print(f"The index of next banana is {fruits.index('banana', 4)}.")
fruits.reverse() # reverse function does NOT return anything
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())
print(fruits)

# modify list
l[4] = "hello"
print(l)
l = l[3:7]
print(l)
l.append(20)
print(l)
l.insert(0, "First")
print(l)
l.append(l1) # list in list
print(l)

faces = ('A', "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("SPADES", "CLUBS", "DIAMONDS", "HEARTS")
cards = [(face, suit) for suit in suits for face in faces]
print(cards)
print(len(cards))

a = (1,2,3)
b = (4,5,6)
c = list(zip(a, b))
print(c)