# Define una función llamada cuenta_vocales que tome un parámetro palabra y devuelva el número de vocales que contiene.
def cuenta_vocales(palabra):
    """
    Cuenta el número de vocales en una palabra.
    
    :param palabra: La palabra a analizar.
    :return: El número de vocales en la palabra.
    """
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

# Ejemplo de uso
palabra = input("Ingrese una palabra: ")
cantidad_vocales = cuenta_vocales(palabra)
print(f"La cantidad de vocales en la palabra '{palabra}' es: {cantidad_vocales}")