import random

# archivos

numeros = {
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve",
    "0": "cero"
}

n = int(input("NUM: "))
while n <= 0:
    n = int(input("NUM: "))

archivo = open("numeros.txt", "w")

for i in range(n):
    numero_azar = random.randint(100, 999) # int
    numero_azar = str(numero_azar)
    archivo.write(numero_azar)
    archivo.write(" ")
    # 789
    # 7
    primer_digito = numero_azar[0]
    # numeros["7"] -> siete
    archivo.write(numeros[primer_digito])
    archivo.write(" ")
    archivo.write(numeros[numero_azar[1]])
    archivo.write(" ")
    archivo.write(numeros[numero_azar[2]])
    archivo.write("\n")

archivo.close()

print("Se generó el archivo numeros.txt")
