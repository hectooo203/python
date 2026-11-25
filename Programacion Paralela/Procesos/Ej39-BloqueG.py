import subprocess
try:
    pingear = subprocess.run(
        ["ping", "8.8.5.2"],
        capture_output=True,
        text=True,
        check=True,
        timeout=5
    )

    print(pingear.stdout)
except subprocess.TimeoutExpired:
    print("Tardo demasiado")
except subprocess.CalledProcessError as e:
    print(f"Error con codigo: {e.returncode}")