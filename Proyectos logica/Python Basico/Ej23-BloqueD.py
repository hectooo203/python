class Coche:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad
    def acelerar(self):
        self.velocidad += 15
    def __str__(self):
        return f"{self.marca}: {self.velocidad}km/h"

seat = Coche("Ibiza", 80)
toyota = Coche("Corolla", 101)
print(seat)
seat.acelerar()
print(seat)
print(toyota)
    