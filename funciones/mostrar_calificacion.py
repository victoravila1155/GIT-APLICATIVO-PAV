import tkinter as tk

def mostrar_calificacion(parent):
    # Elimina los widgets existentes
    for widget in parent.cuerpo_principal.winfo_children():
        widget.destroy()

    centrar_frame = tk.Frame(parent.cuerpo_principal)
    centrar_frame.pack(pady=5, padx=10, fill=tk.X, expand=True)

    # Crear el marco y el título
    titulo_frame = tk.Frame(centrar_frame, bd=2, relief=tk.SOLID, bg="#105494")
    titulo_frame.pack(pady=10, padx=10, fill=tk.X)
    titulo_label = tk.Label(titulo_frame, text="CALIFICACIONES", font=("Helvetica", 18, "bold"), padx=10, pady=10, bg="#105494", fg="white")
    titulo_label.pack()

    # Crear la lista de materias
    materias = ["MATEMATICAS", "INGLES", "LITERATURA", "QUIMICA", "FISICA"]

    # Crear el marco principal para las materias
    for materia in materias:
        materia_frame = tk.Frame(centrar_frame)
        materia_frame.pack(fill=tk.X, pady=5)

        materia_button = tk.Button(materia_frame, text=materia, relief=tk.FLAT, height=2, bg="#2b78e4", fg="white", font=("Helvetica", 10, "bold"), command=lambda m=materia_frame: toggle_calificaciones(m))
        materia_button.pack(fill=tk.X, padx=10, expand=True)

        # Crear el marco para las calificaciones
        calificaciones_frame = tk.Frame(materia_frame, bg="white")
        calificaciones_frame.pack(fill=tk.X, padx=10, pady=5)
        calificaciones_frame.pack_forget()

        # Agregar calificaciones de ejemplo
        agregar_calificaciones(calificaciones_frame)

def toggle_calificaciones(materia_frame):
    calificaciones_frame = materia_frame.winfo_children()[1]
    if calificaciones_frame.winfo_viewable():
        calificaciones_frame.pack_forget()
    else:
        calificaciones_frame.pack(fill=tk.X, padx=10, pady=5)

def agregar_calificaciones(calificaciones_frame):
    centrar_frame = tk.Frame(calificaciones_frame, bg="white")
    centrar_frame.pack(fill=tk.X, pady=5)

    actividades = [
        ("ACTIVIDAD 1", "5.0"),
        ("ACTIVIDAD 2", "4.0"),
        ("ACTIVIDAD 3", "5.0"),
    ]

    for actividad, calificacion in actividades:
        fila_frame = tk.Frame(centrar_frame, bd=1, relief=tk.SOLID, bg="#C4DCFF")
        fila_frame.pack(fill=tk.X, padx=10, pady=2)

        # ACTIVIDAD 
        actividad_label = tk.Label(fila_frame, text=actividad, font=("Helvetica", 12), padx=5, pady=5, bg="#5E9FFF", fg="white", anchor='w')
        actividad_label.pack(side=tk.LEFT, padx=(5, 10), pady=5, fill=tk.X, expand=True)
        
        # marco actividad y calificación
        separador = tk.Frame(fila_frame, width=5, bg="#C4DCFF")
        separador.pack(side=tk.LEFT, padx=(10, 10))

        # CALIFICACION
        calificacion_label = tk.Label(fila_frame, text=calificacion, font=("Helvetica", 12), padx=5, pady=5, bg="#C4DCFF", fg="black")
        calificacion_label.pack(side=tk.LEFT, padx=(10, 5), pady=5, fill=tk.X, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Registrar Actividad")

    class App:
        def __init__(self, master):
            self.cuerpo_principal = tk.Frame(master)
            self.cuerpo_principal.pack(fill=tk.BOTH, expand=True)
            mostrar_calificacion(self)


    






