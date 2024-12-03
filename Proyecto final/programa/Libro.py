from conexion import bd as baseDatos

class Libro:
    def __init__(self,db:baseDatos) -> None:
        self.db = db

    def registrar_libro(self, titulo, autor, descripcion):
        query = "INSERT INTO libros (titulo, autor, descripcion) VALUES (%s, %s, %s)"
        valores = (titulo, autor, descripcion)
        self.db.ejecutar(query, valores)
        return "Libro registrado con éxito."
    
    def actualizar_libro(self, id_libro, titulo, autor, descripcion):
        query = "UPDATE libros SET titulo=%s, autor=%s, descripcion=%s WHERE id_libro=%s"
        valores = (titulo, autor, descripcion,id_libro)
        self.db.ejecutar(query, valores)
        return "Libro actualizado con éxito."
    
    def ver_libro(self, id_libro):
        query = "SELECT * FROM libros WHERE id_libro = %s"
        return self.db.obtener_datos(query, (id_libro,))
    
    def eliminar_libro(self, id_libro):
        query = "DELETE FROM libros WHERE id_libro = %s"
        self.db.ejecutar(query, (id_libro,))
        return "Libro eliminado con éxito."
    
    def ver_libros(self):
        query = "SELECT * FROM libros"
        return self.db.obtener_datos(query,)
    
    def buscar_libro_por_titulo(self, titulo):
        query = "SELECT * FROM libros WHERE titulo LIKE %s"
        valores = (f"%{titulo}%",)
        return self.db.obtener_datos(query, valores)