"""
map 2 list to one
"""

def f1(x):
    return x*x

list1 = []
for i in range(1,11):
    y = f1(i)
    list1.append(y)
print(list1)

l1 = list(range(1,11))
l = list(map(lambda x: f1(x), l1))
print(l)

l = list(map(lambda x: x*x, l1))
print(l)

l2 = list(range(11,21))
l = list(map(lambda x,y:x*x+2*y, l1, l2))
print(type(l))
print(l)