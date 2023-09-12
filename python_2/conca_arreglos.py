# Declara tres listas: `lista_append`, `lista_extend` y `lista_insert`.
lista_append = [1, 2, 3]
lista_extend = [4, 5, 6]
lista_insert = [7, 8, 9]

# Declara una lista de letras: `lista_letras`.
lista_letras = ["a", "b", "c"]

# Agrega la lista `lista_letras` al final de `lista_append`.
lista_append.append(lista_letras)
# Imprime `lista_append`.
print(lista_append)

# Agrega los elementos de la lista `lista_letras` al final de `lista_extend`.
lista_extend.extend(lista_letras)
# Imprime `lista_extend`.
print(lista_extend)

# Inserta la lista `lista_letras` en la posición 2 de `lista_insert`.
lista_insert.insert(2, lista_letras)
# Imprime `lista_insert`.
print(lista_insert)
