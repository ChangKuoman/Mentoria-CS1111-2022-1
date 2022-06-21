
### EJERCICIO DE PC ###

# archivos
"""
2021-2 2.02
4. (5 points) Evalúa archivos .
Crear un programa que lea un archivo y que permita contar el n´umero de ocurrencias de
todas las vocales dentro del archivo considerando todas las vocales en min´uscula y debera
generar un nuevo archivo que denominara resumen.txt, donde cada linea contendra
la vocal y las ocurrencias dentro del archivo original.
origen.txt
”Quicksort (sometimes called partition-exchange sort) is an efficient sorting algorithm.
Developed by British computer scientist Tony Hoare in 1959[1] and published in 1961,[2]
it is still a commonly used algorithm for sorting. When implemented well, it can be about
two or three times faster than its main competitors, merge sort and heapsort.”

Input : origen . txt
Output : resumen . txt
a 16
e 29
i 27
o 22
u 5
"""
a = 0
e = 0
i = 0
o = 0
u = 0

# file = open('input.txt', 'r')
with open('input.txt', 'r') as file:
    for linea in file:
        for letra in linea:
            if letra == 'a': a += 1
            if letra == 'e': e += 1
            if letra == 'i': i += 1
            if letra == 'o': o += 1
            if letra == 'u': u += 1
    print()
print()

with open('resumen.txt', 'w') as archivo:
    archivo.write(f'a {a}\n')
    archivo.write(f'e {e}\n')
    archivo.write(f'i {i}\n')
    archivo.write(f'o {o}\n')
    archivo.write(f'u {u}\n')
