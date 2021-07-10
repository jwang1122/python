def isFloat(number):
    try:
        x = float(number) # raise Error
        return True
    except Exception as error:
        print(error)
        return False

if __name__ == '__main__':
    x = input("enter a number: ")
    if isFloat(x):
        x = float(x)
        print(x * 2)
    print("Done")