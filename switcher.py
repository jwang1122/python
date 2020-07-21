def zero(number):
    return "zero " + str(number)
 
def one(number):
    return "one " + str(number*2)
 
def two(number):
    return "two"
 
switcher = {0: zero,1: one,2: two}

def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    print(func())

if __name__ == '__main__':
    # print(type(switcher))
    f = switcher.get(1)    
    y = one(11)
    x = f(10) # one(10)
    print(x)
    # print(numbers_to_strings(2))
    # numbers_to_strings(1)
