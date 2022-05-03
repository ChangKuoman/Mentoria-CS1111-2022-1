
### EJERICIO DE PC ###

"""
(Nivel 1) Desarrolle un algoritmo que convierta la ultima letra de cada palabra de un
string a mayuscula. El resto de letras deben ser minusculas. Asuma que unicamente
habra un espacio entre palabra y palabra
Algunos ejemplos de dialogo de este programa serian:
Input : Estudie sacare veinte
Output : estudiE sacarE veintE
Input : GueRRa aviSADa NO mata genTE
Output : guerrA avisadA nO matA gentE
"""

cadena = str(input("ingrese string: "))
cadena2 = ""
for palabra in cadena.split():

    for indice in range(len(palabra)):
        if indice == len(palabra)-1:
            cadena2 += palabra[indice].upper()
        else:
            cadena2 += palabra[indice].lower()
    cadena2 += " "

print(cadena2)
