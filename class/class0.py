"""minimum class definition"""

class Robot:
    pass

if __name__ == "__main__":
    x = Robot()    # default factory to create a Robot instance
    y = Robot()
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


z = getattr(x,'energy')
