import tkinter as tk

# Create the main window
ventana = tk.Tk()

ventana.title("Calculadora")
ventana.geometry("500x600")
ventana.configure(bg="#141414")

input = tk.Entry(ventana, font=("Arial", 20), justify='right',
                 bd=10, bg="#303030", fg="white")
input.pack(fill="x", padx=20, pady=(20, 0), ipady=6)

# Crear un frame para los botones
frame_botones = tk.Frame(ventana, bg="#141414")
frame_botones.pack(expand=True, fill="both", padx=20, pady=(0, 20))

# Lista de botones de la calculadora
botones = [
    ('AC', 1, 0, 1, '#01570F'), ('Borrar', 1,
                                 1, 2, "#700000"), ('/', 1, 3, 1, "#264A74"),
    ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2), ('*', 2, 3, 1, "#264A74"),
    ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2), ('-', 3, 3, 1, "#264A74"),
    ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2), ('+', 4, 3, 1, "#264A74"),
    ('0', 5, 0, 1), ('.', 5, 1, 1), ('=', 5, 2, 2, "#002057")
]

# Crear los botones y asignarlos al grid
def crear_boton(texto, fila, columna, colspan=1, bg_color='#303030', fg_color='white'):
    boton = tk.Button(frame_botones, text=texto, font=(
        "Arial", 18), bd=5, bg=bg_color, fg=fg_color)
    boton.grid(row=fila, column=columna, columnspan=colspan, sticky='nsew')


for boton in botones:
    crear_boton(*boton)

# Hacer que las filas y columnas del grid se expandan uniformemente
for i in range(6):
    frame_botones.grid_rowconfigure(i, weight=1)

for j in range(4):
    frame_botones.grid_columnconfigure(j, weight=1)

ventana.mainloop()
