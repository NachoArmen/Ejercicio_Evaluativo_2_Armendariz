import sqlite3
from Conexion import Conexion
from Pelicula import Pelicula
from Pelicula_Animada import Pelicula_Animada
from Cine import Cine


#Cine 1
c1 = Cine("Hoyts", "Unicenter 123")
p1 = Pelicula_Animada("Toy Story", 90, "Animación", "Pixar")
p2 = Pelicula("Die Hard", 120, "Accion")

db = Conexion("mi_db.db")
db.crear_tabla()
db.agregar_pelicula(p1.titulo, p1.duracion, p1.genero)
c1.agregar_pelicula(p1)

peliculas = db.lista_peliculas()
print(peliculas)

c1.mostrar_programacion()