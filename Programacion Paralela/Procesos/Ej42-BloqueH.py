import subprocess
import time

p = subprocess.Popen(["Taskmgr.exe"])

while p.poll() == None:
    print("Sigue abierto...")
    time.sleep(1)

print(f"Cerrado: {p.returncode}")