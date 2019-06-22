import re

def phoneNumberValidator(number):
    pettern = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}'
    if re.match(pettern,str(number)):
        return True
    return False
def emailValidator(mail):
    pattern = '^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][0-9a-z]{3,15}[.][a-z]{2,4}'
    if re.match(pattern,mail):
        return True
    return False
