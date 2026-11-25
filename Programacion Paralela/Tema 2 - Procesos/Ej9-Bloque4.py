import time
import os
from multiprocessing import Pool

def cuadrado_con_pid(numero):
    time.sleep(0.5)
    cuadrado = numero * numero
    pid = os.getpid()
    lista = (numero, cuadrado, pid)
    mensaje = [numero, cuadrado, pid]
    return mensaje

if __name__ == "__main__":
    pidpadre = os.getpid()
    pids = []
    comienzoEjecucion = time.time()
    with Pool(4) as p:
        listacompleta = p.map(cuadrado_con_pid, [1, 2, 3, 4, 5, 6, 7, 8])
        for i in listacompleta:
            print(f"El numero es: {i[0]}. Su cuadrado es: {i[1]}. Y el pid es: {i[2]}")
            if i[2] in pids:
                continue
            else:
                pids.append(i[2])
    finalEjecucion = time.time()
    Totalejecucion = finalEjecucion - comienzoEjecucion
    siexiste = False
    for i in pids:
        if i == pidpadre:
            siexiste = True
    print(f"Cantidad de procesos distintos: {len(pids)}. El proceso a tardado: {Totalejecucion} segudos. El proceso padre {f"si existe y es {pidpadre}" if siexiste == True else "no existe"} dentro de los hijos")