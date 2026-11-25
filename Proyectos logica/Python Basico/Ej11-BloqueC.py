nota = float(input("Dime la nota del alumno: "))

if nota <= 10.0 and nota >= 8.0:
    print("Sobresaliente")
elif nota >= 6.0 and nota < 8.0:
    print("Notable")
elif nota >= 5.0 and nota < 6.0:
    print("Aprobado")
elif nota < 5.0:
    print("Suspenso")
else:
    print("Nota no valida")