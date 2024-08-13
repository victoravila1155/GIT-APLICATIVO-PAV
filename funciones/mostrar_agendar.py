import tkinter as tk
from tkinter import messagebox
import json

def mostrar_agendar(parent):
    # Elimina los widgets existentes
    for widget in parent.cuerpo_principal.winfo_children():
        widget.destroy()

    # Crear un marco para centrar las materias en el medio de la ventana
    centrar_frame = tk.Frame(parent.cuerpo_principal)
    centrar_frame.pack(pady=5, padx=10, fill=tk.X, expand=True)

    # Crear el marco y el título
    titulo_frame = tk.Frame(centrar_frame, bd=2, relief=tk.SOLID, bg="#105494")
    titulo_frame.pack(pady=10, padx=10, fill=tk.X)
    titulo_label = tk.Label(titulo_frame, text="AGENDAR CLASE", font=("Helvetica", 18, "bold"), padx=10, pady=10, bg="#105494", fg="white")
    titulo_label.pack()

    # Crear la lista de materias
    materias = ["MATEMATICAS", "INGLES", "LITERATURA", "QUIMICA", "FISICA"]

    # Crear el marco principal para las materias
    for materia in materias:
        materia_frame = tk.Frame(centrar_frame)
        materia_frame.pack(fill=tk.X, pady=5)

        materia_button = tk.Button(materia_frame, text=materia, relief=tk.FLAT, height=2, bg="#2b78e4", fg="white", font=("Helvetica", 10, "bold"), command=lambda m=materia_frame: toggle_clases(m))
        materia_button.pack(fill=tk.X, padx=10, expand=True)

        # Crear el marco para las clases sin borde negro
        clases_frame = tk.Frame(materia_frame, bg="white")
        clases_frame.pack(fill=tk.X, padx=10, pady=5)
        clases_frame.pack_forget()

        # Agregar horarios de ejemplo
        agregar_horarios(clases_frame, materia, parent)  

def toggle_clases(materia_frame):
    clases_frame = materia_frame.winfo_children()[1]
    if clases_frame.winfo_viewable():
        clases_frame.pack_forget()
    else:
        clases_frame.pack(fill=tk.X, padx=10, pady=5)

def agregar_horarios(clases_frame, materia, parent):
    contenedor_horarios = tk.Frame(clases_frame, bg="white")
    contenedor_horarios.pack(pady=5)

    horarios = [
        {"tipo": "Clase", "nivel": materia, "inicio": "16:30", "fin": "18:00", "fecha": "Friday 26/07/2024"},
        {"tipo": "Clase", "nivel": materia, "inicio": "18:00", "fin": "19:30", "fecha": "Friday 26/07/2024"},
        {"tipo": "refuerzo", "nivel": materia, "inicio": "18:00", "fin": "19:30", "fecha": "Friday 26/07/2024"},
        {"tipo": "Clase", "nivel": materia, "inicio": "19:30", "fin": "21:00", "fecha": "Friday 26/07/2024"}
    ]

    for horario in horarios:
        horario_frame = tk.Frame(contenedor_horarios, bg="#C4DCFF", relief=tk.RAISED, borderwidth=1)
        horario_frame.pack(side=tk.LEFT, padx=10, pady=5)

        tk.Label(horario_frame, text=horario["tipo"], bg="#5E9FFF", font=("Helvetica", 10, "bold")).pack(fill=tk.X, pady=(5, 2))
        tk.Label(horario_frame, text=horario["nivel"], font=("Helvetica", 10)).pack(pady=(0, 2))
        tk.Label(horario_frame, text=f"{horario['inicio']} a {horario['fin']}", font=("Helvetica", 10)).pack(pady=(0, 2))
        tk.Label(horario_frame, text=horario["fecha"], font=("Helvetica", 10)).pack(pady=(0, 5))
        
        button = tk.Button(horario_frame, text="Agendar", font=("Helvetica", 10, "bold"), command=lambda h=horario: guardar_sesion(h))
        button.pack(pady=5)

def guardar_sesion(horario):
    try:
        with open('sesiones_guardadas.json', 'r') as file:
            sesiones = json.load(file)
    except FileNotFoundError:
        sesiones = []

    sesiones.append(horario)

    with open('sesiones_guardadas.json', 'w') as file:
        json.dump(sesiones, file, indent=4)

    messagebox.showinfo("Agendar Clase", "Clase agendada exitosamente")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Agendar Clase")

    class App:
        def __init__(self, master):
            self.cuerpo_principal = tk.Frame(master)
            self.cuerpo_principal.pack(fill=tk.BOTH, expand=True)
            mostrar_agendar(self)
