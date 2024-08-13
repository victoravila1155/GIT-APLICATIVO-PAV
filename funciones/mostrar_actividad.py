import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import ctypes
import os

# Variable global para almacenar el nombre del usuario
user_name = "victor avila"

def mostrar_actividad(parent):
    # Elimina los widgets existentes
    for widget in parent.cuerpo_principal.winfo_children():
        widget.destroy()

    centrar_frame = tk.Frame(parent.cuerpo_principal)
    centrar_frame.pack(pady=5, padx=10, fill=tk.X, expand=True)

    # Crear el marco y el título
    titulo_frame = tk.Frame(centrar_frame, bd=2, relief=tk.SOLID, bg="#105494")
    titulo_frame.pack(pady=10, padx=10, fill=tk.X)
    titulo_label = tk.Label(titulo_frame, text="ACTIVIDADES", font=("Helvetica", 18, "bold"), padx=10, pady=10, bg="#105494", fg="white")
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

        # Agregar actividades de ejemplo
        agregar_actividades(clases_frame, parent)

def toggle_clases(materia_frame):
    clases_frame = materia_frame.winfo_children()[1]
    if clases_frame.winfo_viewable():
        clases_frame.pack_forget()
    else:
        clases_frame.pack(fill=tk.X, padx=10, pady=5)

def agregar_actividades(clases_frame, parent):
    contenedor_actividades = tk.Frame(clases_frame, bg="white")
    contenedor_actividades.pack(fill=tk.X, pady=5)

    actividades = ["ACTIVIDAD 1", "ACTIVIDAD 2", "ACTIVIDAD 3"]

    for actividad in actividades:
        actividad_button = tk.Button(contenedor_actividades, text=actividad, relief=tk.RAISED, height=2, bg="#FFFFFF", font=("Helvetica", 10, "bold"), command=lambda a=actividad: mostrar_detalle_actividad(a))
        actividad_button.pack(fill=tk.X, padx=10, pady=5)

def mostrar_detalle_actividad(actividad):
    # Crear una nueva ventana
    detalle_ventana = tk.Toplevel()
    detalle_ventana.geometry("800x600")
    detalle_ventana.title(f"Detalle de {actividad}")

    # Altura de la pantalla
    user32 = ctypes.windll.user32
    screen_height = user32.GetSystemMetrics(1)
    barra_tareas_height = user32.GetSystemMetrics(4)
    usable_height = screen_height - barra_tareas_height - 90

    detalle_ventana.geometry(f"800x{usable_height}+100+0")

    # Centrar la actividad en el medio de la ventana
    centrar_frame = tk.Frame(detalle_ventana)
    centrar_frame.pack(pady=5, padx=10, fill=tk.X, expand=True)

    # Detalles de la actividad
    detalle_frame = tk.Frame(centrar_frame, bd=2, relief=tk.SOLID, bg="#FFFFFF")
    detalle_frame.pack(pady=10, padx=10, fill=tk.X)

    # Marco y el título
    titulo_frame = tk.Frame(detalle_frame, bg="#105494")
    titulo_frame.pack(fill=tk.X)
    titulo_label = tk.Label(titulo_frame, text="ACTIVIDAD", font=("Helvetica", 18, "bold"), padx=10, pady=10, bg="#105494", fg="white")
    titulo_label.pack()

    actividad_label = tk.Label(detalle_frame, text=actividad, font=("Helvetica", 14, "bold"), padx=10, pady=5, bg="#FFFFFF")  # Título más grande
    actividad_label.pack(anchor="w", padx=10)

    link_label = tk.Label(detalle_frame, text=f"{actividad}_guiaactividad1.pdf", font=("Helvetica", 10), fg="blue", cursor="hand2", bg="#FFFFFF")
    link_label.pack(anchor="w", padx=18, pady=(10, 0))

    # "Introducción a la Actividad"
    introduccion_label = tk.Label(detalle_frame, text="Introducción a la Actividad", font=("Helvetica", 12, "bold"), bg="#FFFFFF", padx=10, pady=5)
    introduccion_label.pack(anchor="w", pady=(10, 5), padx=10)

    # Label para el párrafo
    descripcion_text = tk.Text(detalle_frame, font=("Helvetica", 10), bg="#FFFFFF", wrap="word", height=4, relief="flat")
    descripcion_text.insert(tk.END, "Esta sección presenta la actividad a realizar, explicando su propósito, objetivos, metodología y recursos necesarios. Proporciona el contexto y la importancia de la actividad dentro del proyecto o curso. Al finalizar, los participantes deben entender claramente lo que se espera de ellos, los pasos a seguir y los resultados esperados.")
    descripcion_text.config(state="disabled")
    descripcion_text.pack(fill=tk.BOTH, padx=18, pady=(5, 0), expand=True) 

    # "AGREGAR ENTREGA" título 
    entregar_label = tk.Label(detalle_frame, text="AGREGAR ENTREGA", font=("Helvetica", 18, "bold"), bg="#105494", fg="white", padx=10, pady=10)
    entregar_label.pack(fill=tk.X)

    # Marco para respuesta
    respuesta_frame = tk.Frame(detalle_frame, bg="#FFFFFF")
    respuesta_frame.pack(fill=tk.X, pady=5)

    respuesta_label = tk.Label(respuesta_frame, text="AGREGAR ENTREGA", font=("Helvetica", 12, "bold"), padx=10, pady=5, bg="#FFFFFF")
    respuesta_label.pack(anchor="w", padx=10)

    respuesta_text = tk.Entry(respuesta_frame, font=("Helvetica", 10), bg="#f0f0f0")
    respuesta_text.pack(fill=tk.X, padx=10, pady=5)
    respuesta_text.bind("<Return>", lambda event, entry=respuesta_text, parent=respuesta_frame: agregar_comentario(entry, parent))

    comentarios_frame = tk.Frame(respuesta_frame, bg="#FFFFFF")
    comentarios_frame.pack(fill=tk.X, pady=5)

    # Adjuntar archivo y vínculo
    archivo_frame = tk.Frame(respuesta_frame, bg="#FFFFFF")
    archivo_frame.pack(fill=tk.X, padx=10, pady=5)
    archivo_button = tk.Button(archivo_frame, text="adjuntar archivo", font=("Helvetica", 10), bg="#2b78e4", fg="white", command=lambda: adjuntar_archivo(archivo_frame))
    archivo_button.pack(fill=tk.X)

    vinculo_frame = tk.Frame(respuesta_frame, bg="#FFFFFF")
    vinculo_frame.pack(fill=tk.X, padx=10, pady=5)
    vinculo_button = tk.Button(vinculo_frame, text="adjuntar vínculo", font=("Helvetica", 10), bg="#2b78e4", fg="white", command=lambda: adjuntar_vinculo(vinculo_frame))
    vinculo_button.pack(fill=tk.X)

    # Botón "REALIZAR ENTREGA"
    realizar_entrega_button = tk.Button(respuesta_frame, text="REALIZAR ENTREGA", font=("Helvetica", 10, "bold"), bg="#105494", fg="white", width=20, height=2, command=realizar_entrega)
    realizar_entrega_button.pack(pady=10)
    realizar_entrega_button.pack_configure(anchor="center")

