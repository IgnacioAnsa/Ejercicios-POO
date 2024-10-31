# 3- Clase para representar una Calculadora Crear una clase Calculadora que pueda calcular
# suma, resta, multiplicación y división. Se debe crear la clase e implementarla.

class Calculadora:

    def __init__(self):

        pass

    def sumar(self, a, b):

        return a + b
    
    def restar(self, a, b):

        return a - b
    
    def multiplicacion(self, a, b):

        return a * b
    
    def division(self, a, b):

        if b != 0:
            return a // b
        
        else:
            return "error division por cero no permitida"

calculadora = Calculadora()

print(f"suma: {calculadora.sumar(3,4)}")
print(f"restar: {calculadora.restar(8,6)}")
print(f"multiplicacion: {calculadora.multiplicacion(2,7)}")
print(f"division: {calculadora.division(6,3)}")