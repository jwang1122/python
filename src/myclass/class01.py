"""
a Python class is for defining a particular type of 
object abstracted from real world.

Python classes define data to represent object state and 
functions used to change the state of an object.

1. class name
2. variable attributes
3. function attributes

the variable and function also indicate as object attribute of the class.

class <className>:
    pass
"""

# minimum class definition
class Robot(object):
    pass

def add(x, y):
    return x + y

def addInt2String(x, y):
    return str(x) + str(y)

if __name__ == "__main__":
    x = Robot()    # default factory to create a Robot instance
    y = Robot()
    print(type(x))
    print(id(x), id(y)) # take this as memory address, or unique object id

    t1 = (1,2,3) # tuple is immutable
    t2 = (1,2,3)
    print(id(t1), id(t2))

    l1 = [1,2,3] # list is mutable
    l2 = [1,2,3]
    print(id(l1), id(l2)) 

    obj1 = object() # object is the root class of all other class
    print(type(obj1))

    y2 = y         # assing an instance to a new instance
    print(y == y2) # compare 2 instances of Robot class
    print(y == x)

    x.name = "Marvin"     # dynamically add an instance level attribute to an instance
    x.build_year = "1979" # Binding attributes to objects is a general concept in Python. 
 
    y.name = "Caliban"
    y.build_year = "2018"
 
    print(x.name)
    print(y.build_year)

    Robot.brand = "GE"    # dynamically add a class level attribute to the Robot class
    print(x.brand)
    print(y.brand)

    print(x.__dict__)     # call built-in function defined in the Robot class
    print(Robot.__dict__)

    print(getattr(x, 'name','John')) # call built-in function __getAttribute__()


    z = getattr(x,'energy', 1000) # without default value, will raise Error
    print(z)

    z = getattr(x, 'energy', 100)
    print(z)

    x.energy = 120 # create new data attribute
    z1 = getattr(x, 'energy') # no need default value
    print(z1)

    r = Robot()
    r.add = add # dynamically assign a function to instance of Robot
    print(r.add(4,5))
    r.add = addInt2String
    print(r.add(3, "12"))
