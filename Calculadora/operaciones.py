def suma(a,b):
    return a + b
def resta(c,d):
    return c - d
def producto(e,f):
    return e * f
def division(g,h):
    return g / h
def potencia(base, exponente):
    return base ** exponente
def modulo(dividendo, divisor):
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    return dividendo % divisor