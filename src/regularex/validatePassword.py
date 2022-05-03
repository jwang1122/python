import re

"""
1. Should have at least one number.
2. Should have at least one uppercase and one lowercase character.
3. Should have at least one special symbol.
4. Should be between 6 to 20 characters long.
"""
def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
          
    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val
        
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
# compiling regex
regexPassword = re.compile(reg)

def validatePassword(password):
    ok = re.search(regexPassword, password)
    if ok: print("the password is valid.")
    else: print("invalid password!")

if __name__ == '__main__':
    pw1 = "Geek12@"
    validatePassword(pw1)
    pw2 = "wang"
    validatePassword(pw2)