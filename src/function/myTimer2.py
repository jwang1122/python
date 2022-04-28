import time

def myTimer(original): # original is a function
    print(original.__name__)
    def wrapper(*args, **kargs):
        start = time.time()
        result = original(*args, **kargs)
        end = time.time()
        print(f"{original.__name__} takes {(end-start):.3f} seconds.")
        return result
    return wrapper

def displayInfo(name, age):
    print(f"displayInfo()... the arguments are name={name}, age={age}.")
    time.sleep(2)
    return age

if __name__ == '__main__':
    # displayInfo("John", 14)
    # f = myTimer(displayInfo)
    # print(type(f))
    # result = f("John", 14) # do additional job without change original function
    result = myTimer(displayInfo)("David", 11)
    print(result)