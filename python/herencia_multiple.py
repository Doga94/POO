class AnimalAereo: # clase padre
    def comer(self):
        print("Animal aéreo comiendo")

    def volar(self): # clase padre
        print("Volando")

class AnimalTerrestre:
    def comer(self):
        print("Animal terrestre comiendo")

    def caminar(self): 
        print("Caminando")

class Pajaro(AnimalAereo, AnimalTerrestre): # clase hija
    pass

pato = Pajaro()
pato.volar()
pato.caminar()