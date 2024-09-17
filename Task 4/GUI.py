import tkinter as tk

import tkinter.messagebox as Message
from jan_ken import jugar, combinacion

puntaje_jugador = 0
puntaje_ia = 0


# Funciones
def cambiar_puntaje(resultado):
    global puntaje_jugador, puntaje_ia
    if resultado == "Ganador":
        puntaje_jugador += 1
    elif resultado == "Perdedor":
        puntaje_ia += 1

    label_puntaje_jugador.config(text=f"{puntaje_jugador}")
    label_puntaje_ia.config(text=f"{puntaje_ia}")


def eleccion_IA():
    respuesta_ia.configure(text=jugar())
    player = opcion_usuario.get()
    IA = respuesta_ia.cget("text")
    resultado = combinacion(player, IA)
    cambiar_puntaje(resultado)

    if resultado == "Ganador":
        Message.showinfo("Resultado", "¡Ganaste! La IA eligió " + IA)
    elif resultado == "Perdedor":
        Message.showinfo("Resultado", "Perdiste. La IA eligió " + IA)
    elif resultado == "Empate":
        Message.showinfo(
            "Resultado", "Empate. Ambos eligieron " + player)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Jan Ken")
ventana.geometry("700x600")
ventana.configure(bg="#222222")

# Crear título
titulo = tk.Label(ventana, text="JAN KEN PON", font=(
    "Arial", 36, "bold"), fg="#FFD700", bg="#222222")
titulo.pack(pady=20)

# Crear frame para el puntaje
frame_puntaje = tk.Frame(ventana, bg="#222222")
frame_puntaje.pack(pady=20)

# Etiquetas sobre el marcador indicando Jugador e IA
label_jugador = tk.Label(frame_puntaje, text="Jugador",
                         font=("Arial", 14), fg="white", bg="#222222")
label_jugador.grid(row=0, column=0, padx=40)

label_ia = tk.Label(frame_puntaje, text="IA", font=(
    "Arial", 14), fg="white", bg="#222222")
label_ia.grid(row=0, column=2, padx=40)

label_puntaje_jugador = tk.Label(frame_puntaje, text=f"{puntaje_jugador}", font=(
    "Arial", 48, "bold"), fg="#4CAF50", bg="#222222")
label_puntaje_jugador.grid(row=1, column=0, padx=40)

separador_label = tk.Label(frame_puntaje, text=":", font=(
    "Arial", 48, "bold"), fg="white", bg="#222222")
separador_label.grid(row=1, column=1)

label_puntaje_ia = tk.Label(frame_puntaje, text=f"{puntaje_ia}", font=(
    "Arial", 48, "bold"), fg="#F44336", bg="#222222")
label_puntaje_ia.grid(row=1, column=2, padx=40)

# Crear frame para la elección del jugador y la IA
frame_juego = tk.Frame(ventana, bg="#222222")
frame_juego.pack(pady=40)

# Etiqueta de jugador
jugador_label = tk.Label(frame_juego, text="Tu elección:", font=(
    "Arial", 14), fg="white", bg="#222222")
jugador_label.grid(row=0, column=0, padx=10)

# Crear menú desplegable para las opciones de piedra, papel o tijeras
opciones = ["Piedra", "Papel", "Tijeras"]
opcion_usuario = tk.StringVar()
opcion_usuario.set(opciones[0])

menu_opciones = tk.OptionMenu(frame_juego, opcion_usuario, *opciones)
menu_opciones.config(width=10, font=("Arial", 14), bg="#0F7FFF", fg="white")
menu_opciones.grid(row=0, column=1, padx=10)

# Crear campo para mostrar la respuesta de la IA
ia_label = tk.Label(frame_juego, text="IA elige:", font=(
    "Arial", 14), fg="white", bg="#222222")
ia_label.grid(row=0, column=2, padx=10)

respuesta_ia = tk.Label(frame_juego, text="?", font=(
    "Arial", 14), fg="#FFD700", bg="#222222")
respuesta_ia.grid(row=0, column=3, padx=10)

# Crear botón de jugar de nuevo
boton_jugar = tk.Button(frame_juego, text="Jugar de nuevo", font=(
    "Arial", 14), bg="#4CAF50", fg="white", padx=20, pady=10, command=eleccion_IA)
boton_jugar.grid(row=0, column=4, padx=20)

# Loop principal de la ventana
ventana.mainloop()
