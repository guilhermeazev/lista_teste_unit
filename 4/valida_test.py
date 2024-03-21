import valida_email_4
import pytest
import re

def validar_email(email):
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return True
    else:
        return False

def test_email_valido():
    assert validar_email("usuario@example.com") == True
    assert validar_email("usuario123@example.com") == True
    assert validar_email("primeiro.ultimo@example.com") == True
    assert validar_email("primeiro-ultimo@example.com") == True
    assert validar_email("primeiro_ultimo@example.com") == True
    assert validar_email("primeiro.ultimo@subdominio.example.com") == True
    assert validar_email("primeiro-ultimo@subdominio.example.com") == True
    assert validar_email("primeiro_ultimo@subdominio.example.co.uk") == True

def test_email_invalido():
    assert validar_email("usuario@example") == False
    assert validar_email("usuario@example.") == False
    assert validar_email("@example.com") == False
    assert validar_email("usuario@.com") == False
    assert validar_email("usuario.example.com") == False
    assert validar_email("usuario") == False
    assert validar_email("usuario@-example.com") == False
    assert validar_email("usuario@exa_mple.com") == False
    assert validar_email("usuario@exa@mple.com") == False
    assert validar_email("usuario@exa..mple.com") == False
