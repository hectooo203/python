grados = [20, 30, 11, 3, -2, 8, 40, 33, 22]

Farenheith = list(map(lambda x: (x * 1.8) + 32, grados)) 

filtrarFarenheith = list(filter(lambda x: x>80, Farenheith))

print(f"Grados mayores a 80ºF: {filtrarFarenheith}")