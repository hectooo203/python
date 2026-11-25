try:
    
    puerto = int(input("Dime el puerto: "))
    
    if 1 < puerto > 65535:
        print ("Puerto valido...")
    elif 1 < puerto < 1023:
        print (f"El puerto: {puerto} es bien conocido")
    elif 1024 < puerto < 49151:
        print (f"El puerto: {puerto} es registrado")
    elif 49152 < puerto < 65535:
        print (f"El puerto: {puerto} es dinamico")
    else:
        print ("Puerto invalido...")
    
except ValueError:
    print("Introduce un numero")

