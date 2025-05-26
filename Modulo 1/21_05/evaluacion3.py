# Crear una clase "Persona" que tenga atributos como nombre, edad y profesión, y métodos para obtener y establecer esos atributos.
""" class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, nueva_edad):
        self.edad = nueva_edad

    def obtener_profesion(self):
        return self.profesion

    def establecer_profesion(self, nueva_profesion):
        self.profesion = nueva_profesion
        
# Crear una instancia de la clase Persona y probar los métodos
persona1 = Persona("Juan", 30, "Ingeniero")
print("Nombre:", persona1.obtener_nombre())
print("Edad:", persona1.obtener_edad())
print("Profesión:", persona1.obtener_profesion())
persona1.establecer_nombre("Pedro")
persona1.establecer_edad(35)
persona1.establecer_profesion("Arquitecto")
print("Nombre actualizado:", persona1.obtener_nombre())
print("Edad actualizada:", persona1.obtener_edad())
print("Profesión actualizada:", persona1.obtener_profesion()) """

# Crear una clase "Perro" que tenga atributos como nombre, raza y edad, y un método para ladrar.
""" class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    def ladrar(self):
        return "¡Guau! ¡Guau!"
# Crear una instancia de la clase Perro y probar el método ladrar
perro1 = Perro("Max", "Labrador", 5)
print("Nombre del perro:", perro1.nombre)
print("Raza del perro:", perro1.raza)
print("Edad del perro:", perro1.edad)
print("El perro dice:", perro1.ladrar()) """

# Crear una clase "CuentaBancaria" que represente una cuenta bancaria con atributos como número de cuenta, saldo y titular, y métodos para realizar depósitos y retiros.
""" class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo, titular):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.titular = titular

    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}"

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return "Fondos insuficientes"
        else:
            self.saldo -= cantidad
            return f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}"
# Crear una instancia de la clase CuentaBancaria y probar los métodos de depósito y retiro
cuenta1 = CuentaBancaria("123456789", 1000, "Juan Pérez")
print("Número de cuenta:", cuenta1.numero_cuenta)
print("Titular de la cuenta:", cuenta1.titular)
print("Saldo inicial:", cuenta1.saldo)
print(cuenta1.depositar(500))
print(cuenta1.retirar(200))
print(cuenta1.retirar(2000)) """

# Crear un script para gestionar una central de reservas de hoteles. Crea una clase "Hotel" que tenga atributos para el nombre del hotel y la capacidad total de habitaciones, 
# así como las habitaciones disponibles, y métodos para mostrar la información del hotel, las reservas en ese hotel y las habitaciones que se dejan libres.

""" class Hotel:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.habitaciones_disponibles = capacidad

    def mostrar_informacion(self):
        return f"Hotel: {self.nombre}, Capacidad total: {self.capacidad}, Habitaciones disponibles: {self.habitaciones_disponibles}"

    def reservar_habitacion(self, cantidad):
        if cantidad <= self.habitaciones_disponibles:
            self.habitaciones_disponibles -= cantidad
            return f"Reservadas {cantidad} habitaciones. Habitaciones restantes: {self.habitaciones_disponibles}"
        else:
            return "No hay suficientes habitaciones disponibles"

    def liberar_habitacion(self, cantidad):
        if cantidad + self.habitaciones_disponibles <= self.capacidad:
            self.habitaciones_disponibles += cantidad
            return f"Se han liberado {cantidad} habitaciones. Habitaciones disponibles: {self.habitaciones_disponibles}"
        else:
            return "No se pueden liberar más habitaciones de las que hay en total"
        
# Crear una instancia de la clase Hotel
hotel1 = Hotel("Hotel Playa", 100)
print(hotel1.mostrar_informacion())
print(hotel1.reservar_habitacion(20))
print(hotel1.mostrar_informacion())
print(hotel1.liberar_habitacion(10))
print(hotel1.mostrar_informacion())
print(hotel1.liberar_habitacion(100))  # Intentar liberar más habitaciones de las que hay en total
print(hotel1.reservar_habitacion(90))  # Intentar reservar más habitaciones de las que hay disponibles
print(hotel1.mostrar_informacion()) """

