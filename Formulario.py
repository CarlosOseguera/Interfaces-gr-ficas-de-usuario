import tkinter as tk
from tkinter import ttk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Muestra Widgets")

# Crear las etiquetas y los cuadros de texto
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, padx=5, pady=5)
cuadro_nombre = tk.Entry(ventana)
cuadro_nombre.grid(row=0, column=1, padx=5, pady=5)

etiqueta_paterno = tk.Label(ventana, text="A. Paterno:")
etiqueta_paterno.grid(row=1, column=0, padx=5, pady=5)
cuadro_paterno = tk.Entry(ventana)
cuadro_paterno.grid(row=1, column=1, padx=5, pady=5)

etiqueta_materno = tk.Label(ventana, text="A. Materno:")
etiqueta_materno.grid(row=2, column=0, padx=5, pady=5)
cuadro_materno = tk.Entry(ventana)
cuadro_materno.grid(row=2, column=1, padx=5, pady=5)

etiqueta_correo = tk.Label(ventana, text="Correo:")
etiqueta_correo.grid(row=3, column=0, padx=5, pady=5)
cuadro_correo = tk.Entry(ventana)
cuadro_correo.grid(row=3, column=1, padx=5, pady=5)

etiqueta_movil = tk.Label(ventana, text="Movil:")
etiqueta_movil.grid(row=4, column=0, padx=5, pady=5)
cuadro_movil = tk.Entry(ventana)
cuadro_movil.grid(row=4, column=1, padx=5, pady=5)

# Crear los botones de opción
opcion_seleccionada = tk.StringVar()
boton_estudiante = tk.Radiobutton(ventana, text="Estudiante", variable=opcion_seleccionada, value="Estudiante")
boton_empleado = tk.Radiobutton(ventana, text="Empleado", variable=opcion_seleccionada, value="Empleado")
boton_desempleado = tk.Radiobutton(ventana, text="Desempleado", variable=opcion_seleccionada, value="Desempleado")

# Posicionar los botones de opción a la derecha de las etiquetas
boton_estudiante.grid(row=1, column=4, padx=5, pady=5)
boton_empleado.grid(row=2, column=4, padx=5, pady=5)
boton_desempleado.grid(row=3, column=4, padx=5, pady=5)

# Crear los botones de opción para aficiones
etiqueta_aficiones = tk.Label(ventana, text="Aficiones:")
etiqueta_aficiones.grid(row=5, column=0, padx=5, pady=5)

aficion_seleccionada = tk.StringVar()
boton_leer = tk.Radiobutton(ventana, text="Leer", variable=aficion_seleccionada, value="Leer")
boton_musica = tk.Radiobutton(ventana, text="Música", variable=aficion_seleccionada, value="Música")
boton_videojuegos = tk.Radiobutton(ventana, text="Videojuegos", variable=aficion_seleccionada, value="Videojuegos")

# Posicionar los botones de opción de aficiones debajo de la etiqueta correspondiente
boton_leer.grid(row=6, column=0, padx=5, pady=5, sticky="w")
boton_musica.grid(row=6, column=1, padx=5, pady=5, sticky="w")
boton_videojuegos.grid(row=6, column=2, padx=5, pady=5, sticky="w")

# Crear la lista desplegable para los estados de la República Mexicana
estados = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas"]
etiqueta_estado = tk.Label(ventana, text="Estado:")
etiqueta_estado.grid(row=6, column=4, padx=5, pady=5)
combo_estado = ttk.Combobox(ventana, values=estados)
combo_estado.current(0)
combo_estado.grid(row=6, column=4, padx=5, pady=5)

def guardar_datos():
    nombre = cuadro_nombre.get()
    paterno = cuadro_paterno.get()
    materno = cuadro_materno.get()
    correo = cuadro_correo.get()
    movil = cuadro_movil.get()
    seleccionado = opcion_seleccionada.get()
    aficion = opcion_aficiones.get()
    estado_seleccionado = opcion_estados.get()

    print("Nombre:", nombre)
    print("Apellido Paterno:", paterno)
    print("Apellido Materno:", materno)
    print("Correo:", correo)
    print("Móvil:", movil)
    print("Ocupación:", seleccionado)
    print("Afición:", aficion)
    print("Estado seleccionado:", estado_seleccionado)

def cancelar():
    ventana.destroy()

# Crear los botones para guardar y cancelar
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
boton_cancelar = tk.Button(ventana, text="Cancelar", command=cancelar)

# Posicionar los botones debajo de la lista desplegable
boton_guardar.grid(row=7, column=0, padx=5, pady=5)
boton_cancelar.grid(row=7, column=1, padx=5, pady=5)

# Definir las funciones para guardar y cancelar
def guardar_datos():
    print("Datos guardados:")
    print("Nombre:", cuadro_nombre.get())
    print("Apellido paterno:", cuadro_paterno.get())
    print("Apellido materno:", cuadro_materno.get())
    print("Correo electrónico:", cuadro_correo.get())
    print("Teléfono móvil:", cuadro_movil.get())
    print("Ocupación:", opcion_seleccionada.get())
    print("Aficiones:")
    for aficion in aficiones:
        print("- " + aficion)
    print("Estado:", combo_estado.get())

def cancelar_registro():
    cuadro_nombre.delete(0, tk.END)
    cuadro_paterno.delete(0, tk.END)
    cuadro_materno.delete(0, tk.END)
    cuadro_correo.delete(0, tk.END)
    cuadro_movil.delete(0, tk.END)
    opcion_seleccionada.set("")
    for boton in botones_aficiones:
        boton.deselect()
    combo_estado.current(0)
    print("Registro cancelado")

# Ejecutar la ventana
ventana.mainloop()