import subprocess

proceso = subprocess.run(
    ["python", "-c", "import sys; sys.exit(2)"],
    capture_output=True,
    text=True,
    check=True
)

salida = proceso.returncode

print(f"Codigo devuelto: {"OK" if salida == 0 else "ERROR"} {subprocess.CalledProcessError}")