# Crear una clase base "Figura" con un método para calcular el área, y luego crear clases derivadas 
# como "Rectangulo" y "Circulo" que hereden de "Figura" y sobrescriban el método para calcular el área según la forma geométrica.

class Figura:
    def calcular_area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
         return self.base * self.altura
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return 3.14 * (self.radio ** 2)
    
# Ejemplo de uso
def main():
    figuras = [Rectangulo(5, 10), Circulo(7)]
    
    for figura in figuras:
        print(f'El área de la {figura.__class__.__name__} es: {figura.calcular_area()}')
        
if __name__ == "__main__":
    main()
    
