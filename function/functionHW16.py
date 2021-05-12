def isValid(password):
    def numDigits():
        count = 0;
        for c in password:
            if c.isnumeric():
                count += 1
        return count

    if len(password)<8:
        return False
    if not password.isalnum():
        return False
    if numDigits() < 2:
        return False
    return True

password = input("Enter a number: ")
if isValid(password):
    print(f"The password '{password}' is valid.")
else:
    print(f"The password '{password}' is NOT valid.")
