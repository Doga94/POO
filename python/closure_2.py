def agregar_persona_directorio():
    directorio = {}
    def agregar(nombre, edad, ciudad):
        directorio[nombre] = {"edad": edad, "ciudad": ciudad}
        return directorio
    return agregar


almacenar = agregar_persona_directorio()
directorio = almacenar("David", 29, "Bogota")
directorio = almacenar("Orlandi", 45, "Soacha")
print(directorio)

for nombre in directorio:
    print(nombre)