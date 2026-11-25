import subprocess
import time

administradorTareas = subprocess.Popen(["Taskmgr.exe"])
acercaWindows = subprocess.Popen(["winver.exe"])
infsis = subprocess.Popen(["msinfo32.exe"])

time.sleep(5)

administradorTareas.terminate()
acercaWindows.terminate()
infsis.terminate()

