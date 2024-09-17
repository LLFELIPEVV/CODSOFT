import random

opciones = ["Piedra", "Papel", "Tijeras"]

ganador = {"Piedra": "Tijeras", "Papel": "Piedra", "Tijeras": "Papel"}


def jugar():
    return random.choice(opciones)


def combinacion(player, IA):
    if ganador[player] == IA:
        return "Ganador"
    elif player == IA:
        return "Empate"
    else:
        return "Perdedor"
