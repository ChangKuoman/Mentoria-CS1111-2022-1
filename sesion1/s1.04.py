
### EJERCICIO ###

# Pedir al usuario que ingrese una cantidad de <segundos> y el programa
# convierta esa cantidad de segundos a horas, minutos y segundos

cantidad_segundos = int(input("Ingrese segundos: "))

minutos = cantidad_segundos // 60
segundos = cantidad_segundos % 60

horas = minutos // 60
minutos = minutos % 60

# horas:minutos:segundos

print(f"{cantidad_segundos} segundos son {horas} horas, {minutos} minutos y {segundos} segundos.")
