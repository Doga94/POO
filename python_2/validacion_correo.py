"""
importa el módulo re de la biblioteca estándar de Python.
El módulo re proporciona funciones para trabajar con expresiones regulares.
"""
import re


def validacion_correo(email):
    """
    Esta función valida un correo electrónico.

    La expresión regular utilizada es la siguiente:

    ^([a-z0-9]+[-_.])*[a-z0-9]*@[a-z0-9]+(\.[a-z]{2,})+$

    Si el correo electrónico coincide con el formato válido, devuelve True.
    De lo contrario, devuelve False.
    """
    formato_valido = r"^([a-z0-9]+[-_.])*[a-z0-9]*@[a-z0-9]+(\.[a-z]{2,})+$"
    # Esta expresión regular define el formato válido para un correo electrónico
    if re.match(formato_valido, email, re.IGNORECASE):
        # Si el correo electrónico coincide con el formato válido, devuelve True
        return True
    # De lo contrario, devuelve False
    return False

valido = validacion_correo("david@ejemplo.co")
print("Email valido:", valido)
