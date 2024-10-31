# 5- Encapsulamiento Crear una clase Cuenta Bancaria que tenga las características titular y
# saldo encapsulado. De la cuenta bancaria se puede obtener el saldo, depositar o retirar (en
# cada caso imprimir que fue exitoso). Se debe crear la clase e implementarla.

class Cuenta_Bancaria:

    def __init__(self, titular, saldo):

        self.titular = titular
        self.__saldo = saldo

    def obtener_saldo(self):

        return self.__saldo
    
    def depositar(self, monto):

        if monto > 0:
            
            self.__saldo += monto
            print(f"deposito exitoso. nuevo deposito {self.__saldo}")
        else:
            return "el monto debe ser positivo"
        
    def retirar(self, monto):

        if monto > 0 and monto <= self.__saldo:
            
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")

        elif monto > self.__saldo:

            return "fondos insuficientes"
        
        else:
            return "el monto debe ser positivo"
        

cuenta = Cuenta_Bancaria("juan", 5000000)

print(f"saldo inicial: {cuenta.obtener_saldo()}")

cuenta.depositar(100000)
cuenta.retirar(200000)




