"""
r = map(function, sequence)
map 2 list to one
"""
l1 = list(range(1,11))
l2 = list(range(11,21))
l = list(map(lambda x,y:x*x+2*y-3, l1, l2))
print(type(l))
print(l)

# l = list(map(lambda s: s[::-1], ["cat", "dog", 3.14159, "gecko"]))
l = list(map(lambda s: str(s)[::-1], ["cat", "dog", 3.14159, "gecko"]))
print(l)

s = "+".join(map(str, [1,2,3,4,5]))
print(s)