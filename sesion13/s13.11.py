
### INTRODUCCION ###

# complejidad algorítmica
n = int(input("ingrese n: "))
suma = 0
for i in range(1, n+1):
    suma += i
print(suma)

suma = n * (n + 1) / 2
print(suma)

# O(1) < O(logn) < O(n) < O(n^2)

for i in range(n):
    for j in range(n):
        # n^2
        pass
