
# strings

letra = "A"
digito = "0"

variable = letra + digito
print(variable)

cadena = "11156 00 2455 555 48"

espacios = 0
for digito in cadena:
    if digito == " ":
        espacios += 1
print(espacios)

print(cadena.count(' '))

for i in range(len(cadena)):
    if cadena[i] == '0':
        print(i)
        break

print(cadena.find('0'))

var = str(input("ingrese (x, y): "))

while var != "x" and var != "y":
    var = str(input("ingrese (x, y): "))
