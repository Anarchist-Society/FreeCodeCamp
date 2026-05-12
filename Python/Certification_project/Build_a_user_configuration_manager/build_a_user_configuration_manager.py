print('Build a User Configuration Manager\n')

# Diccionario de prueba simula configuración
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'brightness': '75'
}

# Función de añadir una configuración al diccionario
def add_setting(settings, new_setting):

    # Desempacamos los valores de la tupla y lo almacenamos en las variables key y value
    key, value = new_setting
    key = key.lower() # Lo convertimos a minúscula
    value = value.lower() # Lo convertimos a minúscula

    # Si la clave ya existe en el diccionario devolvemos error
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    # Añadimos la nueva configuración
    settings.update({key: value})

    # Devolvemos que todo fue correcto
    return f"Setting 'volume' added with value 'high' successfully!"

# Función para actualizar una configuración del diccionario
def update_setting(settings, new_setting):

    # Desempacamos los valores de la tupla y lo almacenamos en las variables key y value
    key, value = new_setting
    key = key.lower() # Lo convertimos a minúscula
    value = value.lower() # Lo convertimos a minúscula

    # Si la clave no existe en el diccionario devolvemos error
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    # Actualizamos la configuración con un nuevo valor
    settings.update({key: value})

    # Devolvemos que todo fue correcto
    return f"Setting '{key}' updated to '{value}' successfully!"

# Función para eliminar una configuración del diccionario
def delete_setting(settings, key):

    # Convertimos la clave en minúscula
    key = key.lower()

    # Si la clave no existe en el diccionario devolvemos error
    if key not in settings:
        return 'Setting not found!'

    # Eliminamos la configuración, buscando su clave
    settings.pop(key)

    # Devolvemos que todo fue correcto
    return f"Setting '{key}' deleted successfully!"

# Función para visualizar toda la configuración
def view_settings(settings):
    # Si la configuración, es decir el diccionario está vacío devolvemos error
    if not settings:
        return 'No settings available.'

    result = 'Current User Settings:\n'

    for key, value in settings.items():
        result += f"{key.title()}: {value}\n"

    return result
