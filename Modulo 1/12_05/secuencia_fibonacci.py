# Crea una función que genere los primeros términos de la secuencia Fibonacci.
def fibonacci(n):
    """
    Genera los primeros n términos de la secuencia Fibonacci.
    
    :param n: Número de términos a generar.
    :return: Lista con los primeros n términos de la secuencia Fibonacci.
    """
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

# Ejemplo de uso
n = int(input("Ingrese el número de términos de la secuencia Fibonacci: "))
secuencia_fibonacci = fibonacci(n)
print(f"Los primeros {n} términos de la secuencia Fibonacci son: {secuencia_fibonacci}")