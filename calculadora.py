def pedir_numero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return float(valor)
        except ValueError:
            print("Eso no es un numero... vuelve a probar")

while True:
    print("OPCIONES:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Que quieres hacer (1-5): ")

    if opcion == "1":
        numero1 = pedir_numero("Pon el primer numero: ")
        numero2 = pedir_numero("Pon el segundo numero: ")
        resultado = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es: {resultado}")

    elif opcion == "2":
        numero1 = pedir_numero("Pon el primer numero: ")
        numero2 = pedir_numero("Pon el segundo numero: ")
        resultado = numero1 - numero2
        print(f"El resultado de {numero1} menos {numero2} es: {resultado}")

    elif opcion == "3":
        numero1 = pedir_numero("Pon el primer numero: ")
        numero2 = pedir_numero("Pon el segundo numero: ")
        resultado = numero1 * numero2
        print(f"La multiplicacion de {numero1} y {numero2} es: {resultado}")

    elif opcion == "4":
        numero1 = pedir_numero("Pon el primer numero: ")
        numero2 = pedir_numero("Pon el segundo numero: ")
        if numero2 == 0:
            print("No se puede dividir por cero")
            continue
        resultado = numero1 / numero2
        resto = numero1 % numero2
        print(f"Dividiendo {numero1} entre {numero2} da: {resultado} y el resto es: {resto}")

    elif opcion == "5":
        print("Adios...")
        break

    else:
        print("Opcion no valida, elige entre 1 y 5")
