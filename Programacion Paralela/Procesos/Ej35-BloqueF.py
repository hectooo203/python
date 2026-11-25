from multiprocessing import Pool

def cubo(n):
    return n**3

if __name__ == "__main__":
    with Pool(8) as p:
        resultado = p.map(cubo, [1,2,3,4,5,6,7,8])
    print(resultado)