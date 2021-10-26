"""
1. positional arguments: a, b
2. c, d can be positional or keyword argument.
3. keyword argument: e, f
4. / separate positional only arguments from others
5. * separate keywords only arguments from others
6. when you define a keyword-only arguments without default value, then call the function 
   without keyword argument, it cause TypeError.
7. call function provide keyword argument values, the function will use whatever you provided.
8. you can miss any keyword arguments while you call the function, 
   as long as the function defined a default value.
9. the order of keyword arguments is not important.
10. the order of positional arguments is very important.
11. positional arguments always before keyword arguments.
"""
def f(a, b, /, c, d, *, e=4, f=1000): # keyword-only arguments with default values
    print(a, b, c, d, e, f)

def f1(a, b, c, d): # all arguments can be positional or keyword arbuments.
    print(a, b, c, d)

f(2, 4, "c", "d", e=2, f="hello") # pass all arguments
#f(2, 4, "c", "d", 2, "Hello") # TypeError: f() takes 4 positional arguments but 6 were given
#f(2, 4, "c", "d") # TypeError: f() missing 2 required keyword-only arguments: 'e' and 'f'
f(2, 4, "c", "d") # TypeError: f() missing 2 required keyword-only arguments: 'e' and 'f' if there is no default value
f(2, 4, "c", "d", e="Hello", f="world")# use whatever you provide
f(2, 4, "c", "d", f="world", e="Hello")
f(2, 4, "c", "d", f="world")
f(2, 4, c="John", d="Wang") # use c and d as keyword arguments
f(2, 4, d="Wang", c="John")
f(2, 4, 12, e=10, d=13)
f(4, 2, 12, e=10, d=13)
#f(4, b=2, c="John", d="Wang") # TypeError: f() got some positional-only arguments passed as keyword arguments: 'b'

f1(12, c=1, b=2, d=4)
f1(1,2,3,4)
f1(a=1, c=3, b=2, d=4)
