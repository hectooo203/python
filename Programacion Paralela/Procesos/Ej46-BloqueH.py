import subprocess
import time

procesos = [
    ("a",  subprocess.Popen(["ping", "-n", "10",  "127.0.0.1"], stdout=subprocess.DEVNULL)),
    ("b",  subprocess.Popen(["ping", "-n", "7",  "127.0.0.1"], stdout=subprocess.DEVNULL)),
    ("c",  subprocess.Popen(["ping", "-n", "12",  "127.0.0.1"], stdout=subprocess.DEVNULL))
]

ganador = None
while ganador is None:
    for nombre, p in procesos:
        if p.poll() is not None:
            print(f"El proceso '{nombre}' [PID: {p.pid}] ha terminado antes con codigo {p.returncode}")
            ganador = p
            break
    time.sleep(2)
for nombre, p in procesos:
    if p != ganador:
        p.terminate()
        p.wait()
        print(f"El proceso '{nombre}' [PID: {p.pid}] ha terminado despues con codigo {p.returncode}")

