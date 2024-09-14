import tkinter as tk

from calculator import Calculadora

# Crear una instancia de la calculadora.
calculadora = Calculadora()


# Definir una función que se ejecutará cuando se haga clic en un botón de la calculadora.
def click_boton(texto):
    # Si el botón presionado es 'AC' (All Clear), limpia la entrada y la calculadora.
    if texto == 'AC':
        input.delete(0, tk.END)  # Limpia el campo de entrada.
        calculadora.limpiar()  # Limpia los datos de la calculadora.
    # Si el botón presionado es 'Borrar', elimina el último carácter de la entrada.
    elif texto == 'Borrar':
        # Elimina el último carácter.
        input.delete(len(input.get())-1, tk.END)
    # Si el botón presionado es un operador ('+', '-', '*', '/'), configura la operación actual.
    elif texto in ('+', '-', '*', '/'):
        # Si hay un número en la entrada, lo guarda en la calculadora y configura la operación.
        if input.get():
            # Guarda el número en la calculadora.
            calculadora.set_num(float(input.get()))
            calculadora.set_operacion(texto)  # Configura la operación.
            input.delete(0, tk.END)  # Limpia la entrada.
    # Si el botón presionado es '=', calcula el resultado de la operación actual.
    elif texto == '=':
        # Si hay un número en la entrada, lo usa para el cálculo.
        if input.get():
            # Guarda el número en la calculadora.
            calculadora.set_num(float(input.get()))
            resultado = calculadora.calcular()  # Calcula el resultado.
            input.delete(0, tk.END)  # Limpia la entrada.
            # Muestra el resultado en la entrada.
            input.insert(tk.END, resultado)
    # Si el botón presionado es un número o el punto decimal, lo añade a la entrada.
    else:
        # Añade el texto al final de la entrada.
        input.insert(tk.END, texto)


# Crea la ventana principal de la calculadora.
ventana = tk.Tk()

# Configura el título y el tamaño de la ventana.
ventana.title("Calculadora")
ventana.geometry("500x600")  # Ancho x Alto en píxeles.
ventana.configure(bg="#141414")  # Color de fondo de la ventana.

# Crea un campo de entrada para mostrar los números y resultados.
input = tk.Entry(ventana, font=("Arial", 20), justify='right',
                 bd=10, bg="#303030", fg="white")  # Configura el aspecto del campo de entrada.
# Coloca el campo de entrada en la ventana.
input.pack(fill="x", padx=20, pady=(20, 0), ipady=6)

# Crea un marco (frame) para contener los botones de la calculadora.
frame_botones = tk.Frame(ventana, bg="#141414")
# Coloca el marco en la ventana.
frame_botones.pack(expand=True, fill="both", padx=20, pady=(0, 20))

# Lista de botones que se mostran en la calculadora.
# Cada botón tiene: texto, fila, columna, columnas combinadas, color de fondo (opcional), color de texto (opcional).
botones = [
    ('AC', 1, 0, 1, '#01570F'), ('Borrar', 1, 1,
                                 2, "#700000"), ('/', 1, 3, 1, "#264A74"),
    ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2), ('*', 2, 3, 1, "#264A74"),
    ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2), ('-', 3, 3, 1, "#264A74"),
    ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2), ('+', 4, 3, 1, "#264A74"),
    ('0', 5, 0, 1), ('.', 5, 1, 1), ('=', 5, 2, 2, "#002057")
]


# Definir una función para crear un botón con el texto, fila, columna, y colores especificados.
def crear_boton(texto, fila, columna, colspan=1, bg_color='#303030', fg_color='white'):
    boton = tk.Button(frame_botones, text=texto, font=(
        "Arial", 18), bd=5, bg=bg_color, fg=fg_color, command=lambda: click_boton(texto))
    boton.grid(row=fila, column=columna, columnspan=colspan, sticky='nsew')


# Crear todos los botones según la lista y los coloca en el marco.
for boton in botones:
    crear_boton(*boton)

# Configura el grid del marco para que las filas y columnas se expandan uniformemente.
for i in range(6):
    # Hace que las filas se expandan proporcionalmente.
    frame_botones.grid_rowconfigure(i, weight=1)

for j in range(4):
    # Hace que las columnas se expandan proporcionalmente.
    frame_botones.grid_columnconfigure(j, weight=1)

# Inicia el bucle principal de la interfaz gráfica, que mantiene la ventana abierta.
ventana.mainloop()
