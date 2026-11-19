# f : fonction à intégrer
# a, b : bornes du segment d'intégration
# n : nombre de subdivisions du segment [a, b]

def rectangles_gauche(f, a, b, n):
    h = (b - a) / n
    t = a
    integrale = 0
    for i in range(n):
        integrale = integrale + f(t) * h
        t = t + h
    return integrale

def rectangles_droite(f, a, b, n):
    h = (b - a) / n
    t = a
    integrale = 0
    for i in range(n):
        t = t + h
        integrale = integrale + f(t) * h
    return integrale

def trapezes(f, a, b, n):
    h = (b - a) / n
    t = a
    integrale = 0
    for i in range(n):
        integrale = integrale + (f(t) + f(t + h)) / 2 * h
        t = t + h
    return integrale

def point_milieu(f, a, b, n):
    h = (b - a) / n
    t = a + h / 2
    integrale = 0
    for i in range(n):
        integrale = integrale + f(t) * h
        t = t + h
    return integrale

def simpson(f, a, b, n):
    h = (b - a) / n
    t = a
    integrale = 0
    for i in range(n):
        integrale = integrale + (f(t) + 4 * f(t + h / 2) + f(t + h)) / 6 * h
        t = t + h
    return integrale