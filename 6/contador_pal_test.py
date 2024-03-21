import pytest
from contador_pal_6 import contar_palavras

def test_contar_palavras():
    texto = "Isso é um exemplo de texto para testar o contador de palavras."
    assert contar_palavras(texto) == 10

def test_contar_palavras_com_pontuacao():
    texto = "E se tivermos pontuação? Isso é um teste!"
    assert contar_palavras(texto) == 7

def test_contar_palavras_vazio():
    texto = ""
    assert contar_palavras(texto) == 0

def test_contar_palavras_com_numeros():
    texto = "123 456 789"
    assert contar_palavras(texto) == 3
