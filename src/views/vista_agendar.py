import customtkinter as ctk

#TODO: donde luego importaremos pacientes.py, terapeutas.py y agenda.py.

def contruir_vista_agendar(contenedor_padre, al_ir_a_registros = None, al_guardar_cita = None): 
    #marco principal de la vista con barra de desplazamiento
    vista = ctk.CTkFrame(contenedor_padre, fg_color = "#F8FAFC")

    #TARJETA BLANCA PRINCIPAL PARA NUEVA CITA
    tarjeta_formulario = ctk.CTkFrame(vista, fg_color = "#FFFFFF", corner_radius = 12, border_width = 1, border_color = "#E2E8F0" )
    tarjeta_formulario.pack(fill = "x", padx = 30 , pady = (0,30))
    
    #TITULO DENTRO DE LA TARJETA
    titulo_formulario = ctk.CTkLabel(tarjeta_formulario, text = "Nueva cita terapeutica", font = ("arial",16, "bold"), text_color = "#0F172A")
    titulo_formulario.pack(anchor = "w", padx = 25, pady = (20,2))
    
    #SUBTITULO DENTRO DE LA TARJETA
    subtitulo_formulario = ctk.CTkLabel(tarjeta_formulario, text = "Completa los datos para reservar un bloque de atención.", font = ("arial", 12 ), text_color = "#64748B")
    subtitulo_formulario.pack(anchor = "w", padx = 25, pady = (0,18))
    
    #CAMPOS DEL FORMULARIO
    cuadricula_campos = ctk.CTkFrame(tarjeta_formulario, fg_color = "transparent")
    cuadricula_campos.pack(fill = "x", padx = 25, pady = (0,18))
    cuadricula_campos.grid_columnconfigure((0,1), weight = 1, uniform = "grupo_de_campos")
    
    #FILA PACIENTE REGISTRADO Y ESPECIALIDAD
    # Columna izquierda (0): Etiqueta, desplegable de Paciente y botón "+ Nuevo"
    etiqueta_paciente = ctk.CTkLabel(cuadricula_campos, text = "Paciente registrado", font = ("arial", 12, "bold"), text_color = "#0F172A")
    etiqueta_paciente.grid(row = 0, column = 0, padx = (0,10), pady = (0,5), sticky = "w")

    fila_paciente = ctk.CTkFrame(cuadricula_campos, fg_color = "transparent")
    fila_paciente.grid(row = 1, column = 0, padx = (0,10), pady = (0,15), sticky = "ew")
    fila_paciente.grid_columnconfigure(0, weight = 1)

    desplegable_paciente = ctk.CTkOptionMenu(fila_paciente, values = ["selecciona un paciente..."], height = 40, corner_radius = 10,
    fg_color = "#F1F5F9", button_color = "#F1F5F9", button_hover_color = "#E2E8F0", text_color = "#0F172A", dropdown_fg_color = "#FFFFFF")
    # en values = ["selecciona un paciente"] cuando se conecten paciente.py y terapeutas.py, se remplaza por la lista cargada de .csv
    desplegable_paciente.grid(row = 0, column = 0, padx = (0,8), sticky = "ew")

    boton_nuevo_paciente = ctk.CTkButton(fila_paciente, text = "+ Nuevo", width = 80, height = 40, corner_radius = 10, fg_color = "#ECFDF5",
    hover_color = "#D1FAE5", border_width = 1, border_color = "#D1FAE5", text_color = "#0F766E", font = ("arial", 12, "bold"), command = al_ir_a_registros)
    boton_nuevo_paciente.grid(row = 0, column = 1 )

    #columna derecha (1) depegable de especialidades
    etiqueta_especialidad = ctk.CTkLabel(cuadricula_campos, text = "especialidad", font = ("arial", 12, "bold"), text_color = "#0F172A")
    etiqueta_especialidad.grid(row = 0, column = 1, padx = (10,0), pady = (0,5), sticky = "w" )

    desplegable_especialidad = ctk.CTkOptionMenu(cuadricula_campos, values = ["selecciona una especialidad..."], height = 40, corner_radius = 10,
    fg_color = "#F1F5F9", button_color = "#F1F5F9", button_hover_color = "#E2E8F0", text_color = "#0F172A", dropdown_fg_color = "#FFFFFF")
    #igualmete se conectara la base de datos 
    desplegable_especialidad.grid(row = 1, column = 1, padx = (10,0), pady = (0,15), sticky = "ew")

    #fila 2: terapeuta
    etiqueta_terapeuta = ctk.CTkLabel(cuadricula_campos, text = "Terapeuta", font = ("arial", 12, "bold"), text_color = "#0F172A")
    etiqueta_terapeuta.grid(row = 2, column = 0, padx = (0,10), pady = (0,5), sticky = "w")

# values: recibe una lista con las opciones que verá el usuario al abrir el menú
# state: controla si el menú se puede usar ("normal") o está bloqueado ("disabled")

    desplegable_terapeuta = ctk.CTkOptionMenu(cuadricula_campos, values = ["Primero escoge una especialidad"], height = 40, corner_radius = 10, fg_color = "#F1F5F9",
    button_color = "#F1F5F9", button_hover_color = "#E2E8F0", text_color = "#0F172A", dropdown_fg_color = "#FFFFFF", state = "disabled") 
    desplegable_terapeuta.grid(row = 3, column = 0, padx = (0,10), pady = (0,15), sticky = "w")

    #funcion que se ejecuta cada que el usuario cambia de especialidad
    def al_cambiar_especialidad(especialidad_elegida):
    #TODO: Conectar con terapeutas.py para traer la lista real desde terapeutas.csv
        lista_terapeutas = []

        if lista_terapeutas:
        # Si hay terapeutas, actualizamos las opciones (values) y activamos el menú (state="normal")
            desplegable_terapeuta.configure(values = lista_terapeutas, state = "normal")
            desplegable_terapeuta.set("Selecciona un terapeuta")
        else:
        # Si no hay terapeutas, dejamos el aviso y bloqueamos el menú (state="disabled")
            desplegable_terapeuta.configure(values = ["No hay terapeutas disponibles"], state = "disabled")
            desplegable_terapeuta.set("No hay terapeutas disponible")


    # Conectamos el desplegable de especialidad para que llame a la función al elegir una opción
    desplegable_especialidad.configure(command = al_cambiar_especialidad)

    





    return vista


# Bloque temporal solo para probar esta vista individualmente (luego se borra)
if __name__ == "__main__":
    ventana_prueba = ctk.CTk()
    ventana_prueba.geometry("950x700")
    vista_agendar = contruir_vista_agendar(ventana_prueba)
    vista_agendar.pack(fill="both", expand=True)
    ventana_prueba.mainloop()