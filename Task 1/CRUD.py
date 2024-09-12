from modificacion_json import leer_archivo_json, actualizar_archivo_json


# Crear la tarea
def crear_tarea(tarea):
    datos = leer_archivo_json()
    if datos:
        nuevo_id = str(max([int(i) for i in datos.keys()]) + 1)
    else:
        nuevo_id = "1"
    datos[nuevo_id] = {"tarea": tarea, "completada": False}
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
def actualizar_tarea(id, tarea, completada=None):
    datos = leer_archivo_json()
    if id in datos:
        if completada is not None:
            datos[id] = {"tarea": tarea, "completada": completada}
        else:
            datos[id] = {"tarea": tarea, "completada": datos[id]["completada"]}
        try:
            actualizar_archivo_json(datos)
        except Exception as e:
            print(f"Error al actualizar el archivo JSON: {e}")
    else:
        print("La tarea no existe")


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
