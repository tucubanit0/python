# Mayor de tres números. Desarrolla un programa que lea tres números y determine cuál es el mayor de ellos.
""" a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))

mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c

print("El mayor número es:", mayor) """

# Suma de números pares. Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
""" suma = 0
for i in range(2, 101, 2):
    suma += i
print("La suma de los números pares del 1 al 100 es:", suma) """

# Números primos. Crea un programa que determine si un número ingresado por el usuario es primo o no.
""" num = int(input("Introduce un número: "))
es_primo = True

if num <= 1:
    es_primo = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break

if es_primo:
    print(num, "es un número primo.")
else:
    print(num, "no es un número primo.") """


# Números positivos y negativos. Escribe un programa que lea una lista de números y determine cuántos son positivos y cuántos son negativos.
""" numeros = [3, -1, 5, -7, 0, 8, -2]
positivos = 0
negativos = 0

for n in numeros:
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos) """

# Tabla de multiplicar. Desarrolla un programa que genere la tabla de multiplicar de un número ingresado por el usuario.
""" n = int(input("Introduce un número: "))
print(f"Tabla de multiplicar del {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}") """
    
# Promedio de una lista. Escribe un programa que calcule el promedio de una lista (los valores de la lista los has de escoger tú) de números.
""" numeros = [10, 20, 30, 40, 50]
promedio = sum(numeros) / len(numeros)
print("El promedio es:", promedio) """


# Tuplas como coordenadas. Crea un programa que lea las coordenadas (x, y) de varios puntos y los almacene en una lista de tuplas. Luego, muestra el contenido de la lista.
""" coordenadas = []
cantidad = int(input("¿Cuántos puntos quieres ingresar? "))

for i in range(cantidad):
    x = float(input(f"Introduce coordenada x del punto {i+1}: "))
    y = float(input(f"Introduce coordenada y del punto {i+1}: "))
    coordenadas.append((x, y))

print("Coordenadas ingresadas:", coordenadas) """

# Diccionario de estudiantes. 
# Crea un programa que permita ingresar el nombre y la edad de varios estudiantes, y luego muestra un diccionario donde las claves son los nombres y los valores son las edades.
""" estudiantes = {}
for _ in range(3):
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad del estudiante: "))
    estudiantes[nombre] = edad

print("Diccionario de estudiantes:", estudiantes) """

# Acceder a elementos de un array. Escribe un programa que declare un array de 5 elementos y muestra el valor del tercer elemento.
""" array = [5, 10, 15, 20, 25]
print("El tercer elemento del array es:", array[2]) """

# Ordenar una lista de manera ascendente. Desarrolla un programa que ordene una lista de números de forma ascendente y muestre el resultado.
""" lista = [8, 3, 1, 6, 7]
lista.sort()
print("Lista ordenada ascendentemente:", lista) """