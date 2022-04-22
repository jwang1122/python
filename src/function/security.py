employees = {'jwang':'password1', 'ethan':'password2', 'david':'password3', 'bob':'password4'}

def secure(original):
    def wrapper(*args, **kwargs):
        if username in employees and password==employees[username]:
            result = original(*args, **kwargs)
        else:
            result = 'Invalid user.'
        return result
    return wrapper

@secure
def add(x, y):
    return x + y

def login(loginUser, loginPass):
    global username
    global password
    username = loginUser
    password = loginPass

if __name__ == '__main__':
    loginUser = "jwang"
    login(loginUser, "password1")
    z = add(12, 54)
    print(z)