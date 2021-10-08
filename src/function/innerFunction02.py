"""
Define functions in function, scope of attribute
https://www.javatpoint.com/python-decorator
"""
spam = "defined spam as a global variable"

def scope_test():
    def do_local():
        spam = "local spam" # local variable available only in this function
        print(f"Local variable: {spam}")

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam" # this is parent variable assignment

    def do_global():
        global spam
        spam = "global spam" # global variable assignment, will not change local variable

    spam = "test spam"  # local variable under scope_test() function
    print("Before do_local():",spam)
    do_local()
    print("After do_local() assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

if(__name__ == "__main__"):
    print(spam)
    scope_test()
    print("After do_global() call:", spam) # global variable