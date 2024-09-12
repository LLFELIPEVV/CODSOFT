from modificacion_json import leer_archivo_json, actualizar_archivo_json


# Crear una nueva tarea
def crear_tarea(tarea):
    datos = leer_archivo_json()  # Lee las tareas existentes desde el archivo JSON

    if datos:  # Si hay tareas en el archivo
        # Encuentra el ID máximo actual, convierte todos los IDs a enteros, encuentra el máximo y suma 1
        nuevo_id = str(max([int(i) for i in datos.keys()]) + 1)
    else:  # Si no hay tareas, empieza con el ID 1
        nuevo_id = "1"

    # Añade la nueva tarea al diccionario de tareas
    datos[nuevo_id] = {"tarea": tarea, "completada": False}

    try:
        # Guarda las tareas actualizadas en el archivo JSON
        actualizar_archivo_json(datos)
    except Exception as e:  # Maneja errores al guardar el archivo
        print(f"Error al actualizar el archivo JSON: {e}")


# Leer una tarea específica por su ID
def leer_tarea(id):
    try:
        datos = leer_archivo_json()  # Lee las tareas desde el archivo JSON
        return datos[id]  # Devuelve la tarea con el ID especificado
    except KeyError:  # Si el ID no se encuentra en el archivo
        return "La tarea no existe"  # Mensaje de error


# Actualizar una tarea existente
def actualizar_tarea(id, tarea, completada=None):
    datos = leer_archivo_json()  # Lee las tareas desde el archivo JSON

    if id in datos:  # Si el ID de la tarea existe en el archivo
        if completada is not None:  # Si se ha proporcionado un nuevo estado de completado
            # Actualiza la tarea con el nuevo estado
            datos[id] = {"tarea": tarea, "completada": completada}
        else:
            # Mantiene el estado de completado actual
            datos[id] = {"tarea": tarea, "completada": datos[id]["completada"]}
        try:
            # Guarda las tareas actualizadas en el archivo JSON
            actualizar_archivo_json(datos)
        except Exception as e:  # Maneja errores al guardar el archivo
            print(f"Error al actualizar el archivo JSON: {e}")
    else:  # Si el ID de la tarea no se encuentra en el archivo
        print("La tarea no existe")  # Mensaje de error


# Eliminar una tarea por su ID
def eliminar_tarea(id):
    try:
        datos = leer_archivo_json()  # Lee las tareas desde el archivo JSON
        del datos[id]  # Elimina la tarea con el ID especificado
        # Guarda las tareas actualizadas en el archivo JSON
        actualizar_archivo_json(datos)
    except KeyError:  # Si el ID no se encuentra en el archivo
        print("La tarea no existe")  # Mensaje de error
    except Exception as e:  # Maneja otros errores al guardar el archivo
        print(f"Error al actualizar el archivo JSON: {e}")
