import json


# Función para leer el archivo JSON que contiene las tareas
def leer_archivo_json():
    try:
        # Intenta abrir el archivo JSON en modo lectura ('r')
        with open('tareas.json', 'r') as archivo:
            # Lee el contenido del archivo y lo convierte de JSON a un diccionario de Python
            datos = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no se encuentra (por ejemplo, si es la primera vez que se ejecuta el programa)
        datos = {}  # Inicializa un diccionario vacío

    return datos  # Devuelve el diccionario con los datos del archivo JSON


# Función para actualizar el archivo JSON con nuevos datos
def actualizar_archivo_json(datos):
    # Abre el archivo JSON en modo escritura ('w')
    with open('tareas.json', 'w') as archivo:
        # Convierte el diccionario de Python a formato JSON y lo escribe en el archivo
        # 'indent=4' añade sangrías para hacer el archivo JSON más legible
        json.dump(datos, archivo, indent=4)
