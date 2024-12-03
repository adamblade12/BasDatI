import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel
from conexion import bd
from gui_usuarios import gui_usuario
from gui_libro import gui_libro
from gui_pagos import gui_pagos
from gui_prestamos import gui_prestamos

class VentanaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Biblioteca")

        # Menú principal
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        # ... (código del menú)

        # Botones en la ventana principal
        tk.Button(self.root, text="Usuarios", command=self.mostrar_ventana_usuario).pack(pady=5)
        tk.Button(self.root, text="Libros", command=self.mostrar_ventana_libro).pack(pady=5)
        tk.Button(self.root, text="Pagos", command=self.mostrar_ventana_pagos).pack(pady=5)
        tk.Button(self.root, text="Prestamos", command=self.mostrar_ventana_prestamos).pack(pady=5)

        # ... (otros botones)

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_todas_ventanas)

        self.root.mainloop()

    def mostrar_ventana_usuario(self):
        ventana_usuario = gui_usuario(self.root)
        # ... (código de la ventana de registro)

    def mostrar_ventana_libro(self):
        ventana_libro = gui_libro(self.root)

    def mostrar_ventana_pagos(self):
        ventana_pagos = gui_pagos(self.root)

    def mostrar_ventana_prestamos(self):
        ventana_prestamos = gui_prestamos(self.root)

    def cerrar_todas_ventanas(self):
        self.root.quit()

if __name__ == "__main__":
    ventana_principal = VentanaPrincipal()