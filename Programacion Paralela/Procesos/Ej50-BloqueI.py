import subprocess

codigo = "print(int(input())*2)"
procesoHijo = subprocess.Popen(
    ["python", "-c", codigo],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

salida, error = procesoHijo.communicate(input="5")

print("stdout: ", salida.strip())
print("stderr: ", error.strip())
print("Codigo: ", procesoHijo.returncode)