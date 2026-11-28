import customtkinter as ctk
ctk.set_appearance_mode("light") #para que el fondo de la ventana no tome el modo oscuro de Windows).

ventana = ctk.CTk()

ventana.title("IPS Rehabilitacion")
ventana.geometry("1200x750")
ventana.grid_rowconfigure(0, weight = 1) #para que la fila 0 ocupe todo el alto
ventana.grid_columnconfigure(0, weight = 0) # columna izquierda fija
ventana.grid_columnconfigure(1, weight = 1) #columna derecha flexible

#PANEL IZQUIEROD
barra_lateral = ctk.CTkFrame(ventana, width = 250, corner_radius = 0, fg_color = "#1E293B" )
barra_lateral.pack_propagate(False) # no se encoje aunque este vacio
barra_lateral.grid(row = 0 , column = 0, sticky = "nsew") # row: fila, column: columna, sticky:pegar/estirar, nsew: todos los lados a la vez

#encabezado del logo
encabezado_logo = ctk.CTkFrame(barra_lateral, fg_color = "transparent")
encabezado_logo.pack(fill = "x", padx = 20, pady = (24,30))

# logo: mas adelante se podrian agregar las funciones para que el usuario lo personalize
icon = ctk.CTkFrame(encabezado_logo, width = 38, height = 38, corner_radius = 10, fg_color = "#34D399")
icon.pack(side = "left") # lo coloca al al lado izquierdo del encabezado
icon.pack_propagate(False) #para que no pierda las dimensiones 38x38 al meter el icono adentro

etiqueta_icono = ctk.CTkLabel(icon, text = "♡", text_color = "#FFFFFF", font = ("arial", 22, "bold"))
etiqueta_icono.pack(expand = True) 
# expand=True: ocupa todo el espacio sobrante del cuadrito padre (icon) para centrar el ícono vertical y horizontalmente

# Textos al lado del icono
contenedor_titulo_logo = ctk.CTkFrame(encabezado_logo, fg_color = "transparent")
contenedor_titulo_logo.pack(side = "left", padx = (12,0))

#Titulo IPS
titulo_ips = ctk.CTkLabel(contenedor_titulo_logo, text = "IPS REHABILITACION",text_color = "#FFFFFF", font = ("arial",14, "bold" ))
titulo_ips.pack(anchor = "w")

#subtitulo IPS
subtitulo_ips = ctk.CTkLabel(contenedor_titulo_logo, text = "GESTION CLINICA", text_color = "#94A3B8", font = ("arial",10 ,"bold"))
subtitulo_ips.pack(anchor = "w")

#linea divisoria
linea_divisoria = ctk.CTkFrame(barra_lateral, height = 2, corner_radius = 0, fg_color = "#334155")
linea_divisoria.pack(fill = "x", padx = 20, pady = (0,20))
linea_divisoria.pack_propagate(False)

#Etiqueta de seccion
seccion = ctk.CTkLabel(barra_lateral, text = "MENU PRINCIPAL", text_color = "#64748B", font = ("arial",10 ,"bold"))
seccion.pack(anchor = "w", padx = 24, pady = (0,8))

# BOTONES
#Boton 1: agendar cita, arranca activo
btn_agendar = ctk.CTkButton(barra_lateral, text = "📅 Agendar cita", height = 42, corner_radius = 10, fg_color = "#334155",
hover_color = "#334155", text_color = "#FFFFFF", font = ("arial", 13, "bold"))
btn_agendar.pack(fill = "x", padx = 14, pady = 3)

#Boton 2: cronograma
btn_cronograma = ctk.CTkButton(barra_lateral, text = "📅 Cronograma por paciente", height = 42, corner_radius = 10, fg_color = "transparent",
hover_color = "#334155", text_color = "#CBD5E1", font = ("arial", 13, "bold"))
btn_cronograma.pack(fill = "x", padx = 14, pady = 3)

#Boton 3: Registros
btn_registros = ctk.CTkButton(barra_lateral, text = "👥  Registros", height = 42, corner_radius = 10, fg_color = "transparent",
hover_color = "#334155", text_color = "#CBD5E1", font = ("arial", 13, "bold"))
btn_registros.pack(fill = "x", padx = 14, pady = 3)

# Pie de barra (al fondo)
pie_barra = ctk.CTkFrame(barra_lateral, fg_color="transparent")
pie_barra.pack(side="bottom", fill="x", padx=20, pady=24)

lbl_pie_titulo = ctk.CTkLabel(pie_barra, text="Panel administrativo", text_color="#FFFFFF", font=("arial", 11, "bold"))
lbl_pie_titulo.pack(anchor="w")

lbl_pie_desc = ctk.CTkLabel(pie_barra, text = "Organiza la atención, sin cruces de horario.", text_color = "#94A3B8",
font = ("arial", 11), wraplength = 200, justify = "left"
)
lbl_pie_desc.pack(anchor = "w", pady = (2, 0))

#PANEL DERECHO
area_derecha = ctk.CTkScrollableFrame(ventana, corner_radius = 0, fg_color = "#F8FAFC")
area_derecha.grid(row = 0, column = 1, sticky = "nsew")

#caja para titulo 
barra_superior = ctk.CTkFrame(area_derecha, fg_color = "transparent")
barra_superior.pack(fill = "x", padx = 30, pady = (20,12))

#titulo 
titulo_barra_superior = ctk.CTkLabel(barra_superior, text = "SISTEMA AGENDAMIENTO / IPS REHABILITACION", text_color ="#64748B", font = ("arial",10, "bold"))
titulo_barra_superior.pack(side = "left")

