"""
1. use 'create' to create observable
2. subscribe observable
"""
from rx import create

def create_observable(observer, scheduler):
   observer.on_next("Hello")
   observer.on_next("world")
   observer.on_completed()

source = create(create_observable) # source is observable

source.subscribe(
   on_next = lambda i: print("Received - {0}".format(i)),
   on_error = lambda e: print("Error Occurred: {0}".format(e)),
   on_completed = lambda: print("Done!"),
)