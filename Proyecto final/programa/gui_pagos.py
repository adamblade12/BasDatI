import tkinter
from tkinter import messagebox, simpledialog, Toplevel
from conexion import bd
from Pago import Pago

class gui_pagos:
    def __init__(self,padre) -> None:
        self.db = bd(host="localhost", user="root", password="4123", database="biblioteca")
        self.db.conectar()

        self.pago_db = Pago(self.db)

        self.ventana = Toplevel(padre)
        self.ventana.title("Gestión de Pago")

        tkinter.Button(self.ventana, text="Registrar Pago", command=self.mostrar_registro_pago).pack(pady=5)
        tkinter.Button(self.ventana, text="Actualizar Pago", command=self.mostrar_actualizacion_pago).pack(pady=5)
        tkinter.Button(self.ventana, text="Eliminar Pago", command=self.mostrar_eliminacion_pago).pack(pady=5)
        tkinter.Button(self.ventana, text="Ver Pagos", command=self.mostrar_pagos).pack(pady=5)
        tkinter.Button(self.ventana, text="Buscar Pagos por Usuario", command=self.mostrar_busqueda_pago).pack(pady=5)
        tkinter.Button(self.ventana,text="Calcular Promedio Morosos",command=self.mostrar_promedio_morosos).pack(pady=6)

        self.ventana.mainloop()

    def mostrar_busqueda_pago(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Buscar Pago por Usuario")

        tkinter.Label(ventana, text="DNI:").grid(row=0, column=0)

        dni_usuario = tkinter.Entry(ventana)

        dni_usuario.grid(row=0, column=1)

        listbox_resultados = tkinter.Listbox(ventana, width=60)
        listbox_resultados.grid(row=3, column=0, columnspan=2)

        def buscar():
            resultados = self.pago_db.buscar_pago_por_usuario(dni_usuario.get())
            listbox_resultados.delete(0, tkinter.END)  # Limpiar resultados previos
            for pago in resultados:
                listbox_resultados.insert(tkinter.END, pago)

        tkinter.Button(ventana, text="Buscar", command=buscar).grid(row=2, column=0, columnspan=2)

    def mostrar_registro_pago(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Registrar Pago")

        tkinter.Label(ventana, text="DNI:").grid(row=0,column=0)
        tkinter.Label(ventana, text="Monto:").grid(row=1, column=0)
        tkinter.Label(ventana,text="Mes:").grid(row=2,column=0)
        tkinter.Label(ventana, text="Año:").grid(row=3, column=0)
        tkinter.Label(ventana,text="Estado:").grid(row=4,column=0)
        

        dni_usuario = tkinter.Entry(ventana)
        monto = tkinter.Entry(ventana)
        mes = tkinter.Entry(ventana)
        año = tkinter.Entry(ventana)
        estado = tkinter.Entry(ventana)

        dni_usuario.grid(row=0,column=1)
        monto.grid(row=1, column=1)
        mes.grid(row=2, column=1)
        año.grid(row=3,column=1)
        estado.grid(row=4,column=1)

        def registrar():
            msg = self.pago_db.registrar_pago(dni_usuario.get(),monto.get(), mes.get(), año.get(), estado.get())
            messagebox.showinfo("Información", msg)
            ventana.destroy()

        tkinter.Button(ventana, text="Registrar", command=registrar).grid(row=5, column=0, columnspan=2)

    def mostrar_actualizacion_pago(self):
        id_pago = simpledialog.askinteger("Actualizar Pago", "Ingrese el Id del Pago a actualizar:")
        pago_info = self.pago_db.ver_pago(id_pago)

        if not pago_info:
            messagebox.showerror("Error", "Pago no encontrado.")
            return

        ventana = Toplevel(self.ventana)
        ventana.title("Actualizar Pago")

        tkinter.Label(ventana,text="Id Pago:").grid(row=0,column=0)
        tkinter.Label(ventana, text="DNI Usuario:").grid(row=1, column=0)
        tkinter.Label(ventana, text="Monto:").grid(row=2, column=0)
        tkinter.Label(ventana,text="Mes:").grid(row=3,column=0)
        tkinter.Label(ventana,text="Año:").grid(row=4,column=0)
        tkinter.Label(ventana,text="Estado:").grid(row=5,column=0)

        dni_usuario = tkinter.Entry(ventana)
        monto = tkinter.Entry(ventana)
        mes = tkinter.Entry(ventana)
        año = tkinter.Entry(ventana)
        estado = tkinter.Entry(ventana)

        dni_usuario.grid(row=1, column=1)
        monto.grid(row=2, column=1)
        mes.grid(row=3,column=1)
        año.grid(row=4,column=1)
        estado.grid(row=5,column=1)

        # Cargar datos actuales
        dni_usuario.insert(0, pago_info[0][1])
        monto.insert(0, pago_info[0][2])
        mes.insert(0, pago_info[0][3])
        año.insert(0,pago_info[0][4])
        estado.insert(0,pago_info[0][5])

        def actualizar():
            msg = self.pago_db.actualizar_pago(id_pago, dni_usuario.get(), monto.get(), mes.get(), año.get(), estado.get())
            messagebox.showinfo("Información", msg)
            ventana.destroy()

        tkinter.Button(ventana, text="Actualizar", command=actualizar).grid(row=7, column=0, columnspan=2)

    def mostrar_eliminacion_pago(self):
        id_pago = simpledialog.askinteger("Eliminar Pago", "Ingrese el Id del Pago a eliminar:")
        if id_pago:
            msg = self.pago_db.eliminar_pago(id_pago)
            messagebox.showinfo("Información", msg)

    def mostrar_pagos(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Ver Pagos")

        listbox = tkinter.Listbox(ventana, width=60)
        listbox.pack()

        for Pago in self.pago_db.ver_pagos():
            listbox.insert(tkinter.END, Pago)

    def mostrar_promedio_morosos(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Promedio de Morosos")

        tkinter.Label(ventana,text=f"Morosos: {self.pago_db.calcular_promedio_morosos()}").grid(row=1,column=0)

    def __del__(self):
        # Cerrar conexión al final
        self.db.desconectar()
