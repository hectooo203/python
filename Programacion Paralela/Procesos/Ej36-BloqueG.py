import subprocess

resultado = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

resultadoSeparado = resultado.stdout.split(" ")

print(resultadoSeparado[1])