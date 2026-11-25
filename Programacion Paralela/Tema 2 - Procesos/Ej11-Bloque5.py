import subprocess

WINDOWS = True

proceso = subprocess.run(
    ["cmd", "/c", "mkdir", "prueba_psp"]
)

print(f"Codigo de salida: {proceso.returncode}")

proceso2 = subprocess.run(
    ["cmd", "/c", "dir", "in", "prueba_psp"],
    capture_output=True
)

print(f"Ubicacion y existencia de la carpeta prueba_psp {proceso2.stdout}")

proceso3 = subprocess.run(
    ["cmd", "/c", "where", "python"],
    capture_output=True
)

print(f"Ruta de python: {proceso3.stdout}")


