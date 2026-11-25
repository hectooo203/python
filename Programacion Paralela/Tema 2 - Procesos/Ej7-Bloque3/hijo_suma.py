import sys

try:
    numeros = [int(x) for x in input().split(" ")]
    print(f"Cantidad de numeros: {len(numeros)}. Suma total: {sum(numeros)}")
except ValueError:
    print("La lista contiene letras")
    sys.exit(1)