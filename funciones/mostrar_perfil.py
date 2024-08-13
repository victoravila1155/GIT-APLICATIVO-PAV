import tkinter as tk
from tkinter import messagebox

def mostrar_perfil(parent):
    # Elimina los widgets existentes
    for widget in parent.cuerpo_principal.winfo_children():
        widget.destroy()
    
    # Frame del encabezado del perfil
    header_frame = tk.Frame(parent.cuerpo_principal, bg="#105494")
    header_frame.pack(fill=tk.X, pady=10)

    # Imagen de perfil
    profile_pic = tk.Label(header_frame, text="VA", font=("Helvetica", 40, "bold"), bg="#5886CC", fg="white", width=5, height=2)
    profile_pic.grid(row=0, column=0, padx=20, rowspan=2)

    # Información del perfil
    info_frame = tk.Frame(header_frame, bg="#105494")
    info_frame.grid(row=0, column=1)

    # Etiqueta del nombre
    global name_label
    name_label = tk.Label(info_frame, text="victor avila", font=("Helvetica", 30, "bold"), fg="white", bg="#105494")
    name_label.grid(row=0, column=0, sticky="w")

    status_label = tk.Label(info_frame, text="En Línea", fg="#2ECC71", font=("Helvetica", 16, "italic"), bg="#105494")
    status_label.grid(row=1, column=0, sticky="w")

    # Etiqueta de "Estudiante"
    role_label = tk.Label(parent.cuerpo_principal, text="Estudiante", font=("Helvetica", 16, "italic"), bg="#ECF0F1", fg="#34495E")
    role_label.pack(anchor="w", padx=20)

    # Detalles del curso
    course_details_frame = tk.LabelFrame(header_frame, text="Detalles del curso", font=("Helvetica", 12, "bold"), bg="#ECF0F1", fg="#34495E")
    course_details_frame.grid(row=0, column=2, padx=(120, 20), pady=10)
    create_readonly_entry(course_details_frame, "Curso:", "Bachiller Académico", 0)

    # Actualiza tus datos
    update_data_frame = tk.LabelFrame(parent.cuerpo_principal, text="Actualiza tus datos", font=("Helvetica", 12, "bold"), bg="#ECF0F1", fg="#34495E")
    update_data_frame.pack(pady=20, padx=20, fill="both", expand="yes")

    name_entry = create_form_entry(update_data_frame, "Nombre:", "victor avila", 0)
    email_entry = create_form_entry(update_data_frame, "Email:", "prueba@gmail.com", 1)

    # Botón de actualizar
    update_button = tk.Button(parent.cuerpo_principal, text="Actualizar información básica", 
                              command=lambda: update_info(name_entry, email_entry), 
                              bg="#2980B9", fg="white", font=("Helvetica", 12, "bold"))
    update_button.pack(pady=10)

    # Detalles del usuario
    global user_name_entry
    global user_email_entry
    user_details_frame = tk.LabelFrame(parent.cuerpo_principal, text="Detalles de usuario", font=("Helvetica", 12, "bold"), bg="#ECF0F1", fg="#34495E")
    user_details_frame.pack(fill="both", expand="yes", padx=20, pady=10)
    user_name_entry = create_form_entry(user_details_frame, "Nombre:", "victor avila", 0)
    user_email_entry = create_form_entry(user_details_frame, "Email:", "victor@example.com", 1)
    create_readonly_entry(user_details_frame, "País:", "Colombia", 2)
    create_readonly_entry(user_details_frame, "Ciudad:", "Medellín", 3)

    # Actividad
    activity_details_frame = tk.LabelFrame(parent.cuerpo_principal, text="Actividad", font=("Helvetica", 12, "bold"), bg="#ECF0F1", fg="#34495E")
    activity_details_frame.pack(fill="both", expand="yes", padx=20, pady=10)
    create_form_entry(activity_details_frame, "Primera vez en la plataforma:", "01/01/2023", 0)
    create_form_entry(activity_details_frame, "Última vez en la plataforma:", "25/07/2024", 1)

def create_form_entry(parent, label_text, default_value, row):
    label = tk.Label(parent, text=label_text, font=("Helvetica", 12), bg="#ECF0F1", fg="#34495E")
    label.grid(row=row, column=0, pady=5, sticky="e")
    
    entry = tk.Entry(parent, font=("Helvetica", 12), bg="#FFFFFF", fg="#34495E")
    entry.grid(row=row, column=1, pady=5, padx=10)
    entry.insert(0, default_value)
    
    return entry

def create_readonly_entry(parent, label_text, default_value, row):
    label = tk.Label(parent, text=label_text, font=("Helvetica", 12), bg="#ECF0F1", fg="#34495E")
    label.grid(row=row, column=0, pady=5, sticky="e")
    
    entry = tk.Entry(parent, font=("Helvetica", 12), bg="#FFFFFF", fg="#34495E")
    entry.grid(row=row, column=1, pady=5, padx=10)
    entry.insert(0, default_value)
    entry.config(state='readonly')
    
    return entry

def update_info(name_entry, email_entry):
    name = name_entry.get()
    email = email_entry.get()
    
    # Actualiza la etiqueta del nombre en el encabezado del perfil
    name_label.config(text=name)
    
    # Actualiza la información en los detalles del usuario
    user_name_entry.config(state='normal')
    user_name_entry.delete(0, tk.END)
    user_name_entry.insert(0, name)
    user_name_entry.config(state='readonly')
    
    user_email_entry.config(state='normal') 
    user_email_entry.delete(0, tk.END)
    user_email_entry.insert(0, email)
    user_email_entry.config(state='readonly')
    
    messagebox.showinfo("Actualización", f"Información actualizada:\n\nNombre: {name}\nEmail: {email}")

