import sqlite3

class Conexion:
    def __init__(self, mi_db):
        self.conexion = sqlite3.connect("mi_db.db")
        self.cursor = self.conexion.cursor()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS peliculas (
                id INTEGER PRIMARY KEY,
                titulo VARCHAR(100),
                duracion INTEGER,
                genero VARCHAR(50)
            )
        ''')
        self.conexion.commit()

    def agregar_pelicula(self,titulo,duracion,genero):
        self.cursor.execute('''INSERT INTO peliculas(titulo,duracion,genero) VALUES(?,?,?)''',(titulo, duracion, genero))
        self.conexion.commit()

    def modificar_pelicula(self,titulo,duracion,genero,id):
        self.cursor.execute('''UPDATE peliculas set titulo=?,duracion=?,genero=? WHERE id=?''',(titulo, duracion, genero, id))
        self.conexion.commit()

    def eliminar_pelicula(self,id):
        self.cursor.execute('''DELETE FROM peliculas WHERE id=?''', id)
        self.conexion.commit()

    def lista_peliculas(self):
        self.cursor.execute('''SELECT * FROM peliculas''')
        peliculas= self.cursor.fetchall()
        #debes retornar las peliculas
        return peliculas









