"""
define a class as default value
"""
class KeyNotFound: pass

if __name__ == '__main__':    
    my_dict = {'a':3, 'b':None}
    for key in ['a', 'b', 'c']:
        value = my_dict.get(key, KeyNotFound)
        if value is not KeyNotFound:
            print(f"{key}->{value}")