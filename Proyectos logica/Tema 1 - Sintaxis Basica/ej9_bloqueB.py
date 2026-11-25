procesos = [
    {"nombre": "python.exe", "pid": 4212, "memoria": 85},
    {"nombre": "chrome.exe", "pid": 1080, "memoria": 640},
    {"nombre": "code.exe", "pid": 5600, "memoria": 58},
    {"nombre": "python.exe", "pid": 6666, "memoria": 43},
    {"nombre": "chrome.exe", "pid": 8787, "memoria": 1040},
]

while True:
    try:
        opcion = int(input("> "))

        if opcion == 1:
            for proc in procesos:
                nombre = proc["nombre"]
                pid = proc["pid"]
                memoria = proc["memoria"]
                print(f"Nombre: {nombre} [{pid}] · {memoria} MB")

        elif opcion == 2:
            proceso_pid = int(input("Dime el pid del proceso: "))
            encontrado = False
            for proc in procesos:
                nombre = proc["nombre"]
                pid = proc["pid"]
                memoria = proc["memoria"]
                if pid == proceso_pid:
                    print(f"Nombre: {nombre} [{pid}] · {memoria} MB")
                    encontrado = True
            if not encontrado:
                print(f"El proceso con pid {proceso_pid} no existe")

        elif opcion == 3:
            proceso_eliminar = int(input("Cual es el pid del proceso que quieres eliminar: "))
            for proc in procesos:
                if proc["pid"] == proceso_eliminar:
                    procesos.remove(proc)
                    print(f"Proceso con PID {proceso_eliminar} eliminado correctamente.")
                    break
            else:
                print("No se encontró ningún proceso con ese PID.")

        elif opcion == 4:
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida")

    except ValueError:
        print("La opcion no es un numero")

    
