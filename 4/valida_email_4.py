import re

def validar_email(email):
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return True
    else:
        return False