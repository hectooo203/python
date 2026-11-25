import subprocess

codigo = input("Dime la frase: ")

procesoHijo = subprocess.Popen(
    ["python", "-c", "print(input()[::-1])"],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    text = True
)

salida, error = procesoHijo.communicate(input = codigo)

print(salida.strip())