#etiqueta derecha uso interno
etiquetaUso_interno = ctk.CTkFrame(barra_superior, fg_color="#FFFFFF", corner_radius = 16, border_width = 1, border_color = "#E2E8F0")
etiquetaUso_interno.pack(side = "right")

uso_interno = ctk.CTkLabel(etiquetaUso_interno, text = "🛡 Uso interno", text_color = "#475569", font = ("arial", 11, "bold"))
uso_interno.pack(padx=12, pady=4)

#linea espaciadora
linea_superior = ctk.CTkFrame(area_derecha, height=2, corner_radius=0, fg_color="#E2E8F0")
linea_superior.pack(fill="x", padx=30, pady=(0, 22))
linea_superior.pack_propagate(False)

#TEXTOS DEL ENCABEZADO
encabezado_vista = ctk.CTkFrame(area_derecha, fg_color = "transparent")
encabezado_vista.pack(fill = "x", padx = 30, pady = (0,20))

#categoria vista agendar cita
lbl_categoria = ctk.CTkLabel(encabezado_vista, text = "GESTION DE CITAS", text_color = "#10B981", font = ("arial", 11, "bold"))
lbl_categoria.pack(anchor = "w")

#titulo vista agendar cita
lbl_titulo_vista = ctk.CTkLabel(encabezado_vista, text = "Agendar cita", text_color = "#0F172A", font = ("arial",24, "bold"))
lbl_titulo_vista.pack(anchor = "w", pady = (2,4))

#subtitulo vista agendar cita
lbl_subtitulo_vista = ctk.CTkLabel(encabezado_vista, text = "Coordina las terapias de tus pacientes de forma clara y sin conflictos de horario.",
text_color = "#64748B", font = ("arial",13))
lbl_subtitulo_vista.pack(anchor = "w")

#TARJETAS CONTADORAS
#contenedor
fila_tarjetas = ctk.CTkFrame(area_derecha, fg_color = "transparent")
fila_tarjetas.pack(fill = "x", padx = 30, pady = (0,24))
fila_tarjetas.grid_columnconfigure((0, 1, 2), weight=1, uniform="tarjetas")

def crear_tarjeta_contadora(columna, icono, color_icono, fondo_icono, descripcion, padx):
    #Tarjeta blanca
    tarjeta = ctk.CTkFrame(fila_tarjetas, fg_color = "#FFFFFF", corner_radius = 12, border_width = 1, border_color = "#E2E8F0")
    tarjeta.grid(row=0, column=columna, padx= padx, sticky="ew")

    cuerpo = ctk.CTkFrame(tarjeta, fg_color="transparent")
    cuerpo.pack(fill="x", padx=20, pady=18)

    # Cuadrito del ícono
    caja_icono = ctk.CTkFrame(cuerpo, width=44, height=44, corner_radius=12, fg_color=fondo_icono)
    caja_icono.pack(side="left")
    caja_icono.pack_propagate(False)

    lbl_ico = ctk.CTkLabel(caja_icono, text=icono, text_color=color_icono, font=("arial", 18, "bold"))
    lbl_ico.pack(expand=True)

    # Número y texto a la derecha del ícono
    datos = ctk.CTkFrame(cuerpo, fg_color="transparent")
    datos.pack(side="left", padx=(14, 0))

    lbl_numero = ctk.CTkLabel(datos, text="0", text_color="#0F172A", font=("arial", 22, "bold"))
    lbl_numero.pack(anchor="w")

    lbl_desc = ctk.CTkLabel(datos, text=descripcion, text_color="#64748B", font=("arial", 12))
    lbl_desc.pack(anchor="w")

    # Devolvemos lbl_numero para actualizarlo desde la base de datos
    return lbl_numero

lbl_num_citas = crear_tarjeta_contadora(0, "📅", "#EFF6FF", "#3B82F6", "Citas programadas", (0, 8))
lbl_num_pacientes = crear_tarjeta_contadora(1, "👥", "#ECFDF5", "#10B981", "Pacientes registrados", (8, 8))
lbl_num_terapeutas = crear_tarjeta_contadora(2, "🩺", "#F5F3FF", "#8B5CF6", "Terapeutas activos", (8, 0))



#funcion que actualiza la apariencia del menú lateral y los textos del encabezado al cambiar de vista
def seleccionar_boton(boton_activo, nuevo_titulo, nuevo_subtitulo):
    # Restablece el estilo por defecto (fondo transparente y texto claro) en todos los botones del menú
    for btn in [btn_agendar, btn_cronograma, btn_registros]:
        btn.configure(fg_color = "transparent", text_color = "#CBD5E1")
    # Resalta únicamente el botón que fue presionado con fondo más claro y texto blanco
    boton_activo.configure(fg_color = "#334155", text_color = "#FFFFFF")

    # Actualiza el título principal y el subtítulo del panel derecho según la sección elegida
    lbl_titulo_vista.configure(text=nuevo_titulo)
    lbl_subtitulo_vista.configure(text=nuevo_subtitulo)

# Asigna el evento de clic (command) a cada botón usando lambda para enviar sus parámetros específicos
btn_agendar.configure(command=lambda: seleccionar_boton(btn_agendar,"Agendar cita", "Coordina las terapias de tus pacientes de forma clara y sin conflictos de horario.") )
btn_cronograma.configure(command=lambda: seleccionar_boton(btn_cronograma, "Cronograma por paciente", "Consulta e imprime el plan semanal de terapias de un paciente.") )
btn_registros.configure(command=lambda: seleccionar_boton(btn_registros, "Registro de pacientes y terapeutas", "Mantén actualizado el directorio de atención de la IPS.") )


ventana.mainloop() 
