from conexion import bd as baseDeDatos

class Prestamo:
    def __init__(self,bd:baseDeDatos) -> None:
        self.bd = bd

    def registrar_prestamo(self,fecha_prestamo, fecha_devolucion, dni_usuario, id_libro):
        query = "INSERT INTO prestamos (fecha_prestamo, fecha_devolucion, dni_usuario, id_libro) VALUES (%s, %s, %s, %s)"
        valores = (fecha_prestamo, fecha_devolucion, dni_usuario, id_libro)
        self.bd.ejecutar(query, valores)
        return "Usuario registrado con éxito."
    
    def actualizar_prestamo(self, id_prestamo, dni_usuario, fecha_prestamo, fecha_devolucion,id_libro):
        query = "UPDATE prestamos SET dni_usuario=%s, fecha_prestamo=%s, fecha_devolucion=%s, id_libro=%s WHERE id_prestamo=%s"
        valores = (dni_usuario,fecha_prestamo, fecha_devolucion, id_libro, id_prestamo)
        self.bd.ejecutar(query, valores)
        return "Prestamo actualizado con éxito."
    
    def ver_prestamo(self, id_prestamo):
        query = "SELECT * FROM prestamos WHERE id_prestamo = %s"
        return self.bd.obtener_datos(query, (id_prestamo,))
    
    def eliminar_prestamo(self, id_prestamo):
        query = "DELETE FROM prestamos WHERE id_prestamo = %s"
        self.bd.ejecutar(query, (id_prestamo,))
        return "Prestamo eliminado con éxito."
    
    def ver_prestamos(self):
        query = "SELECT * FROM prestamos"
        return self.bd.obtener_datos(query,)
    
    def buscar_prestamo_por_usuario(self, dni_usuario):
        query = "SELECT * FROM prestamos WHERE (dni_usuario = %s)"
        valores = (f"{dni_usuario}",)
        return self.bd.obtener_datos(query, valores)