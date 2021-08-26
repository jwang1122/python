"""
Create a subject
"""
from rx.subject import Subject
from rx import operators as op

subject1 = Subject() 

def checkNumber(x):
    if type(x) not in [int, float]:
        raise Exception("data error")
    return x

def processor(x):
    print(f"the value is {x}")

sub = subject1.pipe(
    op.map(lambda x: checkNumber(x))
)
sub.subscribe( # define function
    on_next = processor,
    on_error = lambda e: print(f"Error: {e}.")
)

# subject1.subscribe( # define function
#     on_next = lambda x: print(f"different handler for value {x}"),
#     on_error = lambda e: print(f"Error: {e}.")
# )

subject1.on_next(1)
subject1.on_next(2)
subject1.on_next("Hello") # pass data later
subject1.on_next("World")


