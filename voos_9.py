class Voo:
    def __init__(self, origem, destino, data, hora, vagas):
        self.origem = origem
        self.destino = destino
        self.data = data
        self.hora = hora
        self.vagas = vagas

class SistemaDeReservas:
    def __init__(self):
        self.voos = []

    def adicionar_voo(self, voo):
        self.voos.append(voo)

    def pesquisar_voos(self, origem, destino, data):
        voos_disponiveis = []
        for voo in self.voos:
            if voo.origem == origem and voo.destino == destino and voo.data == data and voo.vagas > 0:
                voos_disponiveis.append(voo)
        return voos_disponiveis

    def fazer_reserva(self, voo):
        if voo.vagas > 0:
            voo.vagas -= 1
            return True
        else:
            return False

    def visualizar_reservas(self):
        for voo in self.voos:
            if voo.vagas < 50:  # Considerando que voos com menos de 50 vagas são reservados
                print(f"Origem: {voo.origem}, Destino: {voo.destino}, Data: {voo.data}, Hora: {voo.hora}")

    def cancelar_reserva(self, voo):
        voo.vagas += 1



if __name__ == "__main__":
    sistema = SistemaDeReservas()

    sistema.adicionar_voo(Voo("São Paulo", "Rio de Janeiro", "2024-03-25", "08:00", 100))
    sistema.adicionar_voo(Voo("Rio de Janeiro", "São Paulo", "2024-03-25", "10:00", 50))
    sistema.adicionar_voo(Voo("São Paulo", "Brasília", "2024-03-26", "12:00", 80))

    voos_disponiveis = sistema.pesquisar_voos("São Paulo", "Rio de Janeiro", "2024-03-25")
    print("Voos disponíveis de São Paulo para Rio de Janeiro em 2024-03-25:")
    for voo in voos_disponiveis:
        print(f"{voo.origem} -> {voo.destino}, Data: {voo.data}, Hora: {voo.hora}, Vagas disponíveis: {voo.vagas}")

    if sistema.fazer_reserva(voos_disponiveis[0]):
        print("Reserva realizada com sucesso!")
    else:
        print("Não há vagas disponíveis para este voo.")

    print("\nReservas:")
    sistema.visualizar_reservas()

    sistema.cancelar_reserva(voos_disponiveis[0])
    print("\nReserva cancelada.")

    print("\nReservas após cancelamento:")
    sistema.visualizar_reservas()
