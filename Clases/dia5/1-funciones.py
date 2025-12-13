# FUNCIONES EN PYTHON
# Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica.
# Se define utilizando la palabra clave 'def', seguida del nombre de la funcion y parentesis.

def saludar(nombre):
    mensaje = f'Hola {nombre}'
    return mensaje

usuario = input("Hola como te llamas? ")
print(saludar(usuario))