def DatosPersona(**kwargs):
    for i in kwargs.items():
        print(i)

DatosPersona(nombre = "Manuel", edad = 30, profesion = "fontanero", ciudad = "Alcala de Henares")