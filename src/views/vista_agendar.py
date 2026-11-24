import customtkinter as ctk

#TODO: donde luego importaremos pacientes.py, terapeutas.py y agenda.py.

class VistaAgendar(ctk.CTkScrollableFrame): #crea un plano de vista como un panel de scroll
    def __init__(self, master): #Es el arranque automático de la vista en cuanto se abre; master es la ventana principal que la contiene.
        super().__init__(master, fg_color="#F8FAFC") #Construye el panel con el fondo gris clarito 

        # etiqueta superior en verde GESTION DE CITAS
        self.etiqueta_seccion = ctk.CTkLabel(self, text = "GESTION DE CITAS", font = ("arial", 11, "bold"), text_color = "#10B981")
        self.etiqueta_seccion.pack(anchor="w", padx=30, pady=(20, 0))


# Bloque temporal solo para probar esta vista individualmente (luego se borra)
if __name__ == "__main__":
    ventana_prueba = ctk.CTk()
    ventana_prueba.geometry("950x700")
    vista = VistaAgendar(ventana_prueba)
    vista.pack(fill="both", expand=True)
    ventana_prueba.mainloop()