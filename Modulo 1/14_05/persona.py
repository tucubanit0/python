# Crea una clase llamada Persona que represente a una persona con nombre y edad. 
# La clase debe tener métodos para obtener y establecer el nombre y la edad, así como un método para saludar.

input_nombre = input("Ingrese su nombre: ")
input_edad = input("Ingrese su edad: ")

class Persona:
    def __init__(self, input_nombre="", input_edad=""):
        self.input_nombre = input_nombre
        self.input_edad = input_edad
        
    def establecer_nombre(self, nombre):
        self.input_nombre = input_nombre
        
    def establecer_edad(self, edad):
        self.input_edad = input_edad
        
    def obtener_nombre(self):
        return self.input_nombre
    
    def obtener_edad(self):
        return self.input_edad
    
    def saludar(self):
        return f'Hola, mi nombre es {self.input_nombre} y tengo {self.input_edad} años.'
    
# Ejemplo de uso
persona = Persona(input_nombre, input_edad) 
print("Nombre de la persona:", persona.obtener_nombre())
print("Edad de la persona:", persona.obtener_edad())
print(persona.saludar())