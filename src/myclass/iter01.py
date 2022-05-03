r = range(1, 10)
print(r) # r is iterable, implements __iter__()

print(iter(r)) # iter() function call __iter__() to be able to iterate all elements

x = iter(r) # x is iterator

a = next(x) # builtin next() function will call __next__() to return next element
b = next(x)
c = next(x) # call next() manually, raise StopIteration error once the iteration ends

print(a, b, c)

for i in x: # notice the i is not from 1, but 4 instead
    print(i)
