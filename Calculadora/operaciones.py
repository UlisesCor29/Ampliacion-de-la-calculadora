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
def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return numero ** 0.5
def porcentaje(porcentaje, cantidad):
    return (porcentaje / 100) * cantidad
def valor_absoluto(numero):
    return abs(numero)
def factorial(numero):
    if not isinstance(numero, int) or isinstance(numero, bool) or numero < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if numero == 0:
        return 1
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
def promedio(*numeros):
    if len(numeros) == 0:
        raise ValueError("Debe ingresar al menos un número.")
    return sum(numeros) / len(numeros)