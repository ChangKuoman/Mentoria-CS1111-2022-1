
### EJERCICIO ###

# Crear un quiosco que tenga las siguientes opciones:
#
# Quiosco Pan con Palta
#
# Elija una opción
# 1. Ingresar un nuevo producto
# 2. Averiguar el costo de un producto
# 3. Imprimir todos los productos con su precio
# 4. Salir
#
# y en el diccionario de productos cuente al principio:
#
# productos = {'Pan':1.5, 'Palta':5}

menu = """
1. Ingresar un nuevo producto
2. Averiguar el costo de un producto
3. Imprimir todos los productos con su precio
4. Salir
"""
productos = {'Pan':1.5, 'Palta':5}

def imprimir_productos():
    for i in productos.keys():
        print(f"Nombre: {i}, Precio: {productos[i]}")

def averiguar_costo():
    producto = str(input("Ingrese el nombre del producto: "))
    print("El precio del producto es", productos[producto])

def ingresar_producto():
    producto = str(input("Ingrese el nombre del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    productos[producto] = precio

while True:
    print(menu)
    opcion = int(input("Ingrese la opción: "))
    if opcion == 1:
        ingresar_producto()
    elif opcion == 2:
        averiguar_costo()
    elif opcion == 3:
        imprimir_productos()
    elif opcion == 4:
        break
