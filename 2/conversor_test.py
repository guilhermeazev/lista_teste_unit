import pytest
from conversor_moedas_2 import ConversorDeMoedas

@pytest.fixture
def conversor():
    return ConversorDeMoedas(0.85, 5.0)

def test_dolar_para_euro(conversor):
    assert round(conversor.dolar_para_euro(100), 2) == 85.00
    assert round(conversor.dolar_para_euro(200), 2) == 170.00

def test_real_para_dolar(conversor):
    assert conversor.real_para_dolar(100) == 20.0
    assert conversor.real_para_dolar(500) == 100.0
