from operaciones import suma, resta, producto, division
from operaciones import potencia, modulo, raiz_cuadrada
from operaciones import porcentaje, valor_absoluto
from operaciones import factorial, promedio, redondear


# Solicita un número entero o decimal.
def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingrese un número.")


# Solicita únicamente un número entero.
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")


while True:
    print("\n===== CALCULADORA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Módulo")
    print("7. Raíz cuadrada")
    print("8. Porcentaje")
    print("9. Valor absoluto")
    print("10. Factorial")
    print("11. Promedio")
    print("12. Redondeo")
    print("13. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "13":
        print("Gracias por utilizar la calculadora.")
        break

    if opcion not in ["1", "2", "3", "4", "5", "6", "7",
                      "8", "9", "10", "11", "12"]:
        print("Opción no válida. Intente nuevamente.")
        continue

    try:
        if opcion == "1":
            a = leer_numero("Ingrese el primer número: ")
            b = leer_numero("Ingrese el segundo número: ")
            resultado = suma(a, b)

        elif opcion == "2":
            a = leer_numero("Ingrese el primer número: ")
            b = leer_numero("Ingrese el segundo número: ")
            resultado = resta(a, b)

        elif opcion == "3":
            a = leer_numero("Ingrese el primer número: ")
            b = leer_numero("Ingrese el segundo número: ")
            resultado = producto(a, b)

        elif opcion == "4":
            a = leer_numero("Ingrese el primer número: ")
            b = leer_numero("Ingrese el segundo número: ")
            resultado = division(a, b)

        elif opcion == "5":
            base = leer_numero("Ingrese la base: ")
            exponente = leer_numero("Ingrese el exponente: ")
            resultado = potencia(base, exponente)

        elif opcion == "6":
            dividendo = leer_numero("Ingrese el dividendo: ")
            divisor = leer_numero("Ingrese el divisor: ")
            resultado = modulo(dividendo, divisor)

        elif opcion == "7":
            numero = leer_numero("Ingrese el número: ")
            resultado = raiz_cuadrada(numero)

        elif opcion == "8":
            porcentaje_valor = leer_numero("Ingrese el porcentaje: ")
            cantidad = leer_numero("Ingrese la cantidad: ")
            resultado = porcentaje(porcentaje_valor, cantidad)

        elif opcion == "9":
            numero = leer_numero("Ingrese el número: ")
            resultado = valor_absoluto(numero)

        elif opcion == "10":
            numero = leer_entero("Ingrese un número entero: ")
            resultado = factorial(numero)

        elif opcion == "11":
            cantidad = leer_entero("¿Cuántos números desea promediar?: ")
            if cantidad < 1:
                print("Debe ingresar al menos un número.")
                continue

            numeros = []
            for i in range(cantidad):
                numero = leer_numero("Ingrese un número: ")
                numeros.append(numero)

            resultado = promedio(*numeros)

        elif opcion == "12":
            numero = leer_numero("Ingrese el número: ")
            decimales = leer_entero("Ingrese la cantidad de decimales: ")
            resultado = redondear(numero, decimales)

        print("Resultado:", resultado)

    except (ValueError, ZeroDivisionError) as error:
        print("Error:", error)
        
    continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()

    while continuar not in ["s", "n"]:
        print("Opción no válida. Ingrese s o n.")
        continuar = input("¿Desea realizar otra operación? (s/n): ").lower()

    if continuar == "n":
        print("Gracias por utilizar la calculadora.")
        break