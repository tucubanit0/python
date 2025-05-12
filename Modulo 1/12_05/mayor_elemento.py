# Define una función llamada mayor_elemento que tome un parámetro lista y devuelva el elemento más grande de la lista.
def mayor_elemento(lista):
    """
    Encuentra el elemento más grande de una lista.
    
    :param lista: La lista de números a analizar.
    :return: El elemento más grande de la lista.
    """
    if not lista:
        return None  # Retorna None si la lista está vacía
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

# Ejemplo de uso
numeros = [3, 5, 1, 8, 2]
mayor = mayor_elemento(numeros)
print(f"El elemento más grande de la lista es: {mayor}")