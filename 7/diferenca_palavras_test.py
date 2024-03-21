import pytest
from diferenca_pala_7 import diferenca_entre_datas

def test_diferenca_entre_datas():
    data1 = '2022-03-10 12:00:00'
    data2 = '2022-03-15 14:30:00'
    diferenca_esperada = {
        'dias': 5,
        'meses': 0,
        'anos': 0,
        'horas': 126,
        'minutos': 7560
    }
    assert diferenca_entre_datas(data1, data2) == diferenca_esperada

def test_diferenca_entre_datas_2():
    data1 = '2022-03-10 12:00:00'
    data2 = '2023-03-15 14:30:00'
    diferenca_esperada = {
        'dias': 370,
        'meses': 12,
        'anos': 1,
        'horas': 8886,
        'minutos': 533160
    }
    assert diferenca_entre_datas(data1, data2) == diferenca_esperada
