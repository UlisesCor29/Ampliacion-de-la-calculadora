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


# Almacena las operaciones realizadas.
historial = []


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
    print("13. Consultar historial")
    print("14. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "14":
        print("Gracias por utilizar la calculadora.")
        break

    # Consultar el historial.
    if opcion == "13":
        print("\n===== HISTORIAL DE OPERACIONES =====")

        if len(historial) == 0:
            print("Todavía no hay operaciones registradas.")
        else:
            for i, registro in enumerate(historial, start=1):
                print(f"\n{i}. {registro['operacion']}")
                print("Valores:", registro["valores"])
                print("Resultado:", registro["resultado"])

        continue

    if opcion not in ["1", "2", "3", "4", "5", "6", "7",
                      "8", "9", "10", "11", "12"]:
        print("Opción no válida. Intente nuevamente.")
        continue

    try:
        if opcion == "1":
            a = leer_numero("Ingrese el primer número: ")
            b = leer_numero("Ingrese el segundo número: ")
            operacion = "Suma"
            valores = [a, b]
            resultado = suma(a, b)

        elif opcion == "2":
            a = leer_numero("Ingrese el primer número: ")
            b = leer_numero("Ingrese el segundo número: ")
            operacion = "Resta"
            valores = [a, b]
            resultado = resta(a, b)

        elif opcion == "3":
            a = leer_numero("Ingrese el primer número: ")
            b = leer_numero("Ingrese el segundo número: ")
            operacion = "Multiplicación"
            valores = [a, b]
            resultado = producto(a, b)

        elif opcion == "4":
            a = leer_numero("Ingrese el primer número: ")
            b = leer_numero("Ingrese el segundo número: ")
            operacion = "División"
            valores = [a, b]
            resultado = division(a, b)

        elif opcion == "5":
            base = leer_numero("Ingrese la base: ")
            exponente = leer_numero("Ingrese el exponente: ")
            operacion = "Potencia"
            valores = [base, exponente]
            resultado = potencia(base, exponente)

        elif opcion == "6":
            dividendo = leer_numero("Ingrese el dividendo: ")
            divisor = leer_numero("Ingrese el divisor: ")
            operacion = "Módulo"
            valores = [dividendo, divisor]
            resultado = modulo(dividendo, divisor)

        elif opcion == "7":
            numero = leer_numero("Ingrese el número: ")
            operacion = "Raíz cuadrada"
            valores = [numero]
            resultado = raiz_cuadrada(numero)

        elif opcion == "8":
            porcentaje_valor = leer_numero("Ingrese el porcentaje: ")
            cantidad = leer_numero("Ingrese la cantidad: ")
            operacion = "Porcentaje"
            valores = [porcentaje_valor, cantidad]
            resultado = porcentaje(porcentaje_valor, cantidad)

        elif opcion == "9":
            numero = leer_numero("Ingrese el número: ")
            operacion = "Valor absoluto"
            valores = [numero]
            resultado = valor_absoluto(numero)

        elif opcion == "10":
            numero = leer_entero("Ingrese un número entero: ")
            operacion = "Factorial"
            valores = [numero]
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

            operacion = "Promedio"
            valores = numeros.copy()
            resultado = promedio(*numeros)

        elif opcion == "12":
            numero = leer_numero("Ingrese el número: ")
            decimales = leer_entero("Ingrese la cantidad de decimales: ")
            operacion = "Redondeo"
            valores = [numero, decimales]
            resultado = redondear(numero, decimales)

        # Registrar solamente las operaciones completadas.
        historial.append({
            "operacion": operacion,
            "valores": valores,
            "resultado": resultado
        })

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
