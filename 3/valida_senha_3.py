import re

def verificar_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search("[a-z]", senha):
        return False
    if not re.search("[A-Z]", senha):
        return False
    if not re.search("[0-9]", senha):
        return False
    if not re.search("[!@#$%^&*()_+{}:<>?]", senha):
        return False
    return True