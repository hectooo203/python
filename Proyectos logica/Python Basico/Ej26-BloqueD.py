def generar_numeros(n):
    for i in n:
        if i%2==0:
            yield i


for n in generar_numeros(range(1,8000)):
    print(n)
