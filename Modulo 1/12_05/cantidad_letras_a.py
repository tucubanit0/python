# Crea una función que cuente la cantidad de letras "a" en una cadena de texto.
def contar_letras_a(cadena):
    """
    Cuenta la cantidad de letras "a" en una cadena de texto.
    
    :param cadena: La cadena de texto a analizar.
    :return: Cantidad de letras "a" en la cadena.
    """
    return cadena.lower().count('a')

# Ejemplo de uso

texto = input("Ingrese una cadena de texto: ")
    
cantidad_a = contar_letras_a(texto)
print(f"La cantidad de letras 'a' en la cadena es: {cantidad_a}")