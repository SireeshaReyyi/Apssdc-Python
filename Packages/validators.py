import re

# def phoneNumberValidator(number):
#     pattern = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$'
#     if re.match(pattern,str(number)):
#         return True
#     return False
# def emailValidator(mail):
#     pattern = '^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][0-9a-z]{3,15}[.][a-z]{2,4}$'
#     if re.match(pattern,mail):
#         return True
#     return False
def phoneNumberValidator(number):
    pattern = '^[6-9][0-9]{9}$|[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern,str(number)):
        return True
    else:
        return False

#phoneNumberValidation(8106410134)

def emailValidator(email):
    pattern = "^[0-9a-z][0-9a-z-.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
    if re.match(pattern,email):
        return True
    return False
#emailValidator("chaitanya@gmail.com")