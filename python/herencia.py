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

    def ejecutar_accion (self):
        print("Hacciendo algo")
   
class Id_document:
    def id_num(self, document_id):
        self.document_id = document_id
        return "Documento se guardo"
    
class Aceptado(Persona, Id_document):
    def aprobo(self):
        if self.edad >= 20:
            return "Aprobado"
        else:
            return "No aprobo"

persona_1 = Aceptado("David", "Gomez", 29)
persona_1.id_num(1205569988)

print(f"El empleado {persona_1.nombre}. \nSu estatus es: {persona_1.aprobo()}")
print(f"Su documento es: {persona_1.document_id} y el {persona_1.id_num(persona_1.document_id)}")



