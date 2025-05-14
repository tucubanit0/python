# Crea una clase llamada CuentaBancaria que represente una cuenta bancaria con un saldo y métodos para depositar y retirar dinero. 
# La clase debe tener un método para imprimir el saldo actual.

class CuentaBancaria:
    def __init__(self, saldo=600):
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def imprimir_saldo(self):
        print(f"Saldo actual: {self.saldo}")

def menu():
    print("\nSeleccione la operación que desea realizar:")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

cuenta = CuentaBancaria()

while True:
    menu()
    opcion = input("Ingrese el número de la operación: ")

    if opcion == '1':
        cuenta.imprimir_saldo()
    elif opcion == '2':
        try:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
    elif opcion == '3':
        try:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
    elif opcion == '4':
        print("Saliendo. ¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")