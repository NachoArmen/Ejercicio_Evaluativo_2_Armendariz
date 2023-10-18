class Cine:
    def __init__(self, id,nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.programacion = []



    def agregar_pelicula(self, pelicula):
        self.programacion.append(pelicula)

    def mostrar_programacion(self):
        print(f"Programación de {self.nombre} en {self.direccion}")
        for p in self.programacion:
            p.mostrar_info()
            print("------------------")
