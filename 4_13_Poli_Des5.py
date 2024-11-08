class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def resultado(self):
        # Método genérico sin implementación específica
        raise NotImplementedError("Este método debe ser sobrescrito por una subclase.")

class Suma(Operacion):
    def resultado(self):
        # Realiza la suma de a y b
        return self.a + self.b

class Multiplicacion(Operacion):
    def resultado(self):
        # Realiza la multiplicación de a y b
        return self.a * self.b

# Crear instancias de las subclases con valores específicos
suma = Suma(5, 3)
multiplicacion = Multiplicacion(5, 3)

# Demostrar polimorfismo
operaciones = [suma, multiplicacion]

for operacion in operaciones:
    print(f"Resultado de {operacion.__class__.__name__}: {operacion.resultado()}")
