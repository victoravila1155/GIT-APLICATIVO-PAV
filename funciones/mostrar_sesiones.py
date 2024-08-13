import tkinter as tk
from tkinter import messagebox
import json
import webbrowser

def mostrar_sesiones(parent):
    # Elimina los widgets existentes
    for widget in parent.cuerpo_principal.winfo_children():
        widget.destroy()

    # Crear un marco para contener el título y las sesiones
    contenedor_frame = tk.Frame(parent.cuerpo_principal, bg="white", bd=2, relief=tk.SOLID)
    contenedor_frame.pack(pady=10, padx=10, fill=tk.X, anchor='n')

    # Crear el marco y el título
    titulo_frame = tk.Frame(contenedor_frame, bg="#105494")
    titulo_frame.pack(fill=tk.X)
    titulo_label = tk.Label(titulo_frame, text="MIS SESIONES", font=("Helvetica", 18, "bold"), padx=10, pady=10, bg="#105494", fg="white")
    titulo_label.pack()

    # Crear un marco para centrar las sesiones en el medio de la ventana
    centrar_frame = tk.Frame(contenedor_frame, bg="white")
    centrar_frame.pack(pady=5, padx=10, fill=tk.X)

    # Leer las sesiones guardadas
    sesiones = leer_sesiones_guardadas()

    # Crear los cuadros de las sesiones
    for sesion in sesiones:
        sesion_frame = tk.Frame(centrar_frame, bg="white", relief=tk.RAISED, borderwidth=1)
        sesion_frame.pack(side=tk.LEFT, padx=10, pady=5)

        tk.Label(sesion_frame, text=sesion["tipo"], bg="#5E9FFF", font=("Helvetica", 10, "bold")).pack(fill=tk.X, pady=(5, 2))
        tk.Label(sesion_frame, text=sesion["nivel"], font=("Helvetica", 10)).pack(pady=(0, 2))
        tk.Label(sesion_frame, text=f"{sesion['inicio']} a {sesion['fin']}", font=("Helvetica", 10)).pack(pady=(0, 2))
        tk.Label(sesion_frame, text=sesion["fecha"], font=("Helvetica", 10)).pack(pady=(0, 5))
        
        ingresar_button = tk.Button(sesion_frame, text="Ingresar", font=("Helvetica", 10, "bold"), bg="#2b78e4", fg="white", command=lambda: abrir_google_meet())
        ingresar_button.pack(side=tk.LEFT, padx=5, pady=5)

        cancelar_button = tk.Button(sesion_frame, text="Cancelar", font=("Helvetica", 10, "bold"), bg="#e42b2b", fg="white", command=lambda s=sesion: confirmar_cancelar(s, parent))
        cancelar_button.pack(side=tk.LEFT, padx=5, pady=5)

def leer_sesiones_guardadas():
    try:
        with open('sesiones_guardadas.json', 'r') as file:
            sesiones = json.load(file)
    except FileNotFoundError:
        sesiones = []
    return sesiones

def mostrar_detalles(sesion, parent):
    # Crear una nueva ventana para mostrar los detalles
    detalles_ventana = tk.Toplevel(parent)
    detalles_ventana.title("Detalles de la Sesión")
    
    # Establecer el tamaño de la ventana
    ventana_ancho = 350
    ventana_alto = 200
    detalles_ventana.geometry(f"{ventana_ancho}x{ventana_alto}")

    # Centrar la ventana en la pantalla
    ventana_width = parent.winfo_screenwidth()
    ventana_height = parent.winfo_screenheight()
    x = (ventana_width - ventana_ancho) // 2
    y = (ventana_height - ventana_alto) // 2 - 20
    detalles_ventana.geometry(f"{ventana_ancho}x{ventana_alto}+{x}+{y}")

    # Título en mayúsculas, centrado y en negrita
    titulo_frame = tk.Frame(detalles_ventana, bg="#105494")
    titulo_frame.pack(fill=tk.X, pady=(10, 5))
    titulo_label = tk.Label(titulo_frame, text="CLASE AGENDADA EXITOSAMENTE", font=("Helvetica", 12, "bold"), bg="#105494", fg="white")
    titulo_label.pack(pady=10, padx=10)

    # Detalles del horario
    detalles = (f"Tipo: {sesion['tipo']}\n"
                f"Nivel: {sesion['nivel']}\n"
                f"Horario: {sesion['inicio']} a {sesion['fin']}\n"
                f"Fecha: {sesion['fecha']}")
    
    detalles_label = tk.Label(detalles_ventana, text=detalles, font=("Helvetica", 12), bg="white", justify='left')
    detalles_label.pack(pady=(0, 10), padx=10)

    # Botón para cerrar la ventana de detalles
    cerrar_button = tk.Button(detalles_ventana, text="Cerrar", font=("Helvetica", 12, "bold"), command=detalles_ventana.destroy)
    cerrar_button.pack(pady=(5, 10))

    # Ajustar el estilo de la ventana
    detalles_ventana.configure(bg="white")
    detalles_ventana.transient()
    detalles_ventana.grab_set()

def confirmar_cancelar(sesion, parent):
    respuesta = messagebox.askyesno("Confirmación", "¿Está seguro que desea cancelar la clase?")
    if respuesta:
        eliminar_sesion(sesion, parent)
        mostrar_sesiones(parent)

def eliminar_sesion(sesion_a_eliminar, parent):
    sesiones = leer_sesiones_guardadas()
    sesiones = [sesion for sesion in sesiones if sesion != sesion_a_eliminar]
    with open('sesiones_guardadas.json', 'w') as file:
        json.dump(sesiones, file)

def abrir_google_meet():
    url = "https://meet.google.com/nbe-jxgn-ovf"
    webbrowser.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Mis Reservas")

    class App:
        def __init__(self, master):
            self.cuerpo_principal = tk.Frame(master, bg="white")
            self.cuerpo_principal.pack(fill=tk.BOTH, expand=True, pady=0)
            mostrar_sesiones(self)

    app = App(root)
    root.mainloop()

