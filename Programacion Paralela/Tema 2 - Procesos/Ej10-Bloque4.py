from multiprocessing import Pool
import time
import math

def es_primo(n):
    if n < 2:
        return None
    if n == 2:
        return n
    if n % 2 == 0:
        return None
    limite = math.isqrt(n) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return None
    return n
    
def contar_primos(rango):
    cantidadPrimos = []
    for i in rango:
        resultado = es_primo(i)
        if resultado is not None:
            cantidadPrimos.append(resultado)
    return len(cantidadPrimos)

if __name__ == "__main__":
    cominezo = time.time()
    rangoTotal = range(2, 1_000_000)
    trozos = [
        rangoTotal[2:250_000],
        rangoTotal[250_000:500_000],
        rangoTotal[500_000:750_000],
        rangoTotal[750_000:],
    ]
    with Pool(4) as p:
        print(f"Cantidad de numeros primos en el rango: {sum(p.map(contar_primos, trozos))}")
    final = time.time()

    Total = final - cominezo
    print(f"Timpo total de ejecucion: {Total} segundos")