
# strings

variable = str(input("ingrese algo: ")).upper()

print(variable[0] == "A")

caracteres -> ascii
cadena = "hOLA"
if ord(cadena[0]) in range(65, 91):
    print("Esta en mayuscula")
else:
    print("no esta en mayuscula")

# ord -> caracter a numero
# chr -> numero a caracter

print(chr(65))

cadena = "hola"
cadena = cadena.upper()
print(cadena)
