
class ConversorDeMoedas:
    def __init__(self, taxa_dolar_euro, taxa_real_dolar):
        self.taxa_dolar_euro = taxa_dolar_euro
        self.taxa_real_dolar = taxa_real_dolar

    def dolar_para_euro(self, valor_em_dolar):
        return valor_em_dolar * self.taxa_dolar_euro

    def real_para_dolar(self, valor_em_real):
        return valor_em_real / self.taxa_real_dolar