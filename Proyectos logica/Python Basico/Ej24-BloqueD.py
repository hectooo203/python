class Vehiculo:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad
    def acelerar(self):
        self.velocidad += 15
    def sonido(self):
        raise NotImplementedError
    def __str__(self):
        return f"Marca: {self.marca}. Velocidad: {self.velocidad}."

class Moto(Vehiculo):
    def sonido(self):
        return "Brrrr"

suzuki = Moto("Suzuki", 70)
suzuki.acelerar()
print(suzuki)
print(suzuki.sonido())