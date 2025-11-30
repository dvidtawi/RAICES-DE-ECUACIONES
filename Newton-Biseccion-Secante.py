import math


# ===========================================
# MÉTODOS NUMÉRICOS
# ===========================================

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or abs(b - a) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c


def secante(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            return None

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        if abs(x2 - x1) < tol:
            return x2

        x0, x1 = x1, x2

    return x2


def newton(f, df, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        if df(x0) == 0:
            return None

        x1 = x0 - f(x0) / df(x0)

        if abs(x1 - x0) < tol:
            return x1

        x0 = x1

    return x1


# ===========================================
# EJERCICIOS
# ===========================================

# Ejercicio 1: x^3 − e^(0.8x) = 20
f1 = lambda x: x ** 3 - math.exp(0.8 * x) - 20
df1 = lambda x: 3 * x ** 2 - 0.8 * math.exp(0.8 * x)

# Ejercicio 2: 3 sin(0.5x) − 0.5x + 2 = 0
f2 = lambda x: 3 * math.sin(0.5 * x) - 0.5 * x + 2
df2 = lambda x: 3 * 0.5 * math.cos(0.5 * x) - 0.5

# Ejercicio 3: x^3 − x^2 e^(-0.5x) − 3x = −1
f3 = lambda x: x ** 3 - x ** 2 * math.exp(-0.5 * x) - 3 * x + 1
df3 = lambda x: (3 * x ** 2
                 - 2 * x * math.exp(-0.5 * x)
                 + 0.5 * x ** 2 * math.exp(-0.5 * x)
                 - 3)

# Ejercicio 4: cos^2(x) − 0.5 x e^(0.3x) + 5 = 0
f4 = lambda x: math.cos(x) ** 2 - 0.5 * x * math.exp(0.3 * x) + 5
df4 = lambda x: -2 * math.cos(x) * math.sin(x) - 0.5 * (math.exp(0.3 * x) + 0.3 * x * math.exp(0.3 * x))

# ===========================================
# SOLUCIONES
# ===========================================

print("\n======== EJERCICIO 1 ========")
print("Bisección:", biseccion(f1, 0, 8))
print("Secante:", secante(f1, 0, 8))
print("Newton:", newton(f1, df1, 1))

print("\n======== EJERCICIO 2 ========")
print("Bisección:", biseccion(f2, -10, 10))
print("Secante:", secante(f2, -10, 10))
print("Newton:", newton(f2, df2, 1))

print("\n======== EJERCICIO 3 ========")
print("Bisección raíz 1:", biseccion(f3, -5, 0))
print("Bisección raíz 2:", biseccion(f3, 0, 2))
print("Bisección raíz 3:", biseccion(f3, 2, 10))
print("Secante (cerca 0):", secante(f3, 0, 2))
print("Newton (inicio=1):", newton(f3, df3, 1))

print("\n======== EJERCICIO 4 ========")
print("Bisección:", biseccion(f4, 0, 10))
print("Secante:", secante(f4, 0, 10))
print("Newton:", newton(f4, df4, 1))

