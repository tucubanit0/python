# Crear una clase base "Animal" con un método para hacer sonidos, y luego crear clases derivadas 
# como "Perro", "Gato" y "Vaca" que hereden de "Animal" y sobrescriban el método para hacer sonidos específicos.

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Perro(Animal):
    def hacer_sonido(self):
        return 'Guau! Guau!'
    
class Gato(Animal):
    def hacer_sonido(self):
        return 'Miau! Miau!'
    
class Vaca(Animal):
    def hacer_sonido(self):
        return 'Muu! Muu!'
    
# Ejemplo de uso
def main():
    animales = [Perro(), Gato(), Vaca()]
    
    for animal in animales:
        print(f'El sonido del {animal.__class__.__name__} es: {animal.hacer_sonido()}')

if __name__ == "__main__":
    main()
    
