
# numeros primos del 2 al n

n = int(input("Ingrese n: "))

# 18 / 2 = 9
# 18 % 2 == 0

for num in range(2, n):
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        print(num)
