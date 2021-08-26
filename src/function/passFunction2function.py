"""
pass a function to another function
"""
def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def ff(f, x, y):
    return f(x, y)

def inner1():
    print("this is a inner1() function.")
def inner2():
    print("this is a inner2() function.")

def outer(function):
    function()


def shout(text): 
    return text.upper() 
    
def whisper(text): 
    return text.lower() 
    
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function passed as an argument.") 
    print(greeting)  
    
if __name__ == '__main__':
    x = ff(mul, 6, 4) # 中央决定GDP一年翻两翻（ff），中央不确定各个省如何办到
    print(x)

    outer(inner1) # one outer function can run different function
    outer(inner2) # choose different function to run at runtime (treat different user differently)

    if x > 20:
        greet(shout) 
    else:
        greet(whisper) 
