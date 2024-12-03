import tkinter
from tkinter import messagebox, simpledialog, Toplevel
from conexion import bd
from Libro import Libro

class gui_libro:
    def __init__(self,padre) -> None:
        self.db = bd(host="localhost", user="root", password="4123", database="biblioteca")
        self.db.conectar()
    

        self.libro_db = Libro(self.db)

        self.ventana = Toplevel(padre)
        self.ventana.title("Libros")

        tkinter.Button(self.ventana, text="Registrar Libro", command=self.mostrar_registro_libro).pack(pady=5)
        tkinter.Button(self.ventana, text="Actualizar Libro", command=self.mostrar_actualizacion_libro).pack(pady=5)
        tkinter.Button(self.ventana, text="Eliminar Libro", command=self.mostrar_eliminacion_libro).pack(pady=5)
        tkinter.Button(self.ventana, text="Ver Libros", command=self.mostrar_libros).pack(pady=5)
        tkinter.Button(self.ventana, text="Buscar Libro por Titulo", command=self.mostrar_busqueda_libro).pack(pady=5)

        self.ventana.mainloop()

    def mostrar_busqueda_libro(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Buscar Libro por titulo")

        tkinter.Label(ventana, text="Titulo:").grid(row=0, column=0)

        titulo = tkinter.Entry(ventana)
        titulo.grid(row=0, column=1)

        listbox_resultados = tkinter.Listbox(ventana, width=60)
        listbox_resultados.grid(row=3, column=0, columnspan=2)

        def buscar():
            resultados = self.libro_db.buscar_libro_por_titulo(titulo.get())
            listbox_resultados.delete(0, tkinter.END)  # Limpiar resultados previos
            for libro in resultados:
                listbox_resultados.insert(tkinter.END, libro)

        tkinter.Button(ventana, text="Buscar", command=buscar).grid(row=2, column=0, columnspan=2)

    def mostrar_registro_libro(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Registrar Libro")

        tkinter.Label(ventana, text="Titulo:").grid(row=0,column=0)
        tkinter.Label(ventana, text="Autor:").grid(row=1, column=0)
        tkinter.Label(ventana, text="Descripcion:").grid(row=2, column=0)

        titulo = tkinter.Entry(ventana)
        autor = tkinter.Entry(ventana)
        descripcion = tkinter.Entry(ventana)

        titulo.grid(row=0,column=1)
        autor.grid(row=1, column=1)
        descripcion.grid(row=2, column=1)

        def registrar():
            msg = self.libro_db.registrar_libro(titulo.get(),autor.get(), descripcion.get())
            messagebox.showinfo("Información", msg)
            ventana.destroy()

        tkinter.Button(ventana, text="Registrar", command=registrar).grid(row=5, column=0, columnspan=2)

    def mostrar_actualizacion_libro(self):
        id_libro = simpledialog.askinteger("Actualizar Libro", "Ingrese el id del Libro a actualizar:")
        libro_info = self.libro_db.ver_libro(id_libro)

        if not libro_info:
            messagebox.showerror("Error", "Libro no encontrado.")
            return

        ventana = Toplevel(self.ventana)
        ventana.title("Actualizar Usuario")

        tkinter.Label(ventana, text="Titulo:").grid(row=0, column=0)
        tkinter.Label(ventana, text="Autor:").grid(row=1, column=0)
        tkinter.Label(ventana, text="Descripcion:").grid(row=2, column=0)

        titulo = tkinter.Entry(ventana)
        autor = tkinter.Entry(ventana)
        descripcion = tkinter.Entry(ventana)

        titulo.grid(row=1, column=1)
        autor.grid(row=2, column=1)
        descripcion.grid(row=3,column=1)

        # Cargar datos actuales
        titulo.insert(0, libro_info[0][1])
        autor.insert(0, libro_info[0][2])
        descripcion.insert(0, libro_info[0][3])

        def actualizar():
            msg = self.libro_db.actualizar_libro(id_libro, titulo.get(), autor.get(), descripcion.get())
            messagebox.showinfo("Información", msg)
            ventana.destroy()

        tkinter.Button(ventana, text="Actualizar", command=actualizar).grid(row=5, column=0, columnspan=2)

    def mostrar_eliminacion_libro(self):
        id_libro = simpledialog.askinteger("Eliminar Libro", "Ingrese el Id del Libro a eliminar:")
        if id_libro:
            msg = self.libro_db.eliminar_libro(id_libro)
            messagebox.showinfo("Información", msg)

    def mostrar_libros(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Ver Libros")

        listbox = tkinter.Listbox(ventana, width=60)
        listbox.pack()

        for Libro in self.libro_db.ver_libros():
            listbox.insert(tkinter.END, Libro)

    def __del__(self):
        # Cerrar conexión al final
        self.db.desconectar()