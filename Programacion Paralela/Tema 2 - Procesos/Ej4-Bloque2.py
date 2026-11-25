import subprocess

proceso = subprocess.run(
    ["ping", "-n", "3", "127.0.0.1"],
    capture_output=True,
    text=True
)

codSalida = proceso.returncode

lineas = len(proceso.stdout)

primeraLinea = proceso.stdout.splitlines()

ultimaLinea = proceso.stdout.splitlines()

print(f"Codigo de salida: {codSalida}. Cantidad de lineas: {lineas}. Primera linea: {primeraLinea[1]}. Ultima linea: {ultimaLinea[-1]}")