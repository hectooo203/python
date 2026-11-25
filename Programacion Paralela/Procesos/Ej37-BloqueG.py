import subprocess

resultado = subprocess.run(
    ["python", "--ersion"],
    capture_output=True,
    text=True
)

print(resultado.stderr)
print(resultado.returncode)