"""
Modifique a classe Veiculo do exercício anterior, de maneira que ela tenha um método imprime_informacoes,
que irá imprimir todos os atributos da instância na tela.
"""


class Veiculo(object):
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def imprime_informacoes(self):
        print(f'Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}')


def main():
    a = Veiculo('Ka', 2022, 'vermelho')
    b = Veiculo('Focus', 2017, 'branco')

    a.imprime_informacoes()
    b.imprime_informacoes()


if __name__ == '__main__':
    main()
