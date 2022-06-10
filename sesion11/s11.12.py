
### EJERCICIO ###

lista = []
for i in range(50):
    if i % 2 == 0:
        lista.append(i)

l1 = [i for i in range(50) if i%2==0]
print(l1)

l2 = [i if i%2==0 else "." for i in range(10)]
print(l2)

l3 = [i**j for i in range(10) for j in range(5)]
print(l3)

d1 = {i:i for i in range(10)}
print(d1)
