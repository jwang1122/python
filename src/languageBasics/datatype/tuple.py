"""
tuple: A tuple is an ordered collection of Python objects that is iterable, 
immutable, separated by commas and surrounded by (). 圆数组 

t1 = (1, 2, 3, 4)
"""

# create tuple
t1 = () # create empty tuple
print(type(t1))
print(len(t1))

t1 = (1,2,3,4,5,'hello', (3,4,5), 3-5j)
print(len(t1))
print(t1)

t1 = tuple((i for i in range(100)))
print(t1)

student = ("John", "Wang","Male",11, 98)
print('the student %s %s is %s and %s years old, here is his/her grade %s for Math.' % student)

# tuple is iterable
for i in student:
    print(i)

# tuple slicing [start:stop:step], default start=0, stop=end, step=1
s1 = student[2:]
print(s1)

s1 = student[::-1] # reverse the tuple
print(s1)

# tuple operator *, +

t1 = (1, 2, 3)
t2 = (5, 6, 7)
t = t1 * 3
print(t)
t = t1 + t2 # append the second one to the first.
print(t)

# tuple is immutable (once you define a tuple, there is no way to make change)

# t1[0] = 3 #TypeError: 'tuple' object does not support item assignment

address=('123 main St.',)
print(type(address))

t = student[:3] + address + student[3:]
print(t)

t = student[:2] + ('Famale',) + student[3:]
print(t)

# tuple function: count()
t = (1,1,2,2,2,3,4,5,6,6,6,6)
print(t.count(6))

h = "hello, the world"
t = tuple(h) # using tuple() as function convert string to tuple
print(t)