import re

regexEmail = re.compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
def validateEmail(email):
    x = re.fullmatch(regexEmail, email)
    if x:
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is invalid.")

if __name__ == '__main__':
    email1 = "anonymous123@yahoo.co.uk"
    validateEmail(email1)
    email2 = "johnsnow@gmail"
    validateEmail(email2)