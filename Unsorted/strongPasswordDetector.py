import re

print("Enter Your Password")
password = input()

while True:
    if re.compile(r'[A-Z]').search(password) == None:
        print("Password is not Strong")
        break
    elif re.compile(r'[a-z]').search(password) == None:
        print("Password is not Strong")
        break
    elif re.compile(r'[0-9]').search(password) == None:
        print("Password is not Strong")
        break
    elif re.compile(r'[!@#$%&]').search(password) == None:
        print("Password is not Strong")
        break
    else:
        print("Password is strong enough") 
        break
    
        



