# Crea una clase llamada Coche que represente un coche con marca, modelo y año. 
# La clase debe tener métodos para obtener y establecer la marca, el modelo y el año del coche, así como un método para imprimir la información del coche.

marca = input("Ingrese la marca del coche: ")

modelo = input("Ingrese el modelo del coche: ")

year = input("Ingrese el año del coche: ")

class Coche:
    def __init__(self, marca="", modelo="", year=""):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        
    def estalecer_marca(self, marca):
        self.marca = marca
        
    def establecer_modelo(self, modelo):
        self.modelo = modelo
        
    def establecer_year(self, year):
        self.year = year
        
    def obtener_marca(self):
        return self.marca
    
    def obtener_modelo(self):
        return self.modelo
    
    def obtener_year(self):
        return self.year
    
    def imprimir_informacion(self):
        return f'Información del coche: Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.year}'
    
coche = Coche(marca, modelo, year)
print("Información del coche:", coche.imprimir_informacion())