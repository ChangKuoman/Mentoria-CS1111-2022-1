
### EJERCICIO DE PC ###

# archivos
"""
2021-2 1.04
4. (5 points) Evalúa archivos.
Del archivo poema.txt:
Caminemos en la era de la modernidad
Observando lo que ella nos puede dar
Manejar una computadora por empezar
Pulsando el ratón y el teclado virtual
Una manzanita y varios niños te guiarán
También una computadora sensacional
Así paso a paso vamos a aprender
En la era de la modernidad
Desarrollar un programa en python que realice lo siguiente:
* Abra el archivo poema.txt en modo lectura.
* Crea el archivo palabras.txt en modo escritura.
* Analice cada palabra de poema.txt y si la palabra tiene igual o más de 6 caracteres,
guarde esa palabra en el archivo palabras.txt evitando que esas palabras esten
repetidas.
* Cierre los archivos abiertos.

# palabras .txt
Caminemos
modernidad
Observando
Manejar
computadora
empezar
Pulsando
teclado
virtual
manzanita
guiaran
Tambien
sensacional
aprender
"""

poema = open('poema.txt', 'r')

lista = []
for linea in poema:
    for palabra in linea.rstrip().split():
        if len(palabra) >= 6 and palabra not in lista:
            lista.append(palabra)

poema.close()

palabras = open('palabras.txt', 'w')

for palabra in lista:
    palabras.write(palabra)
    palabras.write('\n')

palabras.close()
