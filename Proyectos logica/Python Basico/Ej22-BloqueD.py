def crear_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero*multiplicador
    return multiplicar

doble = crear_multiplicador(2)
triple = crear_multiplicador(3)

print(f"{doble(6)}, {triple(6)}")