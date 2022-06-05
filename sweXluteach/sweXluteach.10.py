
# n = 3
#   0 1 2
# 0 1
# 1 0 1
# 2 1 0 1

n = int(input("Ingrese n: "))

for i in range(n):
    for j in range(i+1):
        if i % 2 == j % 2:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
