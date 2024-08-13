import tkinter as tk
from tkinter import messagebox
import ctypes
from PIL import Image, ImageTk
import webbrowser

def mostrar_material(parent):
    # Elimina los widgets existentes
    for widget in parent.cuerpo_principal.winfo_children():
        widget.destroy()

    centrar_frame = tk.Frame(parent.cuerpo_principal)
    centrar_frame.pack(pady=5, padx=10, fill=tk.X, expand=True)

    # Crear el marco y el título
    titulo_frame = tk.Frame(centrar_frame, bd=2, relief=tk.SOLID, bg="#105494")
    titulo_frame.pack(pady=10, padx=10, fill=tk.X)
    titulo_label = tk.Label(titulo_frame, text="MATERIAL UTIL", font=("Helvetica", 18, "bold"), padx=10, pady=10, bg="#105494", fg="white")
    titulo_label.pack()

    # Crear la lista de materias
    materias = ["MATEMATICAS", "INGLES", "LITERATURA", "QUIMICA", "FISICA"]

    # Diccionario para almacenar los frames
    materiales_frames = {}

    # Crear el marco principal para los materiales
    for materia in materias:
        materia_frame = tk.Frame(centrar_frame)
        materia_frame.pack(fill=tk.X, pady=5)

        # Frame que contiene los materiales
        materiales_frame = tk.Frame(materia_frame, bg="white") 
        materiales_frame.pack(fill=tk.X, padx=10, pady=5) 
        materiales_frame.pack_forget() 
        
        # Almacenar el frame de materiales en el diccionario
        materiales_frames[materia] = materiales_frame

        # Botón para expandir o contraer
        boton_materia = tk.Button(materia_frame, text=materia, relief=tk.FLAT, height=2, bg="#2b78e4", fg="white", font=("Helvetica", 10, "bold"), command=lambda m=materia: toggle_materiales(m, materiales_frames))
        boton_materia.pack(fill=tk.X, padx=10, expand=True)

        # Crear botones para cada material
        materiales = [("MATERIAL DE APOYO GUIA 1", "materialdeapoyo1.pdf"),
                       ("MATERIAL DE APOYO GUIA 2", "materialdeapoyo2.pdf"),
                       ("MATERIAL DE APOYO GUIA 3", "materialdeapoyo3.pdf")]

        for idx, (titulo, archivo) in enumerate(materiales):
            material_button = tk.Button(materiales_frame, text=titulo, relief=tk.FLAT, bg="#C4DCFF", fg="black", font=("Helvetica", 10, "bold"), command=lambda a=archivo: mostrar_detalle_material(materia))
            material_button.pack(fill=tk.X, padx=10, pady=(5 if idx > 0 else 10))

def toggle_materiales(materia, materiales_frames):
    # Ocultar todas las materiales y solo mostrar el seleccionado
    for m, frame in materiales_frames.items():
        if m == materia:
            if frame.winfo_ismapped():
                frame.pack_forget()
            else:
                frame.pack(fill=tk.X)
        else:
            frame.pack_forget()

def mostrar_detalle_material(materia):
    # Crear una nueva ventana
    detalle_ventana = tk.Toplevel()
    detalle_ventana.geometry("800x600")
    detalle_ventana.title(f"Detalle de {materia}")

    # Altura de la pantalla
    user32 = ctypes.windll.user32
    screen_height = user32.GetSystemMetrics(1)
    barra_tareas_height = user32.GetSystemMetrics(4)
    usable_height = screen_height - barra_tareas_height - 90

    detalle_ventana.geometry(f"800x{usable_height}+100+0")

    # Centrar el material en el medio de la ventana
    centrar_frame = tk.Frame(detalle_ventana)
    centrar_frame.pack(pady=5, padx=10, fill=tk.X, expand=True)

    # Crear el marco y el título
    titulo_frame = tk.Frame(centrar_frame, bd=2, relief=tk.SOLID, bg="#105494")
    titulo_frame.pack(pady=10, padx=10, fill=tk.X)
    titulo_label = tk.Label(titulo_frame, text="MATERIAL", font=("Helvetica", 18, "bold"), padx=10, pady=10, bg="#105494", fg="white")
    titulo_label.pack()

    # Crear el marco para la lista de materiales y videos
    contenido_frame = tk.Frame(centrar_frame, bd=2, relief=tk.SOLID, bg="#FFFFFF")
    contenido_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Crear las secciones de material y video
    seccion_material = tk.LabelFrame(contenido_frame, text="MATERIAL", font=("Helvetica", 12, "bold"))
    seccion_material.pack(fill=tk.X, padx=10, pady=5)

    seccion_videos = tk.LabelFrame(contenido_frame, text="VIDEOS DE INTERES", font=("Helvetica", 12, "bold"))
    seccion_videos.pack(fill=tk.X, padx=10, pady=5)

    # Agregar los enlaces de materiales
    materiales = [("MATERIAL DE APOYO 1", "materialdeapoyo1.pdf"),
                  ("MATERIAL DE APOYO 2", "materialdeapoyo2.pdf"),
                  ("MATERIAL DE APOYO 3", "materialdeapoyo3.pdf")]

    for titulo, archivo in materiales:
        enlace = tk.Label(seccion_material, text=f"{titulo} {archivo}", fg="blue", cursor="hand2", font=("Helvetica", 10, "underline"))
        enlace.pack(anchor="w")
        enlace.bind("<Button-1>", lambda e, a=archivo: abrir_archivo(a))

    # Agregar los enlaces de videos con nombres y URLs
    videos = [("MATERIAL DE APOYO 1", "materialdeapoyo1.VDO", "https://www.youtube.com/watch?v=zRjbwI4K7xc&ab_channel=EDteam"),
              ("MATERIAL DE APOYO 2", "materialdeapoyo2.VDO", "https://www.youtube.com/watch?v=example2"),
              ("MATERIAL DE APOYO 3", "materialdeapoyo3.VDO", "https://www.youtube.com/watch?v=example3")]

    for titulo, archivo, url in videos:
        enlace = tk.Label(seccion_videos, text=f"{titulo} {archivo}", fg="blue", cursor="hand2", font=("Helvetica", 10, "underline"))
        enlace.pack(anchor="w")
        enlace.bind("<Button-1>", lambda e, u=url: abrir_url(u))

    # Mostrar la imagen
    img_path = 'imagenes/apoyo.png'
    img = Image.open(img_path)
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(contenido_frame, image=img, bd=0, bg="white", highlightthickness=0)
    img_label.image = img
    img_label.pack(pady=10, anchor="e")

def abrir_archivo(archivo):
    messagebox.showinfo("Abrir archivo", f"Abrir el archivo: {archivo}")

def abrir_url(url):
    webbrowser.open(url)

