def adjuntar_archivo(parent_frame):
    filetypes = [
        ("Word files", "*.doc *.docx"),
        ("Excel files", "*.xls *.xlsx"),
        ("PDF files", "*.pdf"),
        ("All files", "*.*")
    ]
    filepath = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=filetypes)
    
    if filepath:
        archivo_label = tk.Label(parent_frame, text=os.path.basename(filepath), font=("Helvetica", 10, "underline"), fg="blue", bg="white", padx=10, pady=5)
        archivo_label.pack(fill=tk.X, pady=(5, 0))

def adjuntar_vinculo(parent_frame):
    vinculo_entry = tk.Entry(parent_frame, font=("Helvetica", 10), bg="#f0f0f0")
    vinculo_entry.pack(fill=tk.X, padx=10, pady=5)
    vinculo_entry.bind("<Return>", lambda event, entry=vinculo_entry, parent=parent_frame: agregar_vinculo(entry, parent))

def agregar_vinculo(entry, parent_frame):
    vinculo = entry.get()
    if vinculo:
        vinculo_label = tk.Label(parent_frame, text=vinculo, font=("Helvetica", 10, "underline"), fg="blue", bg="white", padx=10, pady=5, cursor="hand2")
        vinculo_label.pack(fill=tk.X, pady=(5, 0))
        vinculo_label.bind("<Button-1>", lambda e: abrir_vinculo(vinculo))
        entry.destroy()

def abrir_vinculo(vinculo):
    os.system(f"start {vinculo}")

def realizar_entrega():
    messagebox.showinfo("Entrega", "Entrega realizada con éxito")

def agregar_comentario(entry, parent_frame):
    global user_name

    comentario = entry.get()
    if comentario:
        comentario_frame = tk.Frame(parent_frame, bd=1, relief=tk.SOLID, bg="lightgrey")
        comentario_frame.pack(fill=tk.X, padx=10, pady=5)

        # Marco para el usuario y la fecha
        usuario_fecha_frame = tk.Frame(comentario_frame, bg="lightgrey")
        usuario_fecha_frame.pack(side=tk.RIGHT, padx=10, pady=5, anchor="e")

        usuario_label = tk.Label(usuario_fecha_frame, text=f"Usuario: {user_name}", font=("Helvetica", 10, "bold"), bg="lightgrey")
        usuario_label.pack(anchor="e")

        fecha_label = tk.Label(usuario_fecha_frame, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), font=("Helvetica", 8), bg="lightgrey")
        fecha_label.pack(anchor="e")

        comentario_label = tk.Label(comentario_frame, text=comentario, font=("Helvetica", 10), bg="white", padx=10, pady=5)
        comentario_label.pack(fill=tk.X, pady=(5, 10))

        entry.delete(0, tk.END)

        # Coloca el nuevo comentario
        comentario_frame.pack(in_=parent_frame, after=entry)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Registrar Actividad")

    class App:
        def __init__(self, master):
            self.cuerpo_principal = tk.Frame(master)
            self.cuerpo_principal.pack(fill=tk.BOTH, expand=True)
            mostrar_actividad(self)





























