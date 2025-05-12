# Crea una función que genere una lista de números primos en un rango específico.
def es_primo(num):
    """
    Verifica si un número es primo.
    
    :param num: El número a verificar.
    :return: True si el número es primo, False en caso contrario.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generar_lista_primos(inicio, fin):
    """
    Genera una lista de números primos en un rango específico.
    
    :param inicio: El inicio del rango (incluido).
    :param fin: El fin del rango (excluido).
    :return: Lista de números primos en el rango.
    """
    return [num for num in range(inicio, fin) if es_primo(num)]

# Ejemplo de uso
inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el fin del rango: "))
lista_primos = generar_lista_primos(inicio, fin)
print(f"Lista de números primos entre {inicio} y {fin}: {lista_primos}")
