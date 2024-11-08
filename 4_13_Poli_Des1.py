class Musico:
    def instrumento(self):
        return "Instrumento no especificado"

class Guitarrista(Musico):
    def instrumento(self):
        return "Toco la guitarra"

class Baterista(Musico):
    def instrumento(self):
        return "Toco la batería"

# Crear instancias de las subclases
guitarrista = Guitarrista()
baterista = Baterista()

# Demostrar polimorfismo
musicos = [guitarrista, baterista]

for musico in musicos:
    print(musico.instrumento())
