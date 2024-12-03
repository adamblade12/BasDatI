from conexion import bd as baseDatos

class Pago:
    def __init__(self,bd:baseDatos) -> None:
        self.bd = bd

    def registrar_pago(self, dni_usuario, monto, mes, año, estado):
        query = "INSERT INTO pagos (dni_usuario, monto, mes, año, estado) VALUES (%s, %s, %s, %s, %s)"
        valores = (dni_usuario, monto, mes, año, estado)
        self.bd.ejecutar(query, valores)
        return "Pago registrado con éxito."
    
    def actualizar_pago(self,id_pago, dni_usuario, monto, mes, año, estado):
        query = "UPDATE pagos SET dni_usuario=%s, monto=%s, mes=%s, año=%s, estado=%s WHERE id_pago=%s"
        valores = (dni_usuario, monto, mes, año, estado,id_pago)
        self.bd.ejecutar(query, valores)
        return "Pago actualizado con éxito."
    
    def ver_pago(self, id_pago):
        query = "SELECT * FROM pagos WHERE id_pago = %s"
        return self.bd.obtener_datos(query, (id_pago,))
    
    def eliminar_pago(self, id_pago):
        query = "DELETE FROM pagos WHERE id_pago = %s"
        self.bd.ejecutar(query, (id_pago,))
        return "Pago eliminado con éxito."
    
    def ver_pagos(self):
        query = "SELECT * FROM pagos"
        return self.bd.obtener_datos(query,)
    
    def buscar_pago_por_usuario(self, dni_usuario):
        query = "SELECT * FROM pagos WHERE dni_usuario LIKE %s"
        valores = (f"%{dni_usuario}%",)
        return self.bd.obtener_datos(query, valores)
    
    def buscar_pago_por_mes_año(self,mes,año):
        query = "SELECT * FROM pagos WHERE mes LIKE %s or año LIKE %s"
        valores = (f"%{mes}%",f"%{año}%")
        return self.bd.obtener_datos(query,valores)
    
    def calcular_promedio_morosos(self):
        query = "SELECT calcular_promedio_usuarios_morosos()"
        return self.bd.obtener_datos(query,)