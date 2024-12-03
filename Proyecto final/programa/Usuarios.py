from conexion import bd as baseDeDatos

class Usuario:
    def __init__(self,bd:baseDeDatos) -> None:
        self.bd = bd

    def registrar_usuario(self,dni_usuario, nombre, apellido, fecha_inscripcion):
        query = "INSERT INTO usuarios (dni_usuario,nombre, apellido, fecha_inscripcion) VALUES (%s, %s, %s, %s)"
        valores = (dni_usuario, nombre, apellido, fecha_inscripcion)
        self.bd.ejecutar(query, valores)
        return "Usuario registrado con éxito."
    
    def actualizar_usuario(self, dni_usuario, nombre, apellido, fecha_inscripcion):
        query = "UPDATE usuarios SET nombre=%s, apellido=%s, fecha_inscripcion=%s WHERE dni_usuario=%s"
        valores = (nombre, apellido, fecha_inscripcion,dni_usuario)
        self.bd.ejecutar(query, valores)
        return "Usuario actualizado con éxito."
    
    def ver_usuario(self, dni_usuario):
        query = "SELECT * FROM usuarios WHERE dni_usuario = %s"
        return self.bd.obtener_datos(query, (dni_usuario,))
    
    def eliminar_usuario(self, dni_usuario):
        query = "DELETE FROM usuarios WHERE dni_usuario = %s"
        self.bd.ejecutar(query, (dni_usuario,))
        return "Usuario eliminado con éxito."
    
    def ver_usuarios(self):
        query = "SELECT * FROM usuarios"
        return self.bd.obtener_datos(query,)
    
    def buscar_usuario_por_nombre(self, nombre, apellido):
        query = "SELECT * FROM usuarios WHERE (nombre LIKE %s) OR (apellido LIKE %s)"
        valores = (f"%{nombre}%", f"%{apellido}%")
        return self.bd.obtener_datos(query, valores)