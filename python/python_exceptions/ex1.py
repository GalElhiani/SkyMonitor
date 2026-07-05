#this program demonstrates how a function takes a password as a string and
#checks if the password follows the rules:
#it must contain 8 letters at least
#it must contain at least one upper case letter
#it must contain at least one lowercase letter
#it must contain at least one of the following symbols: @, #, %, &
#Author: Gal Elhiani
#Tester: Ron Cohen

def IsStrongPass(string):
    '''this function checks password strength as explained in the comments above'''
    if len(string) < 8:
        raise ValueError("the password must contain at least 8 characters!")

    contains_upper = False
    contains_lower = False
    contains_special = False
    contains_digit = False
    special_char = ['@', '#', '%', '&']

    for c in string:
        if c.isupper():
            contains_upper = True
        elif c.islower():
            contains_lower = True    
        elif c in special_char:
            contains_special = True
        elif c.isdigit():
            contains_digit = True

    if not contains_lower:
        raise ValueError("the password must contain at least one lower case letter!")
    if not contains_upper:
        raise ValueError("the password must contain at least one upper case letter!")
    if not contains_digit:
        raise ValueError("the password must contain at least one digit!")
    if not contains_special:
        raise ValueError(f"the password must contain one of those special characters: {special_char}")
    # if not (contains_lower and contains_upper and contains_digit and contains_special):
    #     print("Password is invalid!")
    #     print("Your password must contain at least one upper case, one lower case, and a special character!")
    #     return False
    # else:
    print("Password is Valid!")
    return True



# invalid_password = "12345678"
valid_password = "123@Abp12"

# IsStrongPass(invalid_password)
IsStrongPass(valid_password)