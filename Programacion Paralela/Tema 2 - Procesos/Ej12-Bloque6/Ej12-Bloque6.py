import subprocess
import time

copia = subprocess.Popen(
    ["python", "hijo_lento.py"],
    
)

informe = subprocess.Popen(
    ["python", "hijo_lento2.py"]
)

fallida = subprocess.Popen(
    ["python", "-c", "import sys; sys.exit(3)"]
)

colgada = subprocess.run(
    ["python", "hijo_lento3.py"],
    timeout=4
)

saludo = subprocess.Popen(
    ["python", "-c", "print('hola')"]
)