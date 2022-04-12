
### EJERCICIO ###

"""
Tai Loy, ha decidido empaquetar en sus bodegas colores, en cajas de 6, 12 y 24 unidades. De tal
manera que reducirá sus costos al ser ellos mismos quienes realicen el empaque de colores.

Se  pide  realizar  un  programa  que  capture  como  dato  de  entrada  un  número  entero  que
representaría la cantidad de colores a ser empaquetados y el programa halle el menor número
de cajas de colores de 24, 12 , 6 e indicar el número de colores sobrantes.
"""

# n
# -> cajas de 24
# 100 // 24 -> 4
# 100 % 24 -> 4
# 4 // 12 -> 0
# 4 % 12 -> 4
# 4 // 6 -> 0
# 4 % 6 -> 4
# nos sobra 4 lapices

lapices = int(input("Ingrese cantidad lapices: "))

cajas24 = lapices // 24
lapices = lapices % 24

cajas12 = lapices // 12
lapices = lapices % 12

cajas6 = lapices // 6
lapices = lapices % 6

print(f"""
Cajas de 24: {cajas24}
Cajas de 12: {cajas12}
Cajas de 6: {cajas6}
Restantes: {lapices}
""")
print("Cajas de 24:", cajas24)
