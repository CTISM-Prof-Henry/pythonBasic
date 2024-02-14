"""
Defina uma classe FormaGeometrica com um método calcular_area. Em seguida, crie as subclasses Quadrado,
Triangulo e Circulo , de maneira que elas implementem o método calcular_area de maneira diferente para
cada classe geométrica.
"""


class FormaGeometrica(object):
    def calcular_area(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado**2


class TrianguloRetangulo(FormaGeometrica):
    def __init__(self, cateto_oposto, cateto_adjacente, hipotenusa):
        self.cateto_oposto = cateto_oposto
        self.cateto_adjacente = cateto_adjacente
        self.hipotenusa = hipotenusa

    def calcular_area(self):
        return (self.cateto_oposto*self.cateto_adjacente)/2


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14*(self.raio**2)
