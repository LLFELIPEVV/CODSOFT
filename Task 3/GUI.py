import tkinter as tk

from generador import generar_contraseña as gc


# Funciones
def generar_contraseña():
    try:
        longitud = int(input.get())
        if longitud <= 0:
            raise ValueError("La longitud debe ser mayor a 0.")
        contraseña = gc(longitud)
        input.delete(0, tk.END)
        contraseña_input.config(text=contraseña)
    except ValueError:
        contraseña_input.config(text="Introduce un número válido.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de contraseñas")
""" ventana.geometry("700x500") """
ventana.config(bg="#f0f0f0")

# Crear un frame para el título
frame_titulo = tk.Frame(ventana, bg="#f0f0f0")
frame_titulo.pack(fill='x', pady=20)

# Crear un título
titulo = tk.Label(frame_titulo, text="Generador de contraseñas",
                  font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
titulo.pack()

# Crear un frame para la longitud y el botón
frame_input = tk.Frame(ventana, bg="#f0f0f0")
frame_input.pack(fill='x', padx=20, pady=10)

# Longitud de la contraseña
longitud_label = tk.Label(frame_input, text="Longitud:", font=(
    "Arial", 18), bg="#f0f0f0", fg="#333")
longitud_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')

input = tk.Entry(frame_input, font=("Arial", 18),
                 relief="solid", borderwidth=1)
input.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

# Botón para generar la contraseña
generar_button = tk.Button(frame_input, text="Generar", font=(
    "Arial", 16, "bold"), bg="#4CAF50", fg="white", relief="flat", padx=15, pady=5, command=generar_contraseña)
generar_button.grid(row=0, column=2, padx=10, pady=5)

# Configurar las columnas para que se adapten al espacio disponible
frame_input.grid_columnconfigure(1, weight=1)

# Crear un frame para la contraseña generada
frame_contraseña = tk.Frame(ventana, bg="#f0f0f0")
frame_contraseña.pack(fill='x', padx=20, pady=20)

# Etiqueta para la contraseña generada
contraseña_label = tk.Label(frame_contraseña, text="Contraseña generada:", font=(
    "Arial", 18), bg="#f0f0f0", fg="#333")
contraseña_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Campo para mostrar la contraseña generada
contraseña_input = tk.Label(frame_contraseña, text="", font=(
    "Courier New", 16, "bold"), bg="white", relief="solid", borderwidth=1, padx=10, pady=5)
contraseña_input.grid(row=0, column=1, sticky='ew', padx=10, pady=5)

# Configurar las columnas para que se adapten al espacio disponible
frame_contraseña.grid_columnconfigure(1, weight=1)

ventana.mainloop()
