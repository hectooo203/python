import subprocess
import time

def comando_tarea(nombre, segundos):
    return ['python', '-c', f'import time; print("Comienza {nombre}"); time.sleep({segundos}); print("Finaliza {nombre}"))']

proceso = subprocess.Popen(
    comando_tarea(input(), input()),
    stdin= subprocess.PIPE,
    stdout= subprocess.PIPE,
    stderr= subprocess.PIPE,
    text=True
)

salida, error = proceso.communicate(input="A \n 1")

print(salida.strip())