import tkinter as tk
from tkinter import font, messagebox
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img

# Importar funciones
from funciones.mostrar_perfil import mostrar_perfil
from funciones.mostrar_sesiones import mostrar_sesiones
from funciones.mostrar_agendar import mostrar_agendar
from funciones.mostrar_actividad import mostrar_actividad
from funciones.mostrar_calificacion import mostrar_calificacion
from funciones.mostrar_material import mostrar_material
from funciones.mostrar_cerrar import mostrar_cerrar

class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("imagenes/anuncios.png", (700, 500))
        self.perfil = util_img.leer_imagen("imagenes/logo.png", (180, 110))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def config_window(self):
        self.title('PAV')
        self.iconbitmap("imagenes/logo_icono.ico")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):       
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='y', expand=False) 
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)
        self.labelTitulo = tk.Label(self.barra_superior, text="MENU")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome, bg=COLOR_BARRA_SUPERIOR, fg="#fff", bd=0, command=self.toggle_panel)
        self.buttonMenuLateral.pack(side=tk.LEFT, padx=10)
        self.labelInfo = tk.Label(self.barra_superior, text="soportepav@pavirtual.com.co")
        self.labelInfo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelInfo.pack(side=tk.RIGHT)
    
    def controles_menu_lateral(self):
        font_awesome = font.Font(family='FontAwesome', size=12)
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)
        self.frame_botones = tk.Frame(self.menu_lateral, bg=COLOR_MENU_LATERAL)
        self.frame_botones.pack(side=tk.TOP, fill='both', expand=True, padx=10, pady=10)

        self.buttonperfil = tk.Button(self.frame_botones, command=lambda: mostrar_perfil(self)) 
        self.buttonsesiones = tk.Button(self.frame_botones, command=lambda: mostrar_sesiones(self))        
        self.buttonagendar = tk.Button(self.frame_botones, command=lambda: mostrar_agendar(self))        
        self.buttonactividad = tk.Button(self.frame_botones, command=lambda: mostrar_actividad(self))
        self.buttoncalificacion = tk.Button(self.frame_botones, command=lambda: mostrar_calificacion(self))        
        self.buttonmaterial = tk.Button(self.frame_botones, command=lambda: mostrar_material(self))
        self.buttoncerrar = tk.Button(self.frame_botones, command=lambda: mostrar_cerrar(self))

        buttons_info = [
            ("MI PERFIL ", "\uf007", self.buttonperfil),
            ("MIS SESIONES ", "\uf109", self.buttonsesiones),
            ("AGENDAMIENTO ", "\uf518", self.buttonagendar),
            ("ACTIVIDADES", "\uf304", self.buttonactividad),
            ("CALIFICACIONES", "\uf14a", self.buttoncalificacion),
            ("MATERIAL UTIL ", "\uf07c", self.buttonmaterial),
            ("CERRAR SESION ", "\uf52a", self.buttoncerrar)
        ]
        
        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome)                    
 
    def controles_cuerpo(self):
        self.labelCuerpo = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.labelCuerpo.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_boton_menu(self, button, text, icon, font_awesome):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome, bd=0, bg="#105494", fg="white", width=20, height=2)
        button.pack(side=tk.TOP, fill='x', pady=5, padx=5)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        button.config(bg="#105494", fg='white')

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')


