from operaciones import suma, resta, producto, division
from operaciones import potencia, modulo, raiz_cuadrada
from operaciones import porcentaje, valor_absoluto
from operaciones import factorial, promedio, redondear

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
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = suma(a, b)

        elif opcion == "2":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = resta(a, b)

        elif opcion == "3":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = producto(a, b)

        elif opcion == "4":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            resultado = division(a, b)

        elif opcion == "5":
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            resultado = potencia(base, exponente)

        elif opcion == "6":
            dividendo = float(input("Ingrese el dividendo: "))
            divisor = float(input("Ingrese el divisor: "))
            resultado = modulo(dividendo, divisor)

        elif opcion == "7":
            numero = float(input("Ingrese el número: "))
            resultado = raiz_cuadrada(numero)

        elif opcion == "8":
            porcentaje_valor = float(input("Ingrese el porcentaje: "))
            cantidad = float(input("Ingrese la cantidad: "))
            resultado = porcentaje(porcentaje_valor, cantidad)

        elif opcion == "9":
            numero = float(input("Ingrese el número: "))
            resultado = valor_absoluto(numero)

        elif opcion == "10":
            numero = int(input("Ingrese un número entero: "))
            resultado = factorial(numero)

        elif opcion == "11":
            cantidad = int(input("¿Cuántos números desea promediar?: "))
            if cantidad < 1:
                print("Debe ingresar al menos un número.")
                continue

            numeros = []
            for i in range(cantidad):
                numero = float(input("Ingrese un número: "))
                numeros.append(numero)

            resultado = promedio(*numeros)

        elif opcion == "12":
            numero = float(input("Ingrese el número: "))
            decimales = int(input("Ingrese la cantidad de decimales: "))
            resultado = redondear(numero, decimales)

        print("Resultado:", resultado)

    except (ValueError, ZeroDivisionError) as error:
        print("Error:", error)
