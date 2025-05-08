# Resuelve los siguientes problemas sobre tipos de datos y variables, respondiendo a las cuestiones planteadas en los enunciados:
# 1.Crea una variable llamada "nombre" y asígnale tu nombre como valor. Luego, muestra por pantalla el contenido de la variable.
nombre = 'Javier'
print(nombre)

# 2. Calcula el área de un triángulo utilizando la fórmula A = (base * altura) / 2. 
# Crea las variables "base" y "altura" con valores enteros y muestra el resultado por pantalla.
base = 5
altura = 10
area = base * altura / 2
print('El área del triángulo es:', area)

# 3. Calcula el perímetro de un rectángulo utilizando la fórmula P = 2 * (lado1 + lado2). 
# Crea las variables "lado1" y "lado2" con valores enteros y muestra el resultado por pantalla.
lado1 = 4
lado2 = 6
perimetro = 2 * (lado1 + lado2)
print('El perímetro del rectángulo es:', perimetro)

# 4. Calcula el promedio de tres números enteros. 
# Crea las variables "num1", "num2" y "num3" con valores enteros y muestra el resultado por pantalla.
num1 = 7
num2 = 5
num3 = 9
promedio = (num1 + num2 + num3) / 3
print('El promedio de los tres números es:', promedio)

# 5 Realiza una concatenación de dos cadenas de texto y asigna el resultado a una variable llamada "concatenacion". 
# Luego, muestra el contenido de la variable por pantalla.
cadena1 = 'Hola'
cadena2 = 'Mundo'
concatenacion = cadena1 + ' ' + cadena2
print('La concatenación de las cadenas es:', concatenacion)

# 6. Escribe un programa que intercambie los valores de dos variables. 
# Crea las variables "a" y "b" con valores iniciales y muestra sus valores intercambiados por pantalla.
a = 10
b = 20
# a, b = b, a   # Esto hace lo mismo pero en solo una línea.
temp = a
a = b
b = temp
print('El valor de a es:', a)

# 7. Explica que hace el siguiente código:
numero_str = "42"
numero_int = int(numero_str)
print(numero_int)
print(type(numero_int))
# Este código convierte una cadena de texto que representa un número entero ("42") en un número entero real (42) utilizando la función int().
# Luego, imprime el número entero y su tipo de dato, que será <class 'int'>.

# 8. Explica que hace el siguiente código:
dividendo = 17
divisor = 4
resultado = dividendo // divisor
resto = dividendo % divisor
print("Resultado:", resultado)
print("Resto:", resto)
# Este código realiza una división entera entre el dividendo (17) y el divisor (4).
# La variable resultado almacena el cociente de la división entera (4), y la variable resto almacena el residuo de la división (1).
# Luego, imprime ambos resultados por pantalla.

# 9. Explica que hace el siguiente código:
decimal_str = "3.14"
decimal_float = float(decimal_str)
print(decimal_float)
print(type(decimal_float))
# Este código convierte una cadena de texto que representa un número decimal ("3.14") en un número decimal real (3.14) utilizando la función float().
# Luego, imprime el número decimal y su tipo de dato, que será <class 'float'>.

# 10. Explica que hace el siguiente código:
num1 = 8
num2 = 3
suma = num1 + num2
print(suma)
# Este código suma dos números enteros (8 y 3) y almacena el resultado en la variable suma. Luego, imprime el resultado de la suma (11) por pantalla.

# 11. Explica que hace el siguiente código:
resultado = None
print(resultado)
print(type(resultado))
# Este código asigna el valor None a la variable resultado, lo que indica que no tiene un valor definido. 
# Luego, imprime el valor de resultado (None) y su tipo de dato, que será <class 'NoneType'>.