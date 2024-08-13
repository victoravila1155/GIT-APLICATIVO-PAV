from tkinter import messagebox

def mostrar_cerrar(self):
    # Mostrar cuadro de diálogo de confirmación
    respuesta = messagebox.askyesno("Cerrar Sesión", "¿Está seguro de que desea cerrar sesión?")
    if respuesta:
        self.destroy()
