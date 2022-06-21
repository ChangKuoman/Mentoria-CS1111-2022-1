
### EJERCICIO DE PC ###

# archivos
"""
2021-2 1.02
4. (5 points) Evalúa archivos.
Crea una función que reciba el nombre de un archivo llamado in.txt y cree un archivo
out.txt sin saltos de líneas (\n).
Algunos ejemplos de diálogo de este programa serían:

in.txt
Anda , alegrame el dia .
Muy bien , Sr. DeMille , estoy lista para mi primer plano .
Que la Fuerza te acompane .
Ajusten sus cinturones . Va a ser una noche movida .

out.txt
Anda , alegrame el dia .Muy bien , Sr. DeMille , estoy lista para mi primer plano . Que la Fuerza te acompane . Ajusten sus cinturones . Va a ser una noche movida .
"""

entrada = open('in.txt', 'r')
salida = open('out.txt', 'w')

for linea in entrada:
    linea = linea.rstrip()
    salida.write(linea)

entrada.close()
salida.close()
