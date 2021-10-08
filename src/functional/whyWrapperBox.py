def neg(num):
    return -abs(num)

def display(name):
    print("hello", name) # return None

x = '10' # null pointer
y = str(neg(int(x)))
print(y)
# x + display("John")

myList = ['a','b','c','d','e', None]
myList.append('f')
print(myList)

myList = None # assign myList to None by accident
# myList.append('g')

# None = 5

# None.age = 5

def div(a, b):
    return a/b

x = div(5, 0) #ZeroDivisionError: division by zero
print(x)

