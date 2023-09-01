class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.document_id = None

    def agregar_documento_id(self, number_document):
        self.document_id = number_document
        print("Document save")

    def ejecutar_accion(self):
        print("Haciendo algo")

class Deportista(Persona):
    def __init__(self, nombre, apellido, edad, deporte) -> None:
        super().__init__(nombre, apellido, edad)
        self.deporte = deporte

    def ejecutar_accion(self):
        super().ejecutar_accion()
        print(f"Practicando {self.deporte}")

class   Taewondistas(Deportista):
    def __init__(self, nombre, apellido, edad) -> None:
        self.deporte = "Taewondo"
        super().__init__(nombre, apellido, edad, self.deporte)

    def patada(self):
        print("Patiando")

david = Taewondistas("David", "Apellido", 29)
david.ejecutar_accion()
print(david.deporte)
david.agregar_documento_id(548555)