# Crear una clase "Estudiante" que tenga atributos como nombre, 
# edad y una lista de materias cursadas, y métodos para agregar una nueva materia y obtener la lista de materias cursadas.
""" class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.materias_cursadas = []

    def agregar_materia(self, materia):
        self.materias_cursadas.append(materia)
        return f"Materia '{materia}' agregada."

    def obtener_materias(self):
        return f"Materias cursadas por {self.nombre}: {', '.join(self.materias_cursadas)}"
# Crear una instancia de la clase Estudiante y probar los métodos
estudiante1 = Estudiante("Ana", 20)
print("Nombre del estudiante:", estudiante1.nombre)
print("Edad del estudiante:", estudiante1.edad)
print(estudiante1.agregar_materia("Matemáticas"))
print(estudiante1.agregar_materia("Historia"))
print(estudiante1.obtener_materias())
print(estudiante1.agregar_materia("Ciencias"))
print(estudiante1.obtener_materias()) """

# Crear una clase base "Vehiculo" con atributos como marca, modelo y cilindrada, y métodos para obtener y establecer esos atributos. 
# Luego, crear una clase derivada "Automovil" que herede de "Vehiculo" y agregue un atributo adicional para el tipo de combustible.
""" class Vehiculo:
    def __init__(self, marca, modelo, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

    def obtener_marca(self):
        return self.marca

    def establecer_marca(self, nueva_marca):
        self.marca = nueva_marca

    def obtener_modelo(self):
        return self.modelo

    def establecer_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    def obtener_cilindrada(self):
        return self.cilindrada

    def establecer_cilindrada(self, nueva_cilindrada):
        self.cilindrada = nueva_cilindrada
        
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, cilindrada, tipo_combustible):
        super().__init__(marca, modelo, cilindrada)
        self.tipo_combustible = tipo_combustible

    def obtener_tipo_combustible(self):
        return self.tipo_combustible

    def establecer_tipo_combustible(self, nuevo_tipo_combustible):
        self.tipo_combustible = nuevo_tipo_combustible
# Crear una instancia de la clase Automovil y probar los métodos
automovil1 = Automovil("Toyota", "Corolla", 1600, "Gasolina")
print("Marca del automóvil:", automovil1.obtener_marca())
print("Modelo del automóvil:", automovil1.obtener_modelo())
print("Cilindrada del automóvil:", automovil1.obtener_cilindrada())
print("Tipo de combustible del automóvil:", automovil1.obtener_tipo_combustible())
automovil1.establecer_marca("Honda")
automovil1.establecer_modelo("Civic")
automovil1.establecer_cilindrada(2000)
automovil1.establecer_tipo_combustible("Diésel")
print("Marca actualizada del automóvil:", automovil1.obtener_marca())
print("Modelo actualizado del automóvil:", automovil1.obtener_modelo())
print("Cilindrada actualizada del automóvil:", automovil1.obtener_cilindrada())
print("Tipo de combustible actualizado del automóvil:", automovil1.obtener_tipo_combustible()) """

# Crear una clase base "Animal" con un método para hacer sonidos, y luego crear clases derivadas como 
# "Perro", "Gato", "Mono", “Tortuga” que hereden de "Animal" y sobrescriban el método para hacer sonidos específicos.
""" class Animal:
    def hacer_sonido(self):
        return "El animal hace un sonido"

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau! ¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau! ¡Miau!"

class Mono(Animal):
    def hacer_sonido(self):
        return "¡Uuuh! ¡Aaah!"
    
class Tortuga(Animal):
    def hacer_sonido(self):
        return "Hiii Hiii."

# Crear instancias de las clases derivadas y probar el método hacer_sonido
perro1 = Perro()
gato1 = Gato()
mono1 = Mono()
tortuga1 = Tortuga()
print("Perro:", perro1.hacer_sonido())
print("Gato:", gato1.hacer_sonido())
print("Mono:", mono1.hacer_sonido())
print("Tortuga:", tortuga1.hacer_sonido()) """

# Crear un script para gestionar una central de reservas de hoteles. Crea una clase "Hotel" que tenga atributos y métodos para 
# todos los hoteles; además se crearán dos clases derivadas que serán 
# “HotelEconómico” y “HotelDeLujo” y heredan su nombre, la capacidad del hotel y las habitaciones disponibles. 
# La clase “HotelEconómico” tiene un atributo adicional llamado “tarifa” y un método llamado “calcular_precio” que calcula el precio 
# total en base a la tarifa y cantidad de noches. La clase “HotelDeLujo” tiene un atributo adicional llamado “servicios_adicionales” 
# y un método “mostrar_servicios” que muestra los servicios adicionales disponibles en el hotel de lujo.

