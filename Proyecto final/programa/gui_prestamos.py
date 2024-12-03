import tkinter
from tkinter import messagebox, simpledialog, Toplevel
from conexion import bd
from Prestamos import Prestamo

class gui_prestamos:
    def __init__(self,padre) -> None:
        self.db = bd(host="localhost", user="root", password="4123", database="biblioteca")
        self.db.conectar()

        self.prestamo_bd = Prestamo(self.db)

        self.ventana = Toplevel(padre)
        self.ventana.title("Gestión de Prestamos")

        tkinter.Button(self.ventana, text="Registrar Prestamo", command=self.mostrar_registro_prestamo).pack(pady=5)
        tkinter.Button(self.ventana, text="Actualizar Prestamo", command=self.mostrar_actualizacion_prestamo).pack(pady=5)
        tkinter.Button(self.ventana, text="Eliminar Prestamo", command=self.mostrar_eliminacion_prestamo).pack(pady=5)
        tkinter.Button(self.ventana, text="Ver Prestamos", command=self.mostrar_prestamos).pack(pady=5)
        tkinter.Button(self.ventana, text="Buscar Prestamo por Usuario", command=self.mostrar_busqueda_prestamo).pack(pady=5)

        self.ventana.mainloop()

    def mostrar_busqueda_prestamo(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Buscar Prestamo por Usuario")

        tkinter.Label(ventana, text="DNI Usuario:").grid(row=0, column=0)

        dni_usuario = tkinter.Entry(ventana)

        dni_usuario.grid(row=0, column=1)                                

        listbox_resultados = tkinter.Listbox(ventana, width=60)
        listbox_resultados.grid(row=3, column=0, columnspan=2)

        def buscar():
            resultados = self.prestamo_bd.buscar_prestamo_por_usuario(dni_usuario.get())
            listbox_resultados.delete(0, tkinter.END)  # Limpiar resultados previos
            for prestamo in resultados:
                listbox_resultados.insert(tkinter.END, prestamo)

        tkinter.Button(ventana, text="Buscar", command=buscar).grid(row=2, column=0, columnspan=2)

    def mostrar_registro_prestamo(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Registrar Prestamo")

        tkinter.Label(ventana, text="Fecha del Prestamo:").grid(row=0,column=0)
        tkinter.Label(ventana, text="Fecha de devolucion:").grid(row=1, column=0)
        tkinter.Label(ventana, text="DNI Usuario:").grid(row=2, column=0)
        tkinter.Label(ventana, text="Id_libro:").grid(row=3, column=0)

        fecha_prestamo = tkinter.Entry(ventana)
        fecha_devolucion = tkinter.Entry(ventana)
        dni_usuario = tkinter.Entry(ventana)
        id_libro = tkinter.Entry(ventana)

        fecha_prestamo.grid(row=0,column=1)
        fecha_devolucion.grid(row=1, column=1)
        dni_usuario.grid(row=2, column=1)
        id_libro.grid(row=3,column=1)

        def registrar():
            msg = self.prestamo_bd.registrar_prestamo(fecha_prestamo.get(),fecha_devolucion.get(), dni_usuario.get(), id_libro.get())
            messagebox.showinfo("Información", msg)
            ventana.destroy()

        tkinter.Button(ventana, text="Registrar", command=registrar).grid(row=5, column=0, columnspan=2)

    def mostrar_actualizacion_prestamo(self):
        id_prestamo = simpledialog.askinteger("Actualizar Prestamo", "Ingrese el Id del prestamo a actualizar:")
        prestamo_info = self.prestamo_bd.ver_prestamo(id_prestamo)

        if not prestamo_info:
            messagebox.showerror("Error", "Prestamo no encontrado.")
            return

        ventana = Toplevel(self.ventana)
        ventana.title("Actualizar Prestamo")

        tkinter.Label(ventana, text="Fecha de Prestamo:").grid(row=1, column=0)
        tkinter.Label(ventana, text="Fecha de Devolucion:").grid(row=2, column=0)
        tkinter.Label(ventana,text="dni_usuario").grid(row=3,column=0)
        tkinter.Label(ventana, text="Id Libro:").grid(row=4, column=0)

        fecha_prestamo = tkinter.Entry(ventana)
        fecha_devolucion = tkinter.Entry(ventana)
        dni_usuario = tkinter.Entry(ventana)
        id_libro = tkinter.Entry(ventana)

        fecha_prestamo.grid(row=1, column=1)
        fecha_devolucion.grid(row=2, column=1)
        dni_usuario.grid(row=3,column=1)
        id_libro.grid(row=4,column=1)

        # Cargar datos actuales
        fecha_prestamo.insert(0, prestamo_info[0][1])
        fecha_devolucion.insert(0, prestamo_info[0][2])
        dni_usuario.insert(0,prestamo_info[0][3])
        id_libro.insert(0, prestamo_info[0][4])

        def actualizar():
            msg = self.prestamo_bd.actualizar_prestamo(id_prestamo, dni_usuario.get(), fecha_prestamo.get(), fecha_devolucion.get(),id_libro.get())
            messagebox.showinfo("Información", msg)
            ventana.destroy()

        tkinter.Button(ventana, text="Actualizar", command=actualizar).grid(row=5, column=0, columnspan=2)

    def mostrar_eliminacion_prestamo(self):
        id_prestamo = simpledialog.askinteger("Eliminar Prestamo", "Ingrese el Id del Prestamo a eliminar:")
        if id_prestamo:
            msg = self.prestamo_bd.eliminar_prestamo(id_prestamo)
            messagebox.showinfo("Información", msg)

    def mostrar_prestamos(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Ver Prestamos")

        listbox = tkinter.Listbox(ventana, width=60)
        listbox.pack()

        for cliente in self.prestamo_bd.ver_prestamos():
            listbox.insert(tkinter.END, cliente)

    def __del__(self):
        # Cerrar conexión al final
        self.db.desconectar()