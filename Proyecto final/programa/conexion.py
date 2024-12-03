import mysql.connector

class bd:
    def __init__(self, host, user, password, database) -> None:
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        self.conexion = None
        self.cursor = None
    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.config)
            self.cursor = self.conexion.cursor()
            if self.conexion.is_connected():
                print("Conexion exitosa")
        except mysql.connector.Error as error:
            print("Error al conectar con MySQL")


    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

    def ejecutar(self, query, valores=None):
        if not self.conexion.is_connected():
            raise Exception("No hay conexión activa a la base de datos")
        try:
            self.cursor.execute(query, valores or ())
            self.conexion.commit()
        except mysql.connector.Error as error:
            print(f"Error al ejecutar consulta: {error}")
            raise

    def obtener_datos(self, query, valores=None):
        if not self.conexion.is_connected():
            raise Exception("No hay conexión activa a la base de datos")
        try:
            self.cursor.execute(query, valores or ())
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            print(f"Error al ejecutar consulta: {error}")
            raise