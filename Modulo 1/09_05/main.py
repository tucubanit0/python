# main.py
import operaciones
from geometria.area import area_cuadrado, area_circulo
from geometria.perimetro import perimetro_cuadrado, perimetro_circulo
import matematicas

# Parte 1: Uso del módulo "operaciones"
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
print(f"Suma: {operaciones.suma(a, b)}")
print(f"Resta: {operaciones.resta(a, b)}")

# Parte 2: Uso del paquete "geometria"
lado_cuadrado = float(input("Ingrese la longitud del lado del cuadrado: "))
radio_circulo = float(input("Ingrese el radio del círculo: "))
print(f"Área del cuadrado: {area_cuadrado(lado_cuadrado)}")
print(f"Área del círculo: {area_circulo(radio_circulo)}")
print(f"Perímetro del cuadrado: {perimetro_cuadrado(lado_cuadrado)}")
print(f"Perímetro del círculo: {perimetro_circulo(radio_circulo)}")

# Parte 3: Uso del módulo "matematicas"
n = int(input("Ingrese un número para calcular su factorial: "))
try:
    print(f"Factorial de {n}: {matematicas.factorial(n)}")
except ValueError as e:
    print(e)
