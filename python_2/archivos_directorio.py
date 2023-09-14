# Importar el módulo os para acceder a funciones del sistema operativo
import os

# Definir una función para listar los archivos de una ruta
def listar_archivos(ruta):
    # Obtener una lista con los nombres de los archivos y carpetas de la ruta
    listar_archivos = os.listdir(ruta)
    # Devolver la lista
    return listar_archivos

# Obtener la ruta absoluta del directorio actual
ruta_absoluta = os.getcwd()

# Obtener la ruta relativa a la ruta absoluta
ruta_relativa = "java/"

# Listar los archivos de la ruta absoluta
archivos = listar_archivos(ruta_absoluta)

# Imprimir la lista de archivos
print(archivos)