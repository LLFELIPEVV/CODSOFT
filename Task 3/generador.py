import random


def generar_contraseña(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    return ''.join(random.choices(caracteres, k=longitud))
