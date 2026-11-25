procesos = [
    {"nombre": "python.exe", "pid": 4212, "memoria": 85},
    {"nombre": "chrome.exe", "pid": 1080, "memoria": 640},
    {"nombre": "code.exe", "pid": 5600, "memoria": 58},
    {"nombre": "python.exe", "pid": 6666, "memoria": 43},
    {"nombre": "chrome.exe", "pid": 8787, "memoria": 1040},
]

dic_pids = {}
dic_memoria = {}

for proc in procesos:
    nombre = proc["nombre"]
    pid = proc["pid"]
    memoria = proc["memoria"]

    if nombre in dic_pids:
        dic_pids[nombre].append(pid)
        dic_memoria[nombre] += memoria
    else:
        dic_pids[nombre] = [pid]
        dic_memoria[nombre] = memoria

print("Programa con mas de un proceso")
for nombre, lista_pid in dic_pids.items():
    if len(lista_pid) > 1:
        memoria_total = dic_memoria[nombre]
        print(f"- {nombre}: PIDs {lista_pid} | Memoria total: {memoria_total} MB")