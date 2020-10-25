# function names can be attributed. re
def f(x):
    f.count = getattr(f, 'count', 0) + 1
    return 'Returned message: Dynamically add attribute to a function'

z = f("Hello")
print(z)

for i in range(10):
    f(i)

print("The number of calls to the function:",f.count)
