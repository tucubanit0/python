# Crea una función que genere una lista de números pares en un rango específico.
def generar_lista_pares(inicio, fin):
    """
    Genera una lista de números pares en un rango específico.
    
    :param inicio: El inicio del rango (incluido).
    :param fin: El fin del rango (excluido).
    :return: Lista de números pares en el rango.
    """
    return [num for num in range(inicio, fin) if num % 2 == 0]

# Ejemplo de uso

inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el fin del rango: "))
    
lista_pares = generar_lista_pares(inicio, fin)
print(f"Lista de números pares entre {inicio} y {fin}: {lista_pares}")