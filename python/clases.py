class Persona:
    tipo = "humano"

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.document_id = None

    def agregar_documento(self, document_id):
        self.document_id = document_id
        print("Documento guardado")

persona_1 = Persona("David", "Gomez", 29)
print(persona_1.nombre)
persona_1.agregar_documento(1022566888)