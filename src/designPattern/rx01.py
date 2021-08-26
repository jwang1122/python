"""
1. use 'of' to create observable
2. subscribe observable
"""
from rx import of

source = of(1,2,3)
source.subscribe(
   on_next = lambda i: print("Got - {0}".format(i)),
   on_error = lambda e: print("Error : {0}".format(e)),
   on_completed = lambda: print("Job Done!"),
)