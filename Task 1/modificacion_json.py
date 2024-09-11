import json

# Abre el archivo JSON en modo lectura


def leer_archivo_json():
    try:
        with open('tareas.json', 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = {}

    return datos


def actualizar_archivo_json(datos):
    with open('tareas.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4) 
