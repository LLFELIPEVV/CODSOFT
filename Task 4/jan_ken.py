import random

# Lista de opciones disponibles en el juego
opciones = ["Piedra", "Papel", "Tijeras"]

# Diccionario que define qué opción gana contra cuál
ganador = {"Piedra": "Tijeras", "Papel": "Piedra", "Tijeras": "Papel"}


def jugar():
    """
    Selecciona aleatoriamente una opción para la IA entre Piedra, Papel o Tijeras.

    Returns:
        str: La opción seleccionada por la IA.
    """
    return random.choice(opciones)  # Retorna una opción aleatoria de la lista


def combinacion(player, IA):
    """
    Determina el resultado del juego comparando la elección del jugador y la IA.

    Args:
        player (str): La opción elegida por el jugador.
        IA (str): La opción elegida por la IA.

    Returns:
        str: El resultado del juego: "Ganador", "Empate", o "Perdedor".
    """
    if ganador[player] == IA:
        return "Ganador"  # El jugador gana
    elif player == IA:
        return "Empate"  # Empate, ambos eligieron lo mismo
    else:
        return "Perdedor"  # La IA gana
