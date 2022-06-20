import time

def myTimer(original): # original is a function
    print(original.__name__)
    def wrapper(*args, **kargs):
        start = time.time() 
        result = original(*args, **kargs)
        diff = time.time() - start
        print(f"{original.__name__} takes {diff:.2f} seconds.")
        return result
    return wrapper

@myTimer
def displayInfo(name, age):
    print(f"displayInfo()... the arguments are name={name}, age={age}.")
    time.sleep(2)
    return age

if __name__ == '__main__':
    age = displayInfo("John", 14)
    print(age)
    # f = myTimer(displayInfo) # looks like a function decorator
    # print(type(f))
    # f("John", 14) # do additional job without change original function