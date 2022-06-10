
### EJERCICIO ###

# Escribir un programa que pida un numero (1-7) y muestre el dia de la semana

dias = {
    1: "lunes",
    2: "martes",
    3: "miercoles",
    4: "jueves",
    5: "viernes",
    6: "sabado",
    7: "domingo"
}

dia = int(input("Dia en numeros (1-7): "))

print("El dia de la semana es", dias[dia])
