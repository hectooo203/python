import subprocess
import time
import os

try:
    ComienzoProceso = time.time()
    proceso = subprocess.run(
        ["python", ".\\hijo_lento.py"],
        text=True,
        timeout=2
        )
    FinalizacionProceso = time.time()
except subprocess.TimeoutExpired:
    print(f"Proceso finalizado (A tardado mucho)")
    FinalizacionProceso = time.time()

TiempoTotal = FinalizacionProceso - ComienzoProceso

print(f"Tiempo total: {TiempoTotal}")

# while proceso.poll() is None:
#     print("Sigue vivo...")
#     time.sleep(2)
#     proceso.terminate()
#     proceso.wait()
# print(f"{"El proceso sigue vivo" if proceso.poll() is None else "El proceso no esta vivo"}. Su codigo de salida es: {proceso.returncode}")