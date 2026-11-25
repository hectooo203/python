import subprocess
import time

administradorTareas = subprocess.Popen(["Taskmgr.exe"])
acercaWindows = subprocess.Popen(["winver.exe"])
infsis = subprocess.Popen(["msinfo32.exe"])
versionPython = subprocess.Popen(["ping", "-t", "8.8.8.8"])
mapaCaracteres = subprocess.Popen(["charmap.exe"])

time.sleep(5)

administradorTareas.terminate()
acercaWindows.terminate()
infsis.terminate()
versionPython.terminate()

print(f"Codigo Administrador de Tareas: {administradorTareas.returncode}. Codigo acerca Windows: {acercaWindows.returncode}. Codigo Informacion del Sistema: {infsis.returncode}. Codigo ping: {versionPython.returncode}. Codigo mapa de Caracteres: {mapaCaracteres.returncode}")
