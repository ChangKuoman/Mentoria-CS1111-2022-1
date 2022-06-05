
# enunciado: funciones_1.JPG

def f(x):
    return 3 * x + 5

def g(x):
    return x ** 2

x = int(input("Ingrese x: "))

print("f(g(x)) =", f(g(x)))
