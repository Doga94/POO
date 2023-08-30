class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.document_id = None

    def add_document_id(self, number_document):
        self.document_id = number_document
        print("Document save")

    def ejecutar_accion(self):
        print("Haciendo algo")

class Deportista (Persona):
    def __init__(self, nombre, apellido, edad, deporte):
        super().__init__(nombre, apellido, edad)
        self.deporte = deporte

    def ejecutar_accion(self):
        super().ejecutar_accion()
        print(f"Practicando {self.deporte}")

david = Deportista("David", "Gomez", 29, "Taewondo")
david.add_document_id(12355866522)
print(david.deporte)
david.ejecutar_accion()