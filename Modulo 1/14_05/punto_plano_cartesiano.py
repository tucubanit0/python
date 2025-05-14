import math

# Crea una clase llamada Punto que represente un punto en un plano cartesiano con coordenadas x e y. 
# La clase debe tener métodos para establecer las coordenadas, obtener las coordenadas y calcular la distancia entre dos puntos.

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def establecer_coordenadas(self, x, y):
        self.x = x
        self.y = y

    def obtener_coordenadas(self):
        return (self.x, self.y)

    def calcular_distancia(self, otro_punto):
        return math.hypot(self.x - otro_punto.x, self.y - otro_punto.y)
    
# Ejemplo de uso
punto1 = Punto(3, 4)
punto2 = Punto(6, 8)
print("Coordenadas del punto 1:", punto1.obtener_coordenadas())
print("Coordenadas del punto 2:", punto2.obtener_coordenadas())
print("Distancia entre los puntos:", punto1.calcular_distancia(punto2))

        