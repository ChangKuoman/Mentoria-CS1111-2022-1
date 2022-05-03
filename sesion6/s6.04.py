
### INTRODUCCION ###

# strings
cadena = str(input("Ingrese cadena: "))

print(len(cadena))

cadena = cadena.upper()
print(cadena)

cadena = cadena.capitalize()
print(cadena)

cadena = cadena.title()
print(cadena)

cadena = cadena.lower()
print(cadena)

print(cadena.islower())
print(cadena.isupper())

print("digitos", cadena.isdigit())

cadena = cadena.replace("o", "i")
print("reeplazo", cadena)

# cadena = cadena.upper()
print("a", cadena.count("a"))
