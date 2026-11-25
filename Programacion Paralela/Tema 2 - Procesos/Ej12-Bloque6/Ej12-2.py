import subprocess
import time

descarga1 = {"nombre":"Archivo MP3 (Descarga)",
             "comando":["python", "-c", "import time; time.sleep(2)"]}
descarga2 = {"nombre":"Archivo PDF (Descarga)",
             "comando":["python", "-c", "import time; time.sleep(1)"]}
descarga3 = {"nombre":"Archivo ZIP (Descarga Maliciosa)",
             "comando":["python", "-c", "import sys; sys.exit(3)"]}
descarga4 = {"nombre":"Pelicula completa (Descarga)",
             "comando":["python", "hijo_lento.py"]}

descargasEnEjecucion = []
descargasPendientes = [descarga1, descarga2, descarga3, descarga4]
mensajeInforme = ""
totalDescargas = len(descargasPendientes)
descargasCompeltadas = 0

inicio_gestor = time.time()
while len(descargasEnEjecucion) > 0 or len(descargasPendientes) > 0:
    while len(descargasEnEjecucion) < 2 and len(descargasPendientes) > 0:
        tareaActual = descargasPendientes[0]
        tareaActual["proceso"] = subprocess.Popen(tareaActual["comando"])
        tareaActual["inicio"] = time.time()
        descargasEnEjecucion.append(tareaActual)
        descargasPendientes.pop(0)
        t_transcurrido = time.time() - inicio_gestor
        print(f"[{t_transcurrido:.2f}s] Iniciando: {tareaActual["nombre"]}")
        
    for tareas in descargasEnEjecucion[:]:
        procesamientoActual = time.time() - tareas["inicio"]
        if tareas["proceso"].poll() is None:
            if procesamientoActual >= 3:
                tareas["proceso"].terminate()
        else:
            tareas["proceso"].wait()
            codigoSalida = tareas["proceso"].returncode
            estado = "Descarga Completada" if tareas["proceso"].returncode == 0 else "Error en la descarga"
            duracionTotal = time.time() - tareas["inicio"]
            if procesamientoActual >= 3:
                estado = "Descarga demasiado grande"
            mensajeInforme += f"Archivo: {tareas["nombre"]}. Estado de descarga: {estado}. Codigo de salida: {codigoSalida}. Duracion: {duracionTotal} \n"
            descargasEnEjecucion.remove(tareas)
            if estado == "Descarga Completada":
                descargasCompeltadas += 1
            t_transcurrido = time.time() - inicio_gestor
            print(f"[{t_transcurrido:.2f}s] Terminada: {tareas["nombre"]}")
    time.sleep(0.1)
print("--- INFORME COMPLETO ---")
print(mensajeInforme)
print(f"Descargas correctas: {descargasCompeltadas}/{totalDescargas}")
