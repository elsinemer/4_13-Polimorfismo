class Autor:
    def biografia(self):
        return "Esta es la biografía general de un autor."

class Escritor(Autor):
    def biografia(self):
        return "Esta es la biografía de un escritor en particular."

    def biografia_autor(self):
        # Llamar al método biografia de la clase Autor usando super()
        return super().biografia()

# Crear una instancia de Escritor
escritor = Escritor()

# Mostrar el resultado de ambos métodos
print("Biografía del escritor:")
print(escritor.biografia())  # Llama al método sobrescrito en Escritor

print("\nBiografía de la clase Autor desde Escritor:")
print(escritor.biografia_autor())  # Llama al método de la clase Autor
