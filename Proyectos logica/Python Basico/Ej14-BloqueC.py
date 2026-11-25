peticion = ""
numero = 0

while True:
    peticion = input("Dime un numero o escribe fin para finalizar: ")

    if peticion == "fin":
        print("Saliendo...")
        break
    else:
        try:
            numero += int(peticion)
        except ValueError:
            print(f"Escribe un numero")

print(f"La suma total equivale a: {numero}")