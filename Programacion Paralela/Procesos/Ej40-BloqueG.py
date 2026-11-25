import subprocess

try:
    creaciondeCarpeta = subprocess.run(
        ["cmd", "/c", "mkdir", "D:\\Salesianos Alcala\\2026-2027\\LENGUAJES\\PYTHON\\prueba_psp"],
        capture_output=True,
        check=True,
        text=True
    )

    print(creaciondeCarpeta.stdout)
except subprocess.CalledProcessError as e:
    print(f"Fallo con codigo: {e.returncode}")