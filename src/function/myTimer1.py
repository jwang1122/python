def myTimer(original): # original is a function
    print(original.__name__)
    def wrapper(*args, **kargs):
        original(*args, **kargs)
    print("finished function call.")
    return wrapper

def displayInfo(name, age):
    print(f"displayInfo()... the arguments are name={name}, age={age}.")

if __name__ == '__main__':
    # displayInfo("John", 14)
    f = myTimer(displayInfo)
    print(type(f))
    f("John", 14) # do additional job without change original function
