# 2 - Clase para representar un Rectángulo Crear una clase rectángulo que tenga las
# características base y altura. Del rectángulo se debe poder calcular el área y el perímetro.
# Se debe crear la clase e implementarla.

class Rectangulo:

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura

    def calcular_area(self):

        return self.base * self.altura
    
    def calcular_perimetro(self):

        return 2 * (self.base + self.altura)
    
rectangulo = Rectangulo(20,10)

print(f"área: {rectangulo.calcular_area()}")
print(f"perimetro: {rectangulo.calcular_perimetro()}")
