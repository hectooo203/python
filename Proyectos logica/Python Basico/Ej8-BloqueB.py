productos = {
    "Manzana": 1.55,
    "Leche": 3.4, 
    "Avena": 10.99,
    "Azucar": 6.8
}
peticion = input("Dime el producto que quieres visualizar: ")
print(f"Producto: {peticion}. Precio: {productos.get(peticion) if peticion in productos else "No existe"}")