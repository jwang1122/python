"""
__repr__ 
__str__ 
__len__
"""

class A:
    def __repr__(self):
        return "John"

    def __str__(self):  # comments out this function see what happens
        return 'Wang'
    
    def __len__(self):
        return 5

if __name__ == '__main__':
    a = A()
    print(a) # use __str__ for readable
    print(repr(a)) # use __repr__ for unambiguous
    print(str(a)) # call __str__()
    print(len(a)) # call __len__()