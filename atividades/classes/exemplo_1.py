# precisa dizer que está herdando a classe object
class Pessoa(object):  
    def __init__(self, nome):
        self.nome = nome


class Pai(Pessoa):
    def __init__(self, nome, sobrenome):
        super().__init__(nome)
        self.sobrenome = sobrenome


class Mae(Pessoa):
    def __init__(self, nome, sobrenome):
        super().__init__(nome)
        self.sobrenome = sobrenome


class Filha(Pai, Mae):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)


def main():
    p = Pai('João', 'da Silva')
    m = Mae('Maria', 'Gonçalves')
    f = Filha('Júlia', p.sobrenome)


if __name__ == '__main__':
    main()


