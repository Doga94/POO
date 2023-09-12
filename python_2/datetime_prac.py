from datetime import datetime

# Importa el módulo `datetime`.

ahora = datetime.now()
# Obtiene la fecha y hora actual.

print(ahora, type(ahora))
# Imprime la fecha y hora actual.


fecha = ahora.strftime("%Y-%m-%d")
# Formatea la fecha y hora actual en el formato "YYYY-MM-DD".

print(fecha, type(fecha))
# Imprime la fecha formateada.

format_24h = ahora.strftime("%H:%M:%S")
# Formatea la fecha y hora actual en el formato "HH:MM:SS".

print(format_24h, type(format_24h))
# Imprime la fecha y hora formateada en formato 24 horas.

format_12h = ahora.strftime("%I:%M:%S %p")
# Formatea la fecha y hora actual en el formato "hh:mm:ss a".

print(format_12h)
# Imprime la fecha y hora formateada en formato 12 horas.
