import customtkinter as ctk

#TODO: donde luego importaremos pacientes.py, terapeutas.py y agenda.py.

class VistaAgendar(ctk.CTkScrollableFrame): #crea un plano de vista como un panel de scroll
    def __init__(self, master): #Es el arranque automático de la vista en cuanto se abre; master es la ventana principal que la contiene.
        super().__init__(master, fg_color="#F8FAFC") #Construye el panel con el fondo gris clarito 

        # etiqueta superior en verde GESTION DE CITAS
        self.etiqueta_seccion = ctk.CTkLabel(self, text = "GESTION DE CITAS", font = ("arial", 11, "bold"), text_color = "#10B981")
        self.etiqueta_seccion.pack(anchor = "w", padx = 30, pady = (20, 0))

        # etiqueta titulo Agendar cita
        self.etiqueta_titulo = ctk.CTkLabel(self, text = "Agendar cita", font = ("arial", 26, "bold"), text_color = "#0F172A")
        self.etiqueta_titulo.pack(anchor = "w", padx = 30 , pady = (2,5))

        # Etiqueta subtitulo
        self.etiqueta_subtitulo = ctk.CTkLabel(self, text = "Coordina las terapias de tus pacientes de forma clara y sin conflictos de horario.", font = ("arial", 13), text_color = "#64748B")
        self.etiqueta_subtitulo.pack(anchor = "w", padx = 30 , pady = (0,20))

        # contenedor para los 3 indicadores
        self.contenedor_indicadores = ctk.CTkFrame(self, fg_color = "transparent")
        self.contenedor_indicadores.pack(fill = "x", padx = 30, pady = (0,20) )
        self.contenedor_indicadores.grid_columnconfigure((0,1,2), weight = 1, uniform = "Grupo indicadores")

        # Tarjeta 1: citas programadas
        self.tarjeta_citas = ctk.CTkFrame(self.contenedor_indicadores, fg_color = "#FFFFFF", corner_radius = 12, border_width = 1, border_color = "#E2E8F0")
        self.tarjeta_citas.grid(row = 0, column = 0, padx = (0,10), sticky = "ew")

        self.texto_citas = ctk.CTkLabel(self.tarjeta_citas, text = "Citas programadas", font = ("arial", 12), text_color = "#64748B")
        self.texto_citas.pack(anchor = "w", padx = 20, pady = (0,15))

# Bloque temporal solo para probar esta vista individualmente (luego se borra)
if __name__ == "__main__":
    ventana_prueba = ctk.CTk()
    ventana_prueba.geometry("950x700")
    vista = VistaAgendar(ventana_prueba)
    vista.pack(fill="both", expand=True)
    ventana_prueba.mainloop()