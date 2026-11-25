import subprocess
import time

proceso1 = subprocess.Popen(["python", "-c", "print('Hola')"])
proceso2 = subprocess.Popen(["python", "-c", "print('Hola2')"])
proceso3 = subprocess.Popen(["python", "-c", "print('Hola3')"])

PIDs = [proceso1.pid, proceso2.pid, proceso3.pid]

time.sleep(2)

recogidaProcesos = subprocess.run(
    ["tasklist", "/FO", "CSV", "/NH"],
    capture_output=True,
    text=True
)

print(recogidaProcesos.stdout)

contador = 0
for i in recogidaProcesos.stdout:
    for f in PIDs:
        if "<defunct>" in i and f in i:
            contador += 1

proceso1.poll()
proceso2.poll()
proceso2.poll()

contador2 = 0
for i in recogidaProcesos.stdout:
    for f in PIDs:
        if "<defunct>" in i and f in i:
            contador2 += 1

print(f"Procesos Zombie: {contador}. Procesos tras recoger: {contador2}")