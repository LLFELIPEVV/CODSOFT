import json

from .modificacion_json import leer_archivo_json, actualizar_archivo_json

# Crear la tarea
def crear_tarea(tarea):
    datos = leer_archivo_json()
    datos.append(tarea)
    try:
        actualizar_archivo_json(datos)
    except Exception as e:
        print(f"Error al actualizar el archivo JSON: {e}")

# Leer la tarea
def leer_tarea(id):
    try:
        datos = leer_archivo_json()
        return datos[id]
    except IndexError:
        return "La tarea no existe"

# Actualizar la tarea
def actualizar_tarea(id, nueva_tarea):
    try:
        datos = leer_archivo_json()
        datos[id] = nueva_tarea
        actualizar_archivo_json(datos)
    except IndexError:
        print("La tarea no existe")
    except Exception as e:
        print(f"Error al actualizar el archivo JSON: {e}")

# Eliminar la tarea
def eliminar_tarea(id):
    try:
        datos = leer_archivo_json()
        del datos[id]
        actualizar_archivo_json(datos)
    except IndexError:
        print("La tarea no existe")
    except Exception as e:
        print(f"Error al actualizar el archivo JSON: {e}")
