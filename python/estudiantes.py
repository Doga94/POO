class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")

    def cumple_anios(self):
        self.edad += 1

nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
grado = input("Digite su grado: ")

estudiante = Estudiante(nombre, edad, grado)

estudiante.cumple_anios()

print(f"""
        DATOS DEL ESTUDIANTE: \n\n
        Nombre: {estudiante.nombre} \n
        Edad: {estudiante.edad} \n
        Grado: {estudiante.grado} \n
""")


while True:
    estudiar = input("¿Desea estudiar? \n(Escriba 'estudiar' para estudiar o 'salir' para salir): \n")
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
    elif(estudiar.lower() == "salir"):
        print("Hasta luego")
        break
    