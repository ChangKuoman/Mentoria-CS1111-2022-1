
### EJERCICIO 2.1.a ###

### manera 1

s = 0
for i in range(1, 21, 2):
    # posi
    s += i**2

for i in range(2, 21, 2):
    # nega
    s -= i ** 2
print(s)

### manera 2

s = 0
for i in range(1, 21):
    if i%2 == 0:
        s -= i**2
    else:
        s += i**2
print(s)

### manera 3

suma = 0
signo = 1
for i in range(1, 21):
    suma += (i**2) * signo
    signo *= -1
print(suma)
