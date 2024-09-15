import tkinter as tk

from generador import generar_contraseña as gc


# Función que genera la contraseña
def generar_contraseña():
    # Intenta ejecutar el código dentro de este bloque
    try:
        # Toma el valor que el usuario escribió en el campo de texto 'input' y lo convierte a entero
        longitud = int(input.get())
        if longitud <= 0:  # Si la longitud es menor o igual a 0, lanza un error
            raise ValueError("La longitud debe ser mayor a 0.")
        # Llama a la función para generar la contraseña con la longitud proporcionada por el usuario
        contraseña = gc(longitud)
        # Borra el contenido del campo de entrada (input) para que quede limpio
        input.delete(0, tk.END)
        # Muestra la contraseña generada en el campo de texto 'contraseña_input'
        contraseña_input.config(text=contraseña)

    # Si hay un error (por ejemplo, si el usuario no ingresa un número), ejecuta esto
    except ValueError:
        # Muestra un mensaje de error en lugar de la contraseña
        contraseña_input.config(text="Introduce un número válido.")


# Crear la ventana principal de la aplicación
ventana = tk.Tk()  # Inicializa la ventana principal de la aplicación
ventana.title("Generador de contraseñas")  # Establece el título de la ventana
# ventana.geometry("700x500")  # Esto establece el tamaño de la ventana (comentado porque se ajusta dinámicamente)
ventana.config(bg="#f0f0f0")  # Establece el color de fondo de la ventana

# Crear un contenedor (frame) para el título
# Crea un 'frame' para organizar el título dentro de la ventana
frame_titulo = tk.Frame(ventana, bg="#f0f0f0")
# Lo coloca en la ventana con algo de espacio vertical (pady)
frame_titulo.pack(fill='x', pady=20)

# Crear y mostrar el título de la aplicación
titulo = tk.Label(frame_titulo, text="Generador de contraseñas",
                  font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")  # Crea una etiqueta con texto grande y negrita
titulo.pack()  # La coloca dentro del frame del título

# Crear un frame para organizar el campo de entrada y el botón
# Crea otro frame, esta vez para la entrada del usuario y el botón
frame_input = tk.Frame(ventana, bg="#f0f0f0")
# Lo coloca dentro de la ventana con algo de espacio alrededor
frame_input.pack(fill='x', padx=20, pady=10)

# Crear una etiqueta para el campo de entrada de longitud de la contraseña
# Crea una etiqueta para indicar dónde ingresar la longitud
longitud_label = tk.Label(frame_input, text="Longitud:", font=(
    "Arial", 18), bg="#f0f0f0", fg="#333")
# La coloca en una cuadrícula (grid), alineada a la derecha
longitud_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')

# Crear el campo de entrada para la longitud de la contraseña
# Crea un campo donde el usuario puede escribir la longitud
input = tk.Entry(frame_input, font=("Arial", 18),
                 relief="solid", borderwidth=1)
# Lo coloca al lado de la etiqueta en la cuadrícula, permitiendo que se expanda horizontalmente
input.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

# Crear el botón para generar la contraseña
generar_button = tk.Button(frame_input, text="Generar", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white",
                           relief="flat", padx=15, pady=5, command=generar_contraseña)  # Crea un botón con texto y estilo
# Lo coloca a la derecha del campo de entrada en la cuadrícula
generar_button.grid(row=0, column=2, padx=10, pady=5)

# Permitir que la columna con el campo de entrada se expanda cuando la ventana cambia de tamaño
frame_input.grid_columnconfigure(1, weight=1)

# Crear un frame para mostrar la contraseña generada
# Crea un nuevo frame para organizar la sección donde se muestra la contraseña generada
frame_contraseña = tk.Frame(ventana, bg="#f0f0f0")
# Lo coloca en la ventana con algo de espacio alrededor
frame_contraseña.pack(fill='x', padx=20, pady=20)

# Crear una etiqueta que indica dónde aparecerá la contraseña generada
contraseña_label = tk.Label(frame_contraseña, text="Contraseña generada:", font=(
    "Arial", 18), bg="#f0f0f0", fg="#333")  # Crea una etiqueta para la sección de contraseña generada
# La coloca en la cuadrícula, alineada a la izquierda
contraseña_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Crear un campo para mostrar la contraseña generada
contraseña_input = tk.Label(frame_contraseña, text="", font=("Courier New", 16, "bold"), bg="white", relief="solid",
                            borderwidth=1, padx=10, pady=5)  # Crea una etiqueta vacía donde se mostrará la contraseña generada
# La coloca al lado de la etiqueta, permitiendo que se expanda
contraseña_input.grid(row=0, column=1, sticky='ew', padx=10, pady=5)

# Permitir que la columna con la contraseña generada se expanda cuando la ventana cambia de tamaño
frame_contraseña.grid_columnconfigure(1, weight=1)

# Iniciar la aplicación
# Mantiene la ventana abierta y en funcionamiento hasta que el usuario la cierre
ventana.mainloop()
