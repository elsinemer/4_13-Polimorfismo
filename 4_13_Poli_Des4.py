import math

class Figura:
    def area(self):
        # Método de área genérico, sin implementación específica
        raise NotImplementedError("Este método debe ser sobrescrito por una subclase.")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        # Cálculo del área del círculo: π * radio^2
        return math.pi * (self.radio ** 2)

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        # Cálculo del área del cuadrado: lado^2
        return self.lado ** 2

# Crear instancias de las subclases
circulo = Circulo(5)
cuadrado = Cuadrado(4)

# Demostrar polimorfismo
figuras = [circulo, cuadrado]

for figura in figuras:
    print(f"Área de la figura {figura.__class__.__name__}: {figura.area():.2f}")
