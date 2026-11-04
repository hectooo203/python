# ==========================================
# GESTOR DE SISTEMA Y SERVIDORES (CLI)
# Autor: (Hector Martinez / hectooo203)
# ==========================================

# --- PROCESOS DEL SISTEMA Y PUERTOS DE SERVIDORES ---

procesos = [
    {"nombre": "python.exe", "pid": 4212, "memoria": 85},
    {"nombre": "chrome.exe", "pid": 1080, "memoria": 640},
    {"nombre": "code.exe", "pid": 5600, "memoria": 58},
    {"nombre": "python.exe", "pid": 6666, "memoria": 43},
    {"nombre": "chrome.exe", "pid": 8787, "memoria": 1040},
    {"nombre": "notepad.exe", "pid": 9120, "memoria": 15},
]

srv_a = {22, 80, 443, 3306, 8080}

srv_b = {22, 443, 5432, 8080, 9000}

# --- LISTA DE OPCIONES ---

opciones = """
    ============================================
                    OPCIONES 
    ============================================

    [1] Ver todos los procesos de la lista
    [2] Ver el consumo de memoria por programa
    [3] Analizar los puertos de los servidores
    [4] Eliminar procesos de la lista por PID
    [0] Salir del programa 
"""
# --- FUNCIONES ---

def ListarOpciones(lista_procesos):

    # Imprime cabeceras de la tabla (Utiliza < y > para alinear a la izquierda o derecha junto con los espacios de tabulacion)
    print(f"{'#':<3} {'PID':<6} {'NOMBRE':<12} {'MEM':>5}")

    # Coge los valores segun clave de la lista de tuplas y lo imprime formando una lista y cuadrando con las cabeceras
    for i, proc in enumerate(lista_procesos):

        # Asigna el valor de cada clave de la lista a una variable para poder trabajar con ella
        nombre = proc["nombre"]
        pid = proc["pid"]
        memoria = proc["memoria"]

        # Imprime el resultado
        print(f"{i+1:<3} {pid:<6} {nombre:<12} {memoria:>5} MB")

def AgruparProcesos(lista_procesos):
    # Creacion de diccionarios para agrupar pids y memoria segun nombre
    nombre_proceso = {}
    memoria_total = {}

    # Imprimir cabeceras como en la anterior funcion
    print(f"{'PID':<12} {'NOMBRE':<12} {'MEM':>5}")                

    # Bucle para asignar los pids a los diccionarios e ir agregando memoria en caso de que sea nombre repetido
    for proc in lista_procesos:
        nombre = proc["nombre"]
        pid = proc["pid"]
        memoria = proc["memoria"]

        # Comparar si el nombre existe ya en el diccionario (agregar PID y memoria a sus diccionarios)
        # sino existe crear una entrada nueva en los diccionarios
        if nombre in nombre_proceso:
            nombre_proceso[nombre].append(pid)
            memoria_total[nombre] += memoria
        else:
            nombre_proceso[nombre] = [pid]
            memoria_total[nombre] = memoria

    # Bucle para mostrar los diccionarios
    for nombre, lista_pid in nombre_proceso.items():
        pid = ", ".join(str(pid) for pid in lista_pid)
        print(f"{pid:<12} {nombre:<12} {memoria_total[nombre]:>5}")

def AnalizarPuertos(srv_a, srv_b):

    # Comparadores de casos para puertos (saber que puerto esta en que servidor, diferencia, totales y saber si hay algo dentro de un diccionario)
    print(f"Puertos abiertos en ambos servidores: {srv_a & srv_b}")
    print(f"Puertos que solo tiene el servidor a: {srv_a - srv_b}")
    print(f"Puertos totales: {srv_a | srv_b}")
    print(f"Puerto 3306 abierto?: Servidor A: {3306 in srv_a} Servidor B: {3306 in srv_b}")

def EliminarProceso(lista_procesos):

    # Inicializacion de las variables
    pid = 0
    seguir_Intentando = True

    # Bucle while para iterar siempre que la condicion se cumpla
    while seguir_Intentando:

        # Peticion del PID por pantalla
        print("Dime el PID del proceso que deseas eliminar: ")
        pid = int(input("> "))

        # Muestreo de informacion de lso procesos a eliminar
        print("--- Procesos que se van a eliminar ---")
        print(f"{'PID':<12} {'NOMBRE':<12} {'MEM':>5}")

        # Bucle que itera sobre la lista en busca del proceso pedido
        for proc in lista_procesos:

            # Si encuentra el proceso lo muestra y pide confirmacion al usuario para eliminarlo
            if pid == proc["pid"]:
                print(f"{proc["pid"]:<12} {proc["nombre"]:<12} {proc["memoria"]:>5}")
                print("Desea eliminar el proceso? [s/n]")
                confirmacion = str(input("> "))
                if confirmacion == "s" or confirmacion == "S":

                    # Si el usuario confirma el proceso se elimina
                    lista_procesos.remove(proc)
                    print("Proceso eliminado con exito")

                    # Confirmacion para introdir otro PID o salida de la opcion
                    print("Desea seleccionar otro proceso? [s/n]")
                    confirmacion_seguirIntentando = str(input("> "))
                    if confirmacion_seguirIntentando == "n" or confirmacion_seguirIntentando == "N":
                        seguir_Intentando = False
                        break
                    else:
                        seguir_Intentando = True
                        break
                else:
                    print("Cancelando Operacion...")
                    break
        else:

            # Manejo de errores en caso de que no encuentre el PID y confirmacon por si el usuario quiere introducir otro diferente
            print(f"El pid {pid} no se encuentra en la lista de procesos")
            print("Desea seleccionar otro? [s/n]")
            confirmacion_pid = input("> ")
            if confirmacion_pid == "n" or confirmacion_pid == "N":
                break

                # Seguir por aqui, hay que mostrar los procesos a eliminar, pedir confirmacion, eliminar procesos, mostrar confirmacion de borrado y manejo de errores.

# --- MENU DE INTERACCION ---

while True:
    try:
        print(opciones)
        opcion = int(input("> "))

        if opcion == 1:
            ListarOpciones(procesos)

        elif opcion == 2:
            AgruparProcesos(procesos)

        elif opcion == 3:
            AnalizarPuertos(srv_a, srv_b)

        elif opcion == 4:
            EliminarProceso(procesos)

        elif opcion == 0:
            break

        else:
            print("Opcion no valida")

    except ValueError:
        print("No se ha seleccionado una opcion valida")

    