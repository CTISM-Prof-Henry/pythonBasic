
class Objeto:
    def __init__(self, largura, altura, comprimento, peso):
        """Construtor da classe Objeto"""
        self.largura = largura
        self.altura = altura
        self.comprimento = comprimento
        self.peso = peso

    def __str__(self):
        return f'Peso: {self.peso}' + \
            f'A/L/C: {self.altura}/{self.largura}/{self.comprimento}'


class Animal(Objeto):
    pass


caixa = Objeto(largura=10, altura=5, comprimento=3, peso=5)
print(caixa)
