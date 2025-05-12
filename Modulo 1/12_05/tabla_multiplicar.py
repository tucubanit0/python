# Crea una función que genere la tabla de multiplicar de un número hasta un límite especificado.
def tabla_multiplicar(numero, limite):
    """
    Genera la tabla de multiplicar de un número hasta un límite especificado.
    
    :param numero: El número del cual se generará la tabla de multiplicar.
    :param limite: El límite hasta el cual se generará la tabla.
    :return: Lista con los resultados de la tabla de multiplicar.
    """
    return [numero * i for i in range(1, limite + 1)]

# Ejemplo de uso
numero = int(input("Ingrese el número para generar la tabla de multiplicar: "))
limite = int(input("Ingrese el límite para la tabla de multiplicar: "))
tabla = tabla_multiplicar(numero, limite)
print(f"Tabla de multiplicar del {numero} hasta {limite}:")
for i, resultado in enumerate(tabla, start=1):
    print(f"{numero} x {i} = {resultado}")