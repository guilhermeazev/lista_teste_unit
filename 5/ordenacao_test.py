import pytest
from ordenacao_5 import ordenar_crescente, ordenar_decrescente

def test_ordenar_crescente():
    lista = [4, 2, 7, 1, 5]
    assert ordenar_crescente(lista) == [1, 2, 4, 5, 7]

def test_ordenar_decrescente():
    lista = [4, 2, 7, 1, 5]
    assert ordenar_decrescente(lista) == [7, 5, 4, 2, 1]
