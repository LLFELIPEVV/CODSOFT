import tkinter as tk
import tkinter.messagebox as Message

from jan_ken import jugar, combinacion

# Variables globales para llevar la cuenta de los puntajes
puntaje_jugador = 0
puntaje_ia = 0


# Función para actualizar el puntaje según el resultado del juego
def cambiar_puntaje(resultado):
    # Se indican las variables globales a modificar
    global puntaje_jugador, puntaje_ia
    if resultado == "Ganador":  # Si el jugador gana
        puntaje_jugador += 1
    elif resultado == "Perdedor":  # Si el jugador pierde
        puntaje_ia += 1

    # Actualizar las etiquetas que muestran los puntajes en la interfaz
    label_puntaje_jugador.config(text=f"{puntaje_jugador}")
    label_puntaje_ia.config(text=f"{puntaje_ia}")


# Función para manejar la elección de la IA y determinar el resultado del juego
def eleccion_IA():
    # La IA hace su elección usando la función jugar()
    respuesta_ia.configure(text=jugar())
    player = opcion_usuario.get()  # Se obtiene la opción elegida por el jugador
    IA = respuesta_ia.cget("text")  # Se obtiene la elección que hizo la IA
    resultado = combinacion(player, IA)  # Se determina el resultado del juego
    cambiar_puntaje(resultado)  # Se actualiza el puntaje según el resultado

    # Dependiendo del resultado, se muestra una ventana emergente con el mensaje adecuado
    if resultado == "Ganador":
        Message.showinfo("Resultado", "¡Ganaste! La IA eligió " + IA)
    elif resultado == "Perdedor":
        Message.showinfo("Resultado", "Perdiste. La IA eligió " + IA)
    elif resultado == "Empate":
        Message.showinfo("Resultado", "Empate. Ambos eligieron " + player)


# Crear la ventana principal
ventana = tk.Tk()  # Se crea la ventana principal con Tkinter
ventana.title("Jan Ken")  # Se establece el título de la ventana
ventana.geometry("700x600")  # Se define el tamaño de la ventana
ventana.configure(bg="#222222")  # Se establece el color de fondo

# Crear título
titulo = tk.Label(ventana, text="JAN KEN PON", font=(
    "Arial", 36, "bold"), fg="#FFD700", bg="#222222")  # Etiqueta para el título
titulo.pack(pady=20)  # Se empaqueta el título con un espacio vertical

# Crear frame para el puntaje
# Frame que contendrá los puntajes
frame_puntaje = tk.Frame(ventana, bg="#222222")
frame_puntaje.pack(pady=20)  # Se empaqueta el frame con un espacio vertical

# Etiquetas para indicar "Jugador" e "IA" sobre el marcador
label_jugador = tk.Label(frame_puntaje, text="Jugador",
                         font=("Arial", 14), fg="white", bg="#222222")
# Posicionamiento en la cuadrícula
label_jugador.grid(row=0, column=0, padx=40)

label_ia = tk.Label(frame_puntaje, text="IA", font=(
    "Arial", 14), fg="white", bg="#222222")
label_ia.grid(row=0, column=2, padx=40)  # Etiqueta para "IA"

# Etiquetas para mostrar los puntajes del jugador y de la IA
label_puntaje_jugador = tk.Label(frame_puntaje, text=f"{puntaje_jugador}", font=(
    "Arial", 48, "bold"), fg="#4CAF50", bg="#222222")
label_puntaje_jugador.grid(row=1, column=0, padx=40)

separador_label = tk.Label(frame_puntaje, text=":", font=(
    "Arial", 48, "bold"), fg="white", bg="#222222")
# Etiqueta para el separador de los puntajes (":")
separador_label.grid(row=1, column=1)

label_puntaje_ia = tk.Label(frame_puntaje, text=f"{puntaje_ia}", font=(
    "Arial", 48, "bold"), fg="#F44336", bg="#222222")
# Etiqueta para mostrar el puntaje de la IA
label_puntaje_ia.grid(row=1, column=2, padx=40)

# Crear frame para la elección del jugador y la IA
# Frame que contendrá las elecciones del jugador y la IA
frame_juego = tk.Frame(ventana, bg="#222222")
frame_juego.pack(pady=40)  # Se empaqueta el frame con un espacio vertical

# Etiqueta para indicar la elección del jugador
jugador_label = tk.Label(frame_juego, text="Tu elección:", font=(
    "Arial", 14), fg="white", bg="#222222")
# Se posiciona en la primera columna del frame
jugador_label.grid(row=0, column=0, padx=10)

# Menú desplegable para que el jugador elija entre piedra, papel o tijeras
opciones = ["Piedra", "Papel", "Tijeras"]
# Se define una variable de tipo string para almacenar la opción del jugador
opcion_usuario = tk.StringVar()
# Se establece "Piedra" como la opción predeterminada
opcion_usuario.set(opciones[0])

# Crear el menú desplegable
menu_opciones = tk.OptionMenu(frame_juego, opcion_usuario, *opciones)
# Se configura el estilo del menú
menu_opciones.config(width=10, font=("Arial", 14), bg="#0F7FFF", fg="white")
menu_opciones.grid(row=0, column=1, padx=10)  # Se posiciona en la cuadrícula

# Etiqueta para mostrar la elección de la IA
ia_label = tk.Label(frame_juego, text="IA elige:", font=(
    "Arial", 14), fg="white", bg="#222222")
ia_label.grid(row=0, column=2, padx=10)

# Etiqueta para mostrar la respuesta de la IA
respuesta_ia = tk.Label(frame_juego, text="?", font=(
    "Arial", 14), fg="#FFD700", bg="#222222")
respuesta_ia.grid(row=0, column=3, padx=10)

# Botón para iniciar una nueva ronda
boton_jugar = tk.Button(frame_juego, text="Jugar de nuevo", font=(
    "Arial", 14), bg="#4CAF50", fg="white", padx=20, pady=10, command=eleccion_IA)
# Se posiciona en la cuadrícula y ejecuta la función eleccion_IA al hacer clic
boton_jugar.grid(row=0, column=4, padx=20)

# Iniciar el loop principal de la ventana
ventana.mainloop()  # Se inicia el loop de eventos de la ventana
