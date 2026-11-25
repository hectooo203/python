import time
import os

print("Comienza el proceso lento")
print(f"PID: {os.getpid()}")
time.sleep(1)
print("Finaliza el proceso lento")