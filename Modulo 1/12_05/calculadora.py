# Crea una calculadora que realice operaciones básicas (suma, resta, multiplicación y división) a partir de dos números ingresados por el usuario.
# La calculadora debe tener un menú que permita al usuario elegir la operación a realizar.

def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a ,b):
    if b == 0:
        return "Error: División por cero"
    else:
        return "Error: División por cero no permitida"
    
def menu():
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    menu()
    opcion = input("Ingrese el número de la operación: ")

    if opcion == '5':
        print("Saliendo de la calculadora. ¡Adiós!")
        break

    if opcion in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print(f"Resultado: {suma(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {resta(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {multiplicacion(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {division(num1, num2)}")
        except ValueError:
            print("Error: Por favor, ingrese valores numéricos válidos.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")