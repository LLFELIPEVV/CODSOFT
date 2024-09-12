import tkinter as tk

from modificacion_json import leer_archivo_json
from CRUD import crear_tarea as ct, actualizar_tarea as at, eliminar_tarea as et

# Crea la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("To-Do List")  # Título de la ventana
ventana.geometry("600x700")  # Tamaño de la ventana

# Configura la ventana para que las columnas se ajusten automáticamente
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)

# Crea un campo de entrada (input) para que el usuario escriba nuevas tareas
input = tk.Entry(ventana, width=50, font=("Times New Roman", 24))
input.grid(row=0, column=0, columnspan=3, padx=50, pady=20, sticky="ew")

# Crea un botón para añadir tareas
boton_agregar = tk.Button(ventana, text="Añadir Tarea",
                          width=20, height=2, bg="Green", fg="White", command=lambda: agregar_tarea())
boton_agregar.grid(row=1, column=0, padx=50, pady=0, sticky="ew")

# Crea un botón para eliminar tareas
boton_eliminar = tk.Button(
    ventana, text="Eliminar Tarea", width=20, height=2, bg="Red", fg="White", command=lambda: eliminar_tarea())
boton_eliminar.grid(row=1, column=1, padx=10, pady=0, sticky="ew")

# Crea un botón para actualizar tareas
boton_actualizar = tk.Button(
    ventana, text="Actualizar Tarea", width=20, height=2, bg="Blue", fg="White", command=lambda: actualizar_tarea())
boton_actualizar.grid(row=1, column=2, padx=50, pady=0, sticky="ew")

# Crea un marco (frame) donde se mostrarán las tareas
lista_tareas_frame = tk.Frame(ventana)
lista_tareas_frame.grid(row=2, column=0, columnspan=3,
                        padx=50, pady=20, sticky="nsew")

# Ajusta la fila 2 para que se expanda cuando la ventana cambie de tamaño
ventana.grid_rowconfigure(2, weight=1)

# Variable global para almacenar la ID de la tarea seleccionada
tarea_seleccionada_id = None


# Función para agregar una nueva tarea
def agregar_tarea():
    tarea = input.get()  # Obtiene el texto del campo de entrada
    if tarea:  # Si hay texto
        ct(tarea)  # Llama a la función para crear la tarea
        obtener_tareas()  # Actualiza la lista de tareas
        input.delete(0, tk.END)  # Limpia el campo de entrada


# Función para eliminar una tarea
def eliminar_tarea():
    id = tarea_seleccionada_id  # Obtiene la ID de la tarea seleccionada
    if id:  # Si hay una tarea seleccionada
        et(id)  # Llama a la función para eliminar la tarea
        obtener_tareas()  # Actualiza la lista de tareas
        input.delete(0, tk.END)  # Limpia el campo de entrada


# Función para actualizar una tarea
def actualizar_tarea():
    id = tarea_seleccionada_id  # Obtiene la ID de la tarea seleccionada
    if id:  # Si hay una tarea seleccionada
        nueva_tarea = input.get()  # Obtiene el nuevo texto del campo de entrada
        if nueva_tarea:  # Si hay texto
            at(id, nueva_tarea)  # Llama a la función para actualizar la tarea
            obtener_tareas()  # Actualiza la lista de tareas
            input.delete(0, tk.END)  # Limpia el campo de entrada


# Función para obtener y mostrar todas las tareas
def obtener_tareas():
    # Elimina todos los widgets existentes en el marco de tareas
    for widget in lista_tareas_frame.winfo_children():
        widget.destroy()

    tarea_texto = leer_archivo_json()  # Lee las tareas desde el archivo JSON
    if tarea_texto:  # Si hay tareas
        for clave, valor in tarea_texto.items():  # Para cada tarea
            # Muestra la tarea en la interfaz
            crear_tarea(clave, valor["tarea"], valor["completada"])


# Función para crear y mostrar una tarea en la interfaz
def crear_tarea(id, tarea, completada):
    tarea_frame = tk.Frame(
        lista_tareas_frame, bg="lightgreen" if completada else "white", padx=10, pady=5)
    tarea_frame.pack(fill="x", pady=5)

    label_tarea = tk.Label(tarea_frame, text=tarea,
                           font=("Arial", 16), anchor="w")
    label_tarea.pack(side="left", fill="x", expand=True)

    label_tarea.bind(
        "<Button-1>", lambda event: cargar_tarea_en_input(tarea, id))
    estado_tarea = tk.BooleanVar(value=completada)

    checkbox = tk.Checkbutton(tarea_frame, variable=estado_tarea,
                              command=lambda: cambiar_estado_tarea(id, tarea, estado_tarea, tarea_frame))
    checkbox.pack(side="right")


# Función para cambiar el estado de completado de una tarea
def cambiar_estado_tarea(id, tarea, estado_tarea, tarea_frame):
    completada = estado_tarea.get()  # Obtiene el estado actual del checkbox
    if completada:
        # Cambia el color del marco si está completada
        tarea_frame.config(bg="lightgreen")
    else:
        # Cambia el color del marco si no está completada
        tarea_frame.config(bg="white")
    at(id, tarea, completada)  # Actualiza el estado de la tarea en el archivo


# Función para cargar una tarea en el campo de entrada para su edición
def cargar_tarea_en_input(tarea, id):
    global tarea_seleccionada_id
    input.delete(0, tk.END)  # Limpia el campo de entrada
    # Inserta el texto de la tarea en el campo de entrada
    input.insert(0, tarea)
    tarea_seleccionada_id = id  # Guarda la ID de la tarea seleccionada


# Carga las tareas cuando se inicia la aplicación
obtener_tareas()

# Inicia el bucle principal de la aplicación, esperando acciones del usuario
ventana.mainloop()
