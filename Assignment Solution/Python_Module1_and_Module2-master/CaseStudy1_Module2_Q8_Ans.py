# A website requires a user to input username and password to register.
# Write a program to check the validity of password given by user.
# Following are the criteria for checking password:
    # 1. At least 1 letter between [a-z]
    # 2. At least 1 number between [0-9]
    # 3. At least 1 letter between [A-Z]
    # 4. At least 1 character from [$#@]
    # 5. Minimum length of transaction password: 6
    # 6. Maximum length of transaction password: 12

import re #Reguler express for re.search
isPwdValid = 0
def validatePassword(pwd):
    while True:
        if(bool(re.search('[a-z]',pwd)))==False:
            isPwdValid = 0
            break
        elif(bool(re.search('[A-Z]',pwd)))==False:
            isPwdValid = 0
            break
        elif (bool(re.search('[0-9]', pwd))) == False:
            isPwdValid = 0
            break
        elif(bool(re.search('[$#@]',pwd))) == False:
            isPwdValid = 0
            break
        elif (len(pwd)<6):
            isPwdValid =0
            break
        elif (len(pwd)>12):
            isPwdValid=0
            break
        else:
            isPwdValid = 1
            return isPwdValid
            break

    if isPwdValid == 0:
        return isPwdValid

# pwd = input('Enter password:')
print validatePassword('p@$$w0rD')
