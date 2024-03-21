import pytest
from valida_senha_3 import validar_senha

def test_senha_curta():
    assert not validar_senha("abc12!")

def test_senha_sem_minuscula():
    assert not validar_senha("ABC123!")

def test_senha_sem_maiuscula():
    assert not validar_senha("abc123!")

def test_senha_sem_numero():
    assert not validar_senha("Abcdef!")

def test_senha_sem_caracter_especial():
    assert not validar_senha("Abc123")

def test_senha_segura():
    assert validar_senha("Abc123!@")
