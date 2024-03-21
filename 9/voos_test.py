import pytest
from voos_9 import SistemaReservas

@pytest.fixture
def sistema_reservas():
    sistema = SistemaReservas()
    sistema.adicionar_voo({'id': 1, 'origem': 'A', 'destino': 'B', 'assentos_disponiveis': 2})
    sistema.adicionar_voo({'id': 2, 'origem': 'B', 'destino': 'C', 'assentos_disponiveis': 1})
    return sistema

def test_pesquisar_voos(sistema_reservas):
    voos_encontrados = sistema_reservas.pesquisar_voos('A', 'B')
    assert len(voos_encontrados) == 1
    assert voos_encontrados[0]['origem'] == 'A'
    assert voos_encontrados[0]['destino'] == 'B'

def test_fazer_reserva(sistema_reservas):
    assert sistema_reservas.fazer_reserva(1, 'A1')
    assert not sistema_reservas.fazer_reserva(1, 'A2')  # Todos os assentos reservados
    assert not sistema_reservas.fazer_reserva(3, 'A1')  # Voo inexistente

def test_visualizar_reservas(sistema_reservas):
    sistema_reservas.fazer_reserva(1, 'A1')
    sistema_reservas.fazer_reserva(2, 'B1')
    reservas = sistema_reservas.visualizar_reservas()
    assert len(reservas) == 2

def test_cancelar_reserva(sistema_reservas):
    sistema_reservas.fazer_reserva(1, 'A1')
    assert sistema_reservas.cancelar_reserva(1)
    assert not sistema_reservas.cancelar_reserva(1)  # Reserva inexistente
