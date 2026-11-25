import subprocess

frase = input("Escribe tu frase: ")

proceso = subprocess.Popen(
    ["python", "-c", "print(f'Su frase contiene: {len(input())} caracteres')"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

salida, error = proceso.communicate(input=frase)

print(salida.strip())


