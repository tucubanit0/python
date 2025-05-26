# Crear una clase base "Animal" con un método "hacer_sonido()" y un método "moverse()". 
# Luego, crear clases derivadas como "Perro", "Gato" y "Ave" que hereden de "Animal" y sobrescriban ambos 
# métodos para producir sonidos y formas de movimiento específicas para cada tipo de animal. Crear una función llamada "interactuar_con_animal()" 
# que tome un objeto de la clase "Animal" y llame a ambos métodos, mostrando el sonido y la forma de movimiento correspondientes a ese animal.

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")
    def moverse(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")
    
class Perro(Animal):
    def hacer_sonido(self):
        return 'Guau! Guau!'
    def moverse(self):
        return 'El perro corre rápidamente.'
    
class Gato(Animal):
    def hacer_sonido(self):
        return 'Miau! Miau!'
    def moverse(self):
        return 'El gato salta ágilmente.'

class Ave(Animal):
    def hacer_sonido(self):
        return 'Pío! Pío!'
    def moverse(self):
        return 'El ave vuela alto en el cielo.'
    
# Función para interactuar con el animal
def interactuar_con_animal(animal):
    print(f'El sonido del {animal.__class__.__name__} es: {animal.hacer_sonido()}')
    print(f'La forma de moverse del {animal.__class__.__name__} es: {animal.moverse()}')    
    
# Ejemplo de uso
def main():
    animales = [Perro(), Gato(), Ave()]
    
    for animal in animales:
        interactuar_con_animal(animal)
        print()  # Línea en blanco para separar la salida de cada animal
        
if __name__ == "__main__":
    main()
