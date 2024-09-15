import random


def generar_contraseña(longitud):
    # Define una cadena que contiene todos los caracteres posibles que se pueden usar en la contraseña:
    # letras minúsculas (a-z), letras mayúsculas (A-Z), números (0-9) y símbolos especiales (!@#$%^&*()?).
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"

    # Usar la función `random.choices` para seleccionar aleatoriamente 'k' caracteres de la cadena anterior.
    # 'k' en este caso es la longitud que el usuario ha especificado para la contraseña.
    # ''.join(...) une todos los caracteres seleccionados aleatoriamente en una sola cadena (es decir, la contraseña final).
    return ''.join(random.choices(caracteres, k=longitud))
