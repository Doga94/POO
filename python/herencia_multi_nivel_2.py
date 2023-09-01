class Empleados:
    def __init__(self, nombre, area) -> None:
        self.nombre = nombre
        self.area = area
        self.sigue_empleado = None

    def activo(self, contrato_activo):
        self.sigue_empleado = contrato_activo
        print("Estado en la empresa actualizado")

class Prueba(Empleados):
    def __init__(self, nombre, area, aprobo) -> None:
        super().__init__(nombre, area)
        self.aprobo = aprobo
        print("Validando data")

david = Prueba("David", "Analisis", "pendiente")
david.activo("Activo")

#Otra clase
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad= edad
        self.distancia_recorida = 0

    def __add__(self, distancia):
        self.distancia_recorida += distancia
        return self.distancia_recorida
        #print(f"{self.nombre} su distancia fue de: {self.distancia_recorida}")

paco = Persona("Paco", 25)
emilio = Persona("Emili", 22)

paco + 5
print(paco.distancia_recorida)
