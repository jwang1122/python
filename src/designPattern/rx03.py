"""
1. use 'of' function to create observable
2. use 'pipe' function to add a series operators to the observable
3. subscribe observable
"""

from rx import range, operators as op

def onError(x):
    raise Exception ("data error")
observable1 = range(1,11)
observable2 = observable1.pipe(
   op.filter(lambda s: s%2==0),
   lambda x: onError(x),
   op.reduce(lambda x0, x1: x0 + x1)
)
observable2.subscribe(lambda x: print("Sum of Even numbers is {0}".format(x))) # 1st step: default on_next

observable2.subscribe(
    on_next = lambda i: print("Sum: {0}".format(i)),
    on_error = lambda e: print("Error : {0}".format(e)),
    on_completed = lambda: print("Done!"),
)