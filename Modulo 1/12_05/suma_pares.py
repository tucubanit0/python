# Define una función llamada suma_pares que tome un parámetro n y devuelva la suma de todos los números pares menores o iguales a n.
def suma_pares(n):
    """
    Calcula la suma de todos los números pares menores o iguales a n.
    
    :param n: El número hasta el cual se sumarán los números pares.
    :return: La suma de los números pares menores o iguales a n.
    """
    return sum(num for num in range(2, n + 1, 2))

# Ejemplo de uso
n = int(input("Ingrese un número: "))
suma = suma_pares(n)
print(f"La suma de los números pares menores o iguales a {n} es: {suma}")