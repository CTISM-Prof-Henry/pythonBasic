"""
Crie uma classe chamada Veiculo que tenha atributos como modelo, ano e cor.
Crie duas instâncias dessa classe e imprima os atributos de cada uma.
"""


class Veiculo(object):
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor


def main():
    a = Veiculo('Ka', 2022, 'vermelho')
    b = Veiculo('Focus', 2017, 'branco')

    print(a.modelo, a.ano, a.cor)
    print(b.modelo, b.ano, b.cor)


if __name__ == '__main__':
    main()
