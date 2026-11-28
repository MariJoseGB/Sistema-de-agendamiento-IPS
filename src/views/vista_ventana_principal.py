"""import customtkinter as ctk

ventana = ctk.CTk()

ventana.title("IPS Rehabilitacion")
ventana.geometry("1200x750")
ventana.grid_rowconfigure(0, weight = 1) #para que la fila 0 ocupe todo el alto
ventana.grid_columnconfigure(0, weight = 0) # columna izquierda fija
ventana.grid_columnconfigure(1, weight = 1) #columna derecha flexible

#Panel izquierdo
barra_lateral = ctk.CTkFrame(ventana, width = 250, corner_radius = 0, fg_color = "#1E293B" )
barra_lateral.pack_propagate(False) # no se encoje aunque este vacio
barra_lateral.grid(row = 0 , column = 0, sticky = "nsew") # row: fila, column: columna, sticky:pegar/estirar, nsew: todos los lados a la vez

#panel derecho
area_derecha = ctk.CTkFrame(ventana, corner_radius = 0, fg_color = "#F8FAFC")
area_derecha.grid(row = 0, column = 1, sticky = "nsew")

#encabezado del logo
encabezado_logo = ctk.CTkFrame(barra_lateral, fg_color = "transparent")
encabezado_logo.pack(fill = "x", padx = 20, pady = (24,30))

# logo: mas adelante se podrian agregar las funciones para que el usuario lo perosnalize
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

#cambiar el color al seleccionar un boton
def seleccionar_boton(boton_activo):
    for btn in [btn_agendar, btn_cronograma, btn_registros]:
        btn.configure(fg_color = "transparent", text_color = "#CBD5E1")
    boton_activo.configure(fg_color = "#334155", text_color = "#FFFFFF")

btn_agendar.configure(command=lambda: seleccionar_boton(btn_agendar) )
btn_cronograma.configure(command=lambda: seleccionar_boton(btn_cronograma) )
btn_registros.configure(command=lambda: seleccionar_boton(btn_registros) )

# Pie de barra (al fondo)
pie_barra = ctk.CTkFrame(barra_lateral, fg_color="transparent")
pie_barra.pack(side="bottom", fill="x", padx=20, pady=24)

lbl_pie_titulo = ctk.CTkLabel(pie_barra, text="Panel administrativo", text_color="#FFFFFF", font=("arial", 11, "bold"))
lbl_pie_titulo.pack(anchor="w")

lbl_pie_desc = ctk.CTkLabel(pie_barra, text = "Organiza la atención, sin cruces de horario.", text_color = "#94A3B8",
font = ("arial", 11), wraplength = 200, justify = "left"
)
lbl_pie_desc.pack(anchor = "w", pady = (2, 0))

ventana.mainloop() """