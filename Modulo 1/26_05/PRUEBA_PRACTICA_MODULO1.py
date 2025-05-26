# Crea una variable llamada pi y asígnale el valor 3.14. Luego, crea una variable llamada radio y asígnale el valor 5. 
# Finalmente, crea una variable llamada área y asígnale el resultado de multiplicar pi por el cuadrado de radio. 
# Imprime el valor de área en la pantalla.
""" pi = 3.14
radio = 5
area = pi * (radio ** 2)
print(area) """

# Crea una variable llamada x y asígnale el valor 10. Luego, crea una variable llamada y y asígnale el valor 2. 
# Finalmente, crea una variable llamada z y asígnale el resultado de dividir x entre y. 
# Imprime el valor de z en la pantalla incluyendo números decimales en el resultado.
""" x = 10
y = 2
z = x / y
print(z) """

# Crea una variable llamada celsius y asígnale un valor numérico. Luego, crea una variable llamada fahrenheit y 
# asígnale el resultado de convertir la temperatura de Celsius a Fahrenheit utilizando la fórmula: (celsius * 9/5) + 32. 
# Finalmente, imprime el valor de fahrenheit en la pantalla.
""" celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit) """

#  Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
""" suma = 0
for i in range(1, 101):
    if i % 2 == 0:
        suma += i
print(suma) """

# Crea un programa que permita ingresar el nombre y la edad de varios estudiantes, y luego muestra 
# un diccionario donde las claves son las edades y los valores son los nombres.
""" estudiantes = {}
while True:
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    edad = input("Ingrese la edad del estudiante: ")
    estudiantes[edad] = nombre
print(estudiantes) """

# Se nos pide que introduzcamos la nota de un alumno, admitiendo decimales, y se nos devuelva la calificación en texto obtenida, siguiendo el siguiente esquema:
# < 5 Insuficiente
# < 6 Suficiente
# < 7 Bien
# < 9 Notable
# < 10 Sobresaliente
""" nota = float(input('Introduce la nota del alumno:)'))
if nota < 5:
    calificacion = 'Insuficiente'
elif nota <6:
    calificacion = 'Suficiente'
elif nota <7:
    calificacion = 'Bien'
elif nota <9:
    calificacion = 'Notable'
elif nota <=10:
    calificacion = 'Sobresaliente'
else:
    calificacion = 'Nota no valida'
print(f'La calificación del alumno es: {calificacion}') """

# Crear una clase "CuentaBancaria" que represente una cuenta bancaria con atributos como número de cuenta, saldo, titular e IBAN, 
# y métodos para realizar ingresos y retiradas de fondos.
""" class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, iban):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.iban = iban
        self.saldo = 0.0

    def ingreso(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Ingreso de {cantidad:.2f} realizado. Nuevo saldo: {self.saldo:.2f}")
        else:
            print("La cantidad a ingresar debe ser positiva.")

    def retirada(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retirada de {cantidad:.2f} realizada. Nuevo saldo: {self.saldo:.2f}")
        else:
            print("Cantidad a retirar no válida o saldo insuficiente.")
# Ejemplo de uso
cuenta = CuentaBancaria("123456789", "Juan Pérez", "ES7620770024003102575766")
cuenta.ingreso(500)
cuenta.retirada(200)
cuenta.retirada(1000) """

# Crea una clase llamada Persona que represente a una persona con nombre, apellidos, sexo y edad. 
# La clase debe tener métodos para obtener y establecer el nombre y la edad, 
# así como un método para calcular el año de nacimiento.
""" class Persona:
    def __init__(self, nombre, apellidos, sexo, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, nueva_edad):
        self.edad = nueva_edad

    def calcular_anio_nacimiento(self, anio_actual):
        return anio_actual - self.edad
# Ejemplo de uso
persona = Persona("Ana", "Gómez", "Femenino", 30)
print(f"Nombre: {persona.obtener_nombre()}")
print(f"Edad: {persona.obtener_edad()}")
persona.establecer_nombre("María")
print(f"Nuevo nombre: {persona.obtener_nombre()}")
anio_actual = 2025
print(f"Año de nacimiento: {persona.calcular_anio_nacimiento(anio_actual)}") """

# Crear una clase base "Figura" con un método para calcular el área, y luego crear 
# clases derivadas como "Triangulo" y "cuadrado" que hereden de "Figura" y sobrescriban 
# el método para calcular el área según la forma geométrica.
""" class Figura:
    def area(self):
        raise NotImplementedError('Este método debe ser implementado por las subclases')
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
# Ejemplo de uso
triangulo = Triangulo(5, 10)
Cuadrado = Cuadrado(4)
print(f"Área del triángulo: {triangulo.area()}")
print(f"Área del cuadrado: {Cuadrado.area()}") """