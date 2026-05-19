import re
password=input('Enter the password : ')
containsCapsAndSmall = re.compile(r'[a-zA-Z]+')
containsDigits = re.compile(r'\d')
if len(password) >= 8:
    if len(containsCapsAndSmall.findall(password)) != 0:
        if len(containsDigits.findall(password)) != 0:
            print("Password save it is following all rules")
        else:
            print("It should contain %s at least one digit" %(password))

    else:
        print(f"given password does not have both upper and lower case letters {password}")
    
else:
    print(f" given password length is less than 8 which should be atleast 8 {password}")

