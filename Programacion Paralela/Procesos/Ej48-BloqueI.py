import subprocess

doble = "print(f'Doble de {input()}: {int(input())*2}')"

procesoHijo = subprocess.Popen(
    ["python", "-c", doble],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

try:
    salida, error = procesoHijo.communicate(input = "5\n" * 2)
    # Apartir de aqui da fallo ya que solo se puede llamar una vez al procesoHijo
    salida, error = procesoHijo.communicate(input = "10")
    salida, error = procesoHijo.communicate(input = "20")
except ValueError as e:
    print("No se puede llamar mas de 1 vez al procesoHijo")

print(salida.strip())
procesoHijo.terminate()