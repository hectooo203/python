class Vehiculo:
    contador = 0
    def __init__(self, marca):
        self.marca = marca
        Vehiculo.contador += 1
    def __str__(self):
        return f"{self.marca}"
    @classmethod
    def mostrar_contador(cls):
        return f"{cls.contador}"
    @staticmethod
    def comprobar(numero):
        return numero%2==0

coche1 = Vehiculo("Toyota")
coche2 = Vehiculo("Suzuki")
coche3 = Vehiculo("Seat")
print(coche1, coche2, coche3)
print(Vehiculo.mostrar_contador())
print(Vehiculo.comprobar(Vehiculo.contador))