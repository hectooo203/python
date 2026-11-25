numero1, numero2 = 0.0, 0.0

try:
    numero1 = float(input("Dime el dividendo: "))
    numero2 = float(input("Dime el divisor: "))
    resultado = numero1 / numero2
    print(f"Resultado: {resultado}")
except ValueError:
    print("No has escrito un numero")
except ArithmeticError:
    print("No se puede dividir por 0")
finally:
    print("Operacion terminada...s")