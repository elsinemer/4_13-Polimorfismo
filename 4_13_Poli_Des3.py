class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        # Llamar al constructor de la clase base para inicializar título y autor
        super().__init__(titulo, autor)
        self.campo_estudio = campo_estudio
        self.nivel_especializacion = nivel_especializacion

    def __str__(self):
        return (f"'{self.titulo}' por {self.autor}\n"
                f"Campo de estudio: {self.campo_estudio}\n"
                f"Nivel de especialización: {self.nivel_especializacion.capitalize()}")

# Crear una instancia de LibroEspecializado y mostrar su información
libro_especializado = LibroEspecializado("Cálculo Avanzado", "James Stewart", "Matemáticas", "avanzado")
print(libro_especializado)
