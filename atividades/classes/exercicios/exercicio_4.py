"""
Crie duas superclasses: Veiculo e MeioDeTransporte, cada uma com métodos e atributos distintos.
Em seguida, crie uma subclasse Carro que tem como superclasse Veiculo e MeioDeTransporte.
"""


class Veiculo(object):
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def imprime_informacoes(self):
        print(f'Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}')


class MeioDeTransporte(object):
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.carregando = 0

    def carrega(self, passageiros):
        if (self.capacidade - self.carregando) >= passageiros:
            self.carregando += passageiros
        else:
            print('não consigo carregar mais passageiros!')


class Carro(Veiculo, MeioDeTransporte):
    def __init__(self, modelo, ano, cor, capacidade):
        super().__init__(modelo, ano, cor)
        self.capacidade = capacidade

    def imprime_informacoes(self):
        print(f'Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Capacidade: {self.capacidade}')


a = Carro('Ka', 2022, 'vermelho', 5)
a.imprime_informacoes()
