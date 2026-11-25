import subprocess
try:
    resultado = subprocess.run(
        ["python", "--version"],
        capture_output=True,
        text=True,
        check=True
    )

    print(resultado.stdout)

except subprocess.CalledProcessError as e:
    print(f"Fallo con codigo: {e.returncode}")