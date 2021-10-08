"""
zip tuple
"""
v1 = (10, 20, 30)
v2 = (7, 5, 3)
l = list(zip(v1, v2))
print(l)
z = sum(x * y for x, y in zip(v1, v2))  # dot product
print(z)

l1 = [1,2,3]
l2 = [4,5,6]
t = tuple(zip(l1, l2))
print(t)