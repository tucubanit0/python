# Crear una clase base "Empleado" con atributos como nombre y salario, y un método para calcular el salario mensual. 
# Luego, crear clases derivadas como "Gerente" y "Programador" que hereden de "Empleado" y sobrescriban el método para calcular el salario mensual según el cargo.

class Empleado:
    def __init__(self, nombre, salsario, horas_trabajadas):
        self.nombre = nombre
        self.salsario = salsario
        self.horas_trabajadas = horas_trabajadas
    def calcular_salario_mensual(self):
        return self.salsario * self.horas_trabajadas
    
class Gerente(Empleado):
    def __init__(self, nombre, salsario, horas_trabajadas):
        super().__init__(nombre, salsario, horas_trabajadas)
    def calcular_salario_mensual(self):
        return super().calcular_salario_mensual() + 1000  # Bonificación para el gerente
    
class Programador(Empleado):
    def __init__(self, nombre, salsario, horas_trabajadas):
        super().__init__(nombre, salsario, horas_trabajadas)
    def calcular_salario_mensual(self):
        return super().calcular_salario_mensual() + 500  # Bonificación para el programador
    
# Ejemplo de uso
def main():
    empleados = [
        Gerente("Juan", 50, 160),
        Programador("Ana", 30, 160)
    ]
    
    for empleado in empleados:
        print(f'El salario mensual de {empleado.nombre} es: {empleado.calcular_salario_mensual()}')

if __name__ == "__main__":
    main()