procesos = [
    {"nombre": "python.exe", "pid": 4212, "cpu": 12.5},
    {"nombre": "chrome.exe", "pid": 1080, "cpu": 22},
    {"nombre": "code.exe", "pid": 7777, "cpu": 22.7}
]

procesos_vacia = []

for i in procesos:
    if (i["cpu"] > 10):
        procesos_vacia.append(i)

procesos_ordenados = sorted(procesos_vacia, key= lambda p: p["cpu"], reverse= True)

for i in procesos_ordenados:
    print(f"{i["nombre"]} ({i["pid"]}) {i["cpu"]}")