
### EJERCICIO DE PC ###

# h
# ho
# hol
# hola
# hol
# ho
# h

palabra = str(input("Palabra: "))

for i in range(1, len(palabra)+1):
    print(palabra[0:i])

for i in range(len(palabra)-1, 0, -1):
    print(palabra[0:i])
