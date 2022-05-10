
### EJERCICIO ###

"""
2021-2 UPCH E3
1. [5 puntos] Dado un mensaje, se debe calcular su costo para enviarlo por telégrafo. Para esto se
sabe que cada letra minúscula cuesta $8.5, cada letra mayúscula cuesta $13, los caracteres
especiales que no sean letras cuestan $20 (considerar ñ, á, é, í, ó, ú, ü como tales) y los dígitos
tienen un valor de $18 cada uno. Los espacios no tienen valor.
Ejemplo:
Mensaje: Feliz Aniversario!
Su mensaje cuesta $165
"""

mensaje = str(input("Ingrese mensaje: "))
precio = 0
for letra in mensaje:
    if letra.islower():
        precio += 8.5
    elif letra.isupper():
        precio += 13
    elif letra.isdigit():
        precio += 18
    elif letra == ' ':
        precio += 0
    else:
        precio += 20

print("Su mensaje cuesta $%f" % precio)
print(f"Su mensaje cuesta ${precio}")
