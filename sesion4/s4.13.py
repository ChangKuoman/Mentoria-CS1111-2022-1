
### EJERCICIO ###

"""
Una veterinaria le ha solicitado crear un programa para calcular la edad apr ́oximada
humana de sus pacientes caninos. El programa que usted realizar ́a solicita un n ́umero
N que indica cu ́antos pacientes se atender ́an. A continuaci ́on solicita la edad canina y
el nombre de cada paciente. Por cada lectura, usted imprime el nombre y la edad real
aproximada humana:
Considere que la edad real aproximada se calcula con los siguientes criterios.
•Los 2 primeros a ̃nos se consideran como 10.5 a ̃nos humanos cada uno.
•Cada a ̃no adicional se considera como 4 a ̃nos humanos.
•Solo se considera edades en n ́umeros enteros mayor o igual a 1. Se solicita que este
dato sea validado por su progra. Es decir si no ingresa un valor mayor o igual a 1,
debe volver a solicitar el dato.
•El texto de salida debe combinar el nombre y la edad equivalente, tal como se ver ́a
en los ejemplos de entra y salida de su programa.
"""

n_canes = int(input("Ingrese cantidad de caninos: "))

for _ in range(n_canes):
    # pidiendo datos
    nombre = str(input("Ingrese nombre: "))
    edad_canina = int(input("Ingrese edad canina: "))
    while edad_canina <= 0:
        edad_canina = int(input("Ingrese edad canina: "))

    # analizando
    edad_humana = 0
    for i in range(1, edad_canina+1):
        if i == 1 or i == 2:
            edad_humana += 10.5
        else:
            edad_humana += 4
    # 1 -> 10.5
    # 2 -> 10.5 + 10.5
    # 4 -> 10.5 + 10.5 + 4 + 4

    # imprimiendo
    print(f"La edad humana de {nombre} es {edad_humana}. ;)")
