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
            