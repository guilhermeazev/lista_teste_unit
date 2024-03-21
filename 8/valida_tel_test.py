import re
import pytest

def validar_telefone(telefone):
    padrao = r'^\([1-9]{2}\) [2-9][0-9]{3,4}-[0-9]{4}$'
    return re.match(padrao, telefone) is not None

def test_telefone_valido():
    assert validar_telefone("(11) 91234-5678") == True
    assert validar_telefone("(31) 99876-5432") == True
    assert validar_telefone("(85) 9876-5432") == True

def test_telefone_invalido():
    assert validar_telefone("11 91234-5678") == False
    assert validar_telefone("(11) 1234-5678") == False
    assert validar_telefone("(11) 912345678") == False
    assert validar_telefone("(011) 91234-5678") == False
    assert validar_telefone("(11) 91234-56789") == False
    assert validar_telefone("(11) 91234-567") == False
    assert validar_telefone("(11) 9123-5678") == False
    assert validar_telefone("(11) 91234-567a") == False
