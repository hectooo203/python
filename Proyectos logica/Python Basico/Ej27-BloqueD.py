from functools import wraps
import time

def tiempoEjecucion(funcion):
    @wraps(funcion)
    def muestraTiempo(*args,**kwargs):
        horadeEjecucion = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        horaFinal = time.perf_counter()
        horaCalculoTotal = horaFinal - horadeEjecucion
        print(f"Tiempo total de ejecucion: {round(horaCalculoTotal,4)} segundos")
        return resultado
    return muestraTiempo

@tiempoEjecucion
def calculomasivo(list_a, list_b):
    resultado1 = 0
    resultado2 = 0
    for i in range(1,80000):
        resultado1 += list_a * i
    for i in range(1,80000):
        resultado2 += list_b * i
    return resultado1*resultado2

print(calculomasivo(5,7))