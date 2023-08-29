'''
class Usuario:
    def __init__ (self, nombre, edad, empleado):
        self.nombre = nombre
        self.edad = edad
        self.empleado = empleado

    def aprobracion(self):
        if self.empleado == "Si":
            print("\n---------------------------------------------")
            print(f"El empleado {self.nombre} es bienvenido")
            print("---------------------------------------------\n")

        else:
            print("\n********************************************")
            print(f"El empleado {self.nombre} NO es bienvenido")
            print("********************************************\n")

empleado_1 = Usuario("David", 29, "Si")
empleado_2 = Usuario("Daniel", 27, "No")

empleado_1.aprobracion()
empleado_2.aprobracion()
'''     

#Metodos
class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Esta haciendo una llamda desde el: {self.modelo}")

    def colgar(self):
        print(f"Colgo la llamada desde el {self.modelo}")

celular_1 = Celular("pollito", "s25", "450mp")
celular_2 = Celular("gatico", "pro 25", "1520 mp")

celular_2.llamar()