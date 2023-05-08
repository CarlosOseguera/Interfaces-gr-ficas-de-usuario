import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Formulario de registro")

campos = ["Nombre", "Apellido paterno", "Apellido materno", "Correo electrónico", "Teléfono móvil"]
cuadros = []

for i, campo in enumerate(campos):
    etiqueta = tk.Label(ventana, text=campo + ":")
    etiqueta.grid(row=i, column=0, padx=5, pady=5)
    cuadro = tk.Entry(ventana)
    cuadro.grid(row=i, column=1, padx=5, pady=5)
    cuadros.append(cuadro)

cuadros[0].focus()
    

opciones = ["Estudiante", "Empleado", "Desempleado",]
opcion_seleccionada = tk.StringVar()
opcion_seleccionada.set(opciones[0])

etiqueta_ocupacion = tk.Label(ventana, text="Ocupación:")
etiqueta_ocupacion.grid(row=5, column=0, padx=5, pady=5)
menu_ocupacion = tk.OptionMenu(ventana, opcion_seleccionada, *opciones)
menu_ocupacion.grid(row=5, column=1, padx=5, pady=5)

aficiones = ["Leer", "Música", "Videojuegos"]
opcion_aficiones = []

for i, aficion in enumerate(aficiones):
    opcion = tk.BooleanVar()
    opcion_aficiones.append(opcion)
    boton = tk.Checkbutton(ventana, text=aficion, variable=opcion)
    boton.grid(row=i+1, column=4, padx=5, pady=5)

for i in range(len(cuadros)-1):
    cuadros[i].bind('<Return>', lambda event, index=i: cuadros[index+1].focus_set())

estados = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas"]

etiqueta_estado = tk.Label(ventana, text="Estado:")
etiqueta_estado.grid(row=6, column=4, padx=5, pady=5)
combo_estado = ttk.Combobox(ventana, values=estados)
combo_estado.current(0)
combo_estado.grid(row=6, column=4, padx=5, pady=5)

cuadro_nombre = tk.Entry(ventana)
cuadro_paterno = tk.Entry(ventana)
cuadro_materno = tk.Entry(ventana)
cuadro_correo = tk.Entry(ventana)
cuadro_movil = tk.Entry(ventana)

cuadro_nombre = cuadros[0]
cuadro_paterno = cuadros[1]
cuadro_materno = cuadros[2]
cuadro_correo = cuadros[3]
cuadro_movil = cuadros[4]

def guardar_datos():
    print("Datos guardados:")
    print("Nombre:", cuadro_nombre.get())
    print("Apellido paterno:", cuadro_paterno.get())
    print("Apellido materno:", cuadro_materno.get())
    print("Correo electrónico:", cuadro_correo.get())
    print("Teléfono móvil:", cuadro_movil.get())
    print("Ocupación:", opcion_seleccionada.get())
    print("Aficiones:")
    for i, aficion in enumerate(aficiones):
        if opcion_aficiones[i].get():
            print("- " + aficion)
    print("Estado:", combo_estado.get())

def cancelar_registro():
    for cuadro in cuadros:
        cuadro.delete(0, tk.END)
    opcion_seleccionada.set(opciones[0])
    for boton in opcion_aficiones:
        boton.set(False)
    combo_estado.current(0)
    print("Registro cancelado")

boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
boton_guardar.bind("<Return>", lambda event: guardar_datos())
boton_cancelar = tk.Button(ventana, text="Cancelar", command=cancelar_registro)
boton_cancelar.bind("<Return>", lambda event: cancelar_registro())

boton_guardar.grid(row=7, column=0, padx=5, pady=5)
boton_cancelar.grid(row=7, column=1, padx=5, pady=5)


def siguiente_cuadro(event, cuadro_actual, lista_cuadros):
    """Función para mover el foco al siguiente cuadro de texto"""
    indice_actual = lista_cuadros.index(cuadro_actual)
    if indice_actual == len(lista_cuadros) - 1:
        # Si estamos en el último cuadro, no hacemos nada
        return
    else:
        # Movemos el foco al siguiente cuadro
        siguiente_cuadro = lista_cuadros[indice_actual + 1]
        siguiente_cuadro.focus_set()

# Añadir el evento Enter a todos los cuadros de texto
for cuadro in cuadros:
    cuadro.bind("<Return>", lambda event, cuadro_actual=cuadro, lista_cuadros=cuadros: 
                siguiente_cuadro(event, cuadro_actual, lista_cuadros))


# Ejecutar la ventana
ventana.mainloop()