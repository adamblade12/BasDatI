import tkinter
from tkinter import messagebox, simpledialog, Toplevel
from conexion import bd
from Usuarios import Usuario

class gui_usuario:
    def __init__(self,padre) -> None:
        self.db = bd(host="localhost", user="root", password="4123", database="biblioteca")
        self.db.conectar()

        self.usuario_bd = Usuario(self.db)

        self.ventana = Toplevel(padre)
        self.ventana.title("Usuarios")

        tkinter.Button(self.ventana, text="Registrar Usuario", command=self.mostrar_registro_usuario).pack(pady=5)
        tkinter.Button(self.ventana, text="Actualizar Usuario", command=self.mostrar_actualizacion_usuario).pack(pady=5)
        tkinter.Button(self.ventana, text="Eliminar Usuario", command=self.mostrar_eliminacion_usuario).pack(pady=5)
        tkinter.Button(self.ventana, text="Ver Usuarios", command=self.mostrar_usuarios).pack(pady=5)
        tkinter.Button(self.ventana, text="Buscar Usuario por Nombre", command=self.mostrar_busqueda_usuario).pack(pady=5)

        self.ventana.mainloop()

    

    def mostrar_busqueda_usuario(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Buscar Usuario por Nombre o Apellido")

        tkinter.Label(ventana, text="Nombre:").grid(row=0, column=0)
        tkinter.Label(ventana, text="Apellido:").grid(row=1, column=0)

        nombre = tkinter.Entry(ventana)
        apellido = tkinter.Entry(ventana)
        nombre.grid(row=0, column=1)                    
        apellido.grid(row=1, column=1)               

        listbox_resultados = tkinter.Listbox(ventana, width=60)
        listbox_resultados.grid(row=3, column=0, columnspan=2)

        def buscar():
            resultados = self.usuario_bd.buscar_usuario_por_nombre(nombre.get(), apellido.get())
            listbox_resultados.delete(0, tkinter.END)  # Limpiar resultados previos
            for cliente in resultados:
                listbox_resultados.insert(tkinter.END, cliente)

        tkinter.Button(ventana, text="Buscar", command=buscar).grid(row=2, column=0, columnspan=2)

    def mostrar_registro_usuario(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Registrar Usuario")

        tkinter.Label(ventana, text="DNI:").grid(row=0,column=0)
        tkinter.Label(ventana, text="Nombre:").grid(row=1, column=0)
        tkinter.Label(ventana, text="Apellido:").grid(row=2, column=0)
        tkinter.Label(ventana, text="Fecha de Inscripcion:").grid(row=3, column=0)

        dni_usuario = tkinter.Entry(ventana)
        nombre = tkinter.Entry(ventana)
        apellido = tkinter.Entry(ventana)
        fecha_inscripcion = tkinter.Entry(ventana)

        dni_usuario.grid(row=0,column=1)
        nombre.grid(row=1, column=1)
        apellido.grid(row=2, column=1)
        fecha_inscripcion.grid(row=3,column=1)

        def registrar(self):
            msg = self.usuario_bd.registrar_usuario(dni_usuario.get(),nombre.get(), apellido.get(), fecha_inscripcion.get())
            messagebox.showinfo("Información", msg)
            ventana.destroy()

        tkinter.Button(ventana, text="Registrar", command=registrar).grid(row=5, column=0, columnspan=2)

    def mostrar_actualizacion_usuario(self):
        dni_usuario = simpledialog.askinteger("Actualizar Usuario", "Ingrese el DNI del Usuario a actualizar:")
        cliente_info = self.usuario_bd.ver_usuario(dni_usuario)

        if not cliente_info:
            messagebox.showerror("Error", "Usuario no encontrado.")
            return

        ventana = Toplevel(self.ventana)
        ventana.title("Actualizar Usuario")

        tkinter.Label(ventana, text="Nombre:").grid(row=0, column=0)
        tkinter.Label(ventana, text="Apellido:").grid(row=1, column=0)
        tkinter.Label(ventana, text="Fecha de Inscripcion:").grid(row=2, column=0)

        nombre = tkinter.Entry(ventana)
        apellido = tkinter.Entry(ventana)
        fecha_inscripcion = tkinter.Entry(ventana)

        nombre.grid(row=1, column=1)
        apellido.grid(row=2, column=1)
        fecha_inscripcion.grid(row=3,column=1)

        # Cargar datos actuales
        nombre.insert(0, cliente_info[0][1])
        apellido.insert(0, cliente_info[0][2])
        fecha_inscripcion.insert(0, cliente_info[0][3])

        def actualizar():
            msg = self.usuario_bd.actualizar_usuario(dni_usuario, nombre.get(), apellido.get(), fecha_inscripcion.get())
            messagebox.showinfo("Información", msg)
            ventana.destroy()

        tkinter.Button(ventana, text="Actualizar", command=actualizar).grid(row=5, column=0, columnspan=2)

    def mostrar_eliminacion_usuario(self):
        dni_usuario = simpledialog.askinteger("Eliminar Usuario", "Ingrese el DNI del Usuario a eliminar:")
        if dni_usuario:
            msg = self.usuario_bd.eliminar_usuario(dni_usuario)
            messagebox.showinfo("Información", msg)

    def mostrar_usuarios(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Ver Usuarios")

        listbox = tkinter.Listbox(ventana, width=60)
        listbox.pack()

        for cliente in self.usuario_bd.ver_usuarios():
            listbox.insert(tkinter.END, cliente)

    def __del__(self):
        # Cerrar conexión al final
        self.db.desconectar()
    

    
