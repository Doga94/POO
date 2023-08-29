class Persona:
    def __init__(self, nombre: str, posicion: int) -> None:
        self.nombre = nombre
        self.posicion = posicion
    
    def caminar(self, distancia_km: int) -> int:
        self.posicion += distancia_km
        return self.posicion
    
persona_1 = Persona(nombre= "David", posicion= 1)
posicion_p1 = persona_1.caminar(distancia_km= 2)

print(f"\nEl corredor {persona_1.nombre}")
print(f"Esta en la posicion {posicion_p1}\n")