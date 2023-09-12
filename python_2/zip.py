# Crea dos listas, una de nombres y otra de edades.
lista_nombres = ["David", "Martha", "Sandra", "Jorge"]
lista_edades = [29, 30, 15, 18]

# Utiliza la función `zip()` para combinar las dos listas en una sola lista de tuplas.
# Cada tupla contiene un nombre y una edad.
datos_zip = zip(lista_nombres, lista_edades)

# Imprime la lista de tuplas.
print(list(datos_zip))

# Utiliza un bucle for para recorrer la lista de tuplas.
# Imprime cada nombre y edad en una línea separada.
for nombre, edad in zip(lista_nombres, lista_edades):
    print(nombre, edad)
