# Crea una función que verifique si una palabra es un palíndromo (se lee igual de izquierda a derecha y viceversa).
def es_palindromo(palabra):
    """
    Verifica si una palabra es un palíndromo.
    
    :param palabra: La palabra a verificar.
    :return: True si la palabra es un palíndromo, False en caso contrario.
    """
    # Convertir la palabra a minúsculas y eliminar espacios
    palabra = palabra.replace(" ", "").lower()
    
    # Comparar la palabra con su reverso
    return palabra == palabra[::-1]

# Ejemplo de uso

palabra = input("Ingrese una palabra: ")
    
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")