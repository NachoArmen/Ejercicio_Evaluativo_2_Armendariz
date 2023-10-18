from Conexion import Conexion
from Pelicula import Pelicula #importar pelicula
class Cine:
    def __init__(self, id,nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.programacion = []



    def agregar_pelicula(self, pelicula):
        self.programacion.append(pelicula)
#tienes cque conectarte a la base de datos y luego extraer los elementos
    def mostrar_programacion(self):
        print(f"Programación de {self.nombre} en {self.direccion}")
        conexion=Conexion("mi_db.db")
        peliculas=conexion.lista_peliculas()

        for peli in peliculas:
            print(peli)
            print("------------------")


