procesos = [
    {"pid": 4212, "nombre": "python.exe", "cpu": 12.5, "memoria": 85},
    {"pid": 1080, "nombre": "chrome.exe", "cpu": 34.0, "memoria": 640}
]

print(f"{'#':<3} {'PID':<6} {'NOMBRE':<12} {'CPU%':>5} {'MEM':>6}")

memoria_total = 0

for i, proc in enumerate(procesos):

    pid = proc["pid"]
    nombre = proc["nombre"]
    cpu = proc["cpu"]
    memoria = proc["memoria"]

    memoria_total += memoria
    print(f"{i+1:<3} {pid:<6} {nombre:<12} {cpu:>5} {memoria:>6} MB")

print(f"Memoria total: {memoria_total}")


