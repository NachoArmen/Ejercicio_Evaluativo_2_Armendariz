import sqlite3
from Conexion import Conexion
from Pelicula import Pelicula
from Pelicula_Animada import Pelicula_Animada
from Cine import Cine




db = Conexion("mi_db.db")
db.crear_tabla()


c1 = Cine(1,"Cinepolis", "Houssay 789")
c2 = Cine(2,"Cinemark", "Palermo 654")
c3 = Cine(3,"Hoyts", "Unicenter 123")

p1 = Pelicula("Toy Story", 90, "Animación")
p2 = Pelicula("Avatar", 120, "Ciencia Ficción")

db.agregar_pelicula(p1.titulo, p1.duracion, p1.genero)
db.agregar_pelicula(p2.titulo, p2.duracion, p2.genero)


c1.agregar_pelicula(p1)
c2.agregar_pelicula(p1)
c3.agregar_pelicula(p1)

def menu_cine(cine):

  while True:
    print(f"CINE: {cine.nombre}")
    print("""
    1. Agregar película
    2. Eliminar película
    3. Modificar película 
    4. Ver programación
    5. Salir
    """)

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        titulo = input("Titulo: ")
        duracion = input("Duración: ")
        genero = input("Género: ")
        cine.agregar_pelicula()
        db.agregar_pelicula(titulo, duracion, genero)

    elif opcion == "2":
        id = input("ID a eliminar: ")
        db.eliminar_pelicula(id)

    elif opcion == "3":
        id = input("ID a modificar: ")
        titulo = input("Nuevo titulo: ")
        duracion = input("Nueva duración: ")
        genero = input("Nuevo género: ")
        db.modificar_pelicula(titulo, duracion, genero, id)

    elif opcion == "4":
        cine.mostrar_programacion(cine_elegido)

    elif opcion == "5":
        break


db = Conexion("mi_db.db")
db.crear_tabla()



while True:

    print("Seleccione un cine:")
    print(f"1.{c1.nombre}")
    print(f"2.{c2.nombre}")
    print(f"3.{c2.nombre}")
    print("4.Salir")

    cine_elegido= input(">")

    if cine_elegido == "1":
        menu_cine(c1)
    elif cine_elegido == "2":
        menu_cine(c2)
    elif cine_elegido == "3":
        menu_cine(c3)
    else:
        break