""" class Hotel:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.habitaciones_disponibles = capacidad

    def mostrar_informacion(self):
        return f"Hotel: {self.nombre}, Capacidad total: {self.capacidad}, Habitaciones disponibles: {self.habitaciones_disponibles}"

    def reservar_habitacion(self, cantidad):
        if cantidad <= self.habitaciones_disponibles:
            self.habitaciones_disponibles -= cantidad
            return f"Reservadas {cantidad} habitaciones. Habitaciones restantes: {self.habitaciones_disponibles}"
        else:
            return "No hay suficientes habitaciones disponibles"

    def liberar_habitacion(self, cantidad):
        if cantidad + self.habitaciones_disponibles <= self.capacidad:
            self.habitaciones_disponibles += cantidad
            return f"Se han liberado {cantidad} habitaciones. Habitaciones disponibles: {self.habitaciones_disponibles}"
        else:
            return "No se pueden liberar más habitaciones de las que hay en total"

class HotelEconomico(Hotel):
    def __init__(self, nombre, capacidad, tarifa):
        super().__init__(nombre, capacidad)
        self.tarifa = tarifa

    def calcular_precio(self, noches):
        return self.tarifa * noches
# Crear una instancia de la clase HotelEconomico
hotel_economico = HotelEconomico("Hotel Económico", 50, 100)
print(hotel_economico.mostrar_informacion())
print("Precio total por 3 noches:", hotel_economico.calcular_precio(3))
class HotelDeLujo(Hotel):
    def __init__(self, nombre, capacidad, servicios_adicionales):
        super().__init__(nombre, capacidad)
        self.servicios_adicionales = servicios_adicionales

    def mostrar_servicios(self):
        return f"Servicios adicionales en {self.nombre}: {', '.join(self.servicios_adicionales)}"
# Crear una instancia de la clase HotelDeLujo
hotel_lujo = HotelDeLujo("Hotel de Lujo", 30, ["Spa", "Gimnasio", "Restaurante"])
print(hotel_lujo.mostrar_informacion())
print(hotel_lujo.mostrar_servicios())
# Crear una instancia de la clase Hotel
hotel1 = Hotel("Hotel Playa", 100)
print(hotel1.mostrar_informacion())
print(hotel1.reservar_habitacion(20))
print(hotel1.mostrar_informacion())
print(hotel1.liberar_habitacion(10))
print(hotel1.mostrar_informacion())
print(hotel1.liberar_habitacion(100))  
print(hotel1.reservar_habitacion(90))  
print(hotel1.mostrar_informacion())
# Crear una instancia de la clase HotelEconomico
hotel_economico = HotelEconomico("Hotel Económico", 50, 100)
print(hotel_economico.mostrar_informacion())
print("Precio total por 3 noches:", hotel_economico.calcular_precio(3)) """

# Crear una clase base "Empleado" con atributos como nombre y salario, y un método para calcular el salario mensual. 
# Luego, crear clases derivadas como "Administrativo" y "Tecnico" que hereden de "Empleado" y sobrescriban el método para calcular el salario mensual según el cargo. 
# El Técnico/a cobra un 20% más que el Administrativo. Nos debemos de inventar el salario del Administrativo/a.
""" class Empelado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario_mensual(self):
        return self.salario

class Administrativo(Empelado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)

    def calcular_salario_mensual(self):
        return self.salario

class Tecnico(Empelado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        self.salario = salario * 1.2  # El Técnico cobra un 20% más que el Administrativo
# Crear instancias de las clases y probar el método calcular_salario_mensual
administrativo1 = Administrativo("Juan", 1500)
tecnico1 = Tecnico("Ana", 1800)
print("Salario mensual del Administrativo:", administrativo1.calcular_salario_mensual())
print("Salario mensual del Técnico:", tecnico1.calcular_salario_mensual())     """

# Crear una clase base "GrupoRock" con un método para tocar el instrumento, y luego crear clases derivadas como 
# "Guitarrista", "Cantante", “Batería” que hereden de "GrupoRock" y sobrescriban el método para tocar el instrumento de forma específica.
class GrupoRock:
    def tocar_instrumento(self):
        return "El grupo toca su música"
class Guitarrista(GrupoRock):
    def tocar_instrumento(self):
        return "El guitarrista toca la guitarra"
class Cantante(GrupoRock):
    def tocar_instrumento(self):
        return "El cantante canta"
class Bateria(GrupoRock):
    def tocar_instrumento(self):
        return "El batería toca la batería"
# Crear instancias de las clases derivadas y probar el método tocar_instrumento
guitarrista1 = Guitarrista()
cantante1 = Cantante()
bateria1 = Bateria()
print("Guitarrista:", guitarrista1.tocar_instrumento())
print("Cantante:", cantante1.tocar_instrumento())
print("Batería:", bateria1.tocar_instrumento())