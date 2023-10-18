class Pelicula:
    def __init__(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero


    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Duración: {self.duracion}")
        print(f"Género: {self.genero}")