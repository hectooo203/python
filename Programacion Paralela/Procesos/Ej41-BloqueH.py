import subprocess

blocNotas = subprocess.Popen(["ping", "-n", "4" ,"8.8.8.8"])
print(blocNotas.poll())
print(blocNotas.pid)
print("Haciendo cosas...")
blocNotas.wait()
print(blocNotas.returncode)
print("Se cerro correctamente")


