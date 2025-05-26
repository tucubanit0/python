# Crear una clase base "InstrumentoMusical" con un método para tocar el instrumento, y luego crear clases derivadas como "Guitarra" y "Piano" que
# hereden de "InstrumentoMusical" y sobrescriban el método para tocar el instrumento de forma específica.

class InstrumentoMusical:
    def tocar(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")
    
class Guitarra(InstrumentoMusical):
    def tocar(self):
        return 'Tocando la guitarra: Strum, strum!'
    
class Piano(InstrumentoMusical):
    def tocar(self):
        return 'Tocando el piano: Do, re, mi!'
    
# Ejemplo de uso
def main():
    instrumentos = [Guitarra(), Piano()]
    
    for instrumento in instrumentos:
        print(f'El sonido del {instrumento.__class__.__name__} es: {instrumento.tocar()}')

if __name__ == "__main__":
    main()