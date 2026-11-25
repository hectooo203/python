import subprocess

proceso = subprocess.Popen(
    ["python", ".\\hijo_suma.py"],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    text=True
)

salida, error = proceso.communicate(input="4 8 15 16 23 42")

print(f"Salida: {salida.strip()}. Codigo salida: {proceso.returncode}")