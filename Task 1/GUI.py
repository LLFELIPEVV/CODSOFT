import tkinter as tk

from modificacion_json import leer_archivo_json
from CRUD import crear_tarea as ct, actualizar_tarea as at, eliminar_tarea as et

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("To-Do List")
ventana.geometry("600x700")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)

# Input para las tareas
input = tk.Entry(ventana, width=50, font=("Times New Roman", 24))
input.grid(row=0, column=0, columnspan=3, padx=50, pady=20, sticky="ew")

# Boton para agregar tareas
boton_agregar = tk.Button(ventana, text="Añadir Tarea",
                          width=20, height=2, bg="Green", fg="White", command=lambda: agregar_tarea())
boton_agregar.grid(row=1, column=0, padx=50, pady=0, sticky="ew")

# Boton para eliminar tareas
boton_eliminar = tk.Button(
    ventana, text="Eliminar Tarea", width=20, height=2, bg="Red", fg="White", command=lambda: eliminar_tarea())
boton_eliminar.grid(row=1, column=1, padx=10, pady=0, sticky="ew")

# Boton para actualizar tareas
boton_actualizar = tk.Button(
    ventana, text="Actualizar Tarea", width=20, height=2, bg="Blue", fg="White")
boton_actualizar.grid(row=1, column=2, padx=50, pady=0, sticky="ew")

# Lista donde se agregarán los frames de tareas
lista_tareas_frame = tk.Frame(ventana)
lista_tareas_frame.grid(row=2, column=0, columnspan=3,
                        padx=50, pady=20, sticky="nsew")

ventana.grid_rowconfigure(2, weight=1)

# Funciones


def agregar_tarea():
    tarea = input.get()
    if tarea:
        ct(tarea)
        obtener_tareas()
        input.delete(0, tk.END)


def eliminar_tarea():
    tarea = input.get()
    if tarea:
        et(tarea)
        obtener_tareas()
        input.delete(0, tk.END)


def actualizar_tarea():
    pass


def obtener_tareas():
    for widget in lista_tareas_frame.winfo_children():
        widget.destroy()

    tarea_texto = leer_archivo_json()
    if tarea_texto:
        for clave, valor in tarea_texto.items():
            crear_tarea(clave, valor["tarea"], valor["completada"])


def crear_tarea(id, tarea, completada):
    tarea_frame = tk.Frame(
        lista_tareas_frame, bg="lightgreen" if completada else "white", padx=10, pady=5)
    tarea_frame.pack(fill="x", pady=5)

    label_tarea = tk.Label(tarea_frame, text=tarea,
                           font=("Arial", 16), anchor="w")
    label_tarea.pack(side="left", fill="x", expand=True)

    label_tarea.bind("<Button-1>", lambda event,
                     t=tarea: cargar_tarea_en_input(t))
    estado_tarea = tk.BooleanVar(value=completada)

    checkbox = tk.Checkbutton(tarea_frame, variable=estado_tarea,
                              command=lambda: cambiar_estado_tarea(id, tarea, estado_tarea, tarea_frame))
    checkbox.pack(side="right")


def cambiar_estado_tarea(id, tarea, estado_tarea, tarea_frame):
    completada = estado_tarea.get()
    if completada:
        tarea_frame.config(bg="lightgreen")
    else:
        tarea_frame.config(bg="white")
    at(id, tarea, completada)


def cargar_tarea_en_input(tarea):
    input.delete(0, tk.END)
    input.insert(0, tarea)


obtener_tareas()

# Bucle principal de la aplicación
ventana.mainloop()
