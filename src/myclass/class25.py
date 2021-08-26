class OverrideEqual:
    def __eq__(self, other): 
        return True

if __name__ == '__main__':
    a = OverrideEqual()
    print(a==None)
    print(a is None) # always use 'is' or 'is not' operator to check None