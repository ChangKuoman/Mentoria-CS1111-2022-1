
# manejo de errores

while True:
    try:
        n = int(input("n: "))
        m = int(input("m: "))
        break
    except:
        pass

try:
    print(n/m)
except:
    pass
