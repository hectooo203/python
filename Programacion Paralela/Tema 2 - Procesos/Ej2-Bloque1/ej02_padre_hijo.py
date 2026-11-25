import os
import subprocess

print(os.getppid())

procesoHijo = subprocess.run(
    ["python", ".\\hijo_pid.py"],
    capture_output=True,
    text=True
)

resultadoSeparado = procesoHijo.stdout.split(" ")

print(resultadoSeparado[1])