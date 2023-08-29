class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.document_id = None
        self.correo = None

    def agregar_document(self, id_document):
        self.document_id = id_document
        print("Documento guardado")

    def agregar_correo(self, add_correo):
        self.correo = add_correo
        print("Correo guardado")

persona_1 = Persona("David", "Gomez", 29)
print(persona_1.nombre)

persona_1.agregar_document(10222365855)

correo = persona_1.nombre.lower() + "." + persona_1.apellido.lower() + "@empresa.com"
persona_1.agregar_correo(correo)
print(persona_1.correo)