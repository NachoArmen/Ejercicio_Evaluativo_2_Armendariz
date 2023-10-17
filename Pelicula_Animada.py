from Pelicula import Pelicula


class Pelicula_Animada(Pelicula):
    def __init__(self, titulo, duracion, genero, estudio):
        super().__init__(titulo, duracion, genero)
        self.estudio = estudio

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Estudio de animación: {self.estudio}")
