#scope global
fecha = "01-01-1994"

def function_scope_local():
    nombre = "David"
    return nombre

def function_principal():
    nombre = "David"
    def anidada():
        print(nombre)
    anidada()

function_principal()

def saludar():
    mensaje = "Buen día"

    def imprimir_saludo():
        print(mensaje)

    return imprimir_saludo

saludo = saludar()
saludo()
