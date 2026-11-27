import customtkinter as ctk

#TODO: donde luego importaremos pacientes.py, terapeutas.py y agenda.py.

def contruir_vista_agendar(contenedor_padre):
    #marco principal de la vista con barra de desplazamiento
    vista = ctk.CTkScrollableFrame(contenedor_padre, fg_color = "#F8FAFC")

    # etiqueta superior en verde GESTION DE CITAS
    etiqueta_seccion = ctk.CTkLabel(vista, text = "GESTION DE CITAS", font = ("arial", 11, "bold"), text_color = "#10B981")
    etiqueta_seccion.pack(anchor = "w", padx = 30, pady = (20, 0))

    # etiqueta titulo Agendar cita
    etiqueta_titulo = ctk.CTkLabel(vista, text = "Agendar cita", font = ("arial", 26, "bold"), text_color = "#0F172A")
    etiqueta_titulo.pack(anchor = "w", padx = 30 , pady = (2,5))

    # Etiqueta subtitulo
    etiqueta_subtitulo = ctk.CTkLabel(vista, text = "Coordina las terapias de tus pacientes de forma clara y sin conflictos de horario.", font = ("arial", 13), text_color = "#64748B")
    etiqueta_subtitulo.pack(anchor = "w", padx = 30 , pady = (0,20))

    #CONTENEDOR HORIZONTAL PARA LAS 3 TARJETAS INDICADORAS
    contenedor_indicadores = ctk.CTkFrame(vista, fg_color =  "transparent")
    contenedor_indicadores.pack(fill = "x", padx = 30, pady = (0,20))
    contenedor_indicadores.grid_columnconfigure((0,1,2), weight = 1, uniform = "grupo_indicadores")

    #TARJETAS REUTILIZANDO LA FUNCION
    numero_citas = crear_tarjeta_indicador(contenedor_indicadores, 0, "Citas programadas", (0,10))
    numero_pacientes = crear_tarjeta_indicador(contenedor_indicadores, 1, "Pacientes registrados", 5 )
    numero_terapeutas = crear_tarjeta_indicador(contenedor_indicadores, 2, "Terapeutas activos", (10, 0) )

    #TARJETA BLANCA PRINCIPAL PARA NUEVA CITA
    tarjeta_formulario = ctk.CTkFrame(vista, fg_color = "#FFFFFF", corner_radius = 12, border_width = 1, border_color = "#E2E8F0" )
    tarjeta_formulario.pack(fill = "x", padx = 30 , pady = (0,30))
    #TITULO DENTRO DE LA TARJETA
    
# por aqui creo que va la funsion para actualizar los contadores con la info guardada
    return vista


#INDICADORES
def crear_tarjeta_indicador(contenedor, columna, texto_descriptivo, margen_x):

    #MARCO BLANCO DE LA TARJETA:
    tarjeta = ctk.CTkFrame(contenedor, fg_color = "#FFFFFF", corner_radius = 12, border_width = 1, border_color = "#E2E8F0") 
    tarjeta.grid(row = 0, column = columna, padx = margen_x, sticky = "ew")

    #NUMERO GRANDE ARRIBA: 
    numero_indicador = ctk.CTkLabel(tarjeta, text = "0", font = ("arial", 22, "bold"), text_color = "#0F172A")
    numero_indicador.pack(anchor = "w", padx = 20, pady = (15,0))

    #TEXTO DESCRIPTIVO
    texto_indicador = ctk.CTkLabel(tarjeta, text = texto_descriptivo, font = ("arial", 12), text_color = "#64748B")
    texto_indicador.pack(anchor="w", padx=20, pady=(0, 15))

    return numero_indicador




# Bloque temporal solo para probar esta vista individualmente (luego se borra)
if __name__ == "__main__":
    ventana_prueba = ctk.CTk()
    ventana_prueba.geometry("950x700")
    vista_agendar = contruir_vista_agendar(ventana_prueba)
    vista_agendar.pack(fill="both", expand=True)
    ventana_prueba.mainloop()