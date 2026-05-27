while True:
    print("OPCIÓNES:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Que quieres hacer (1-5): ")
    
    if opcion == "1":
        while True:
            numero1 = input("Pon el primer numero: ")
            if numero1.isdigit():
                numero1 = int(numero1)
                break
            else:
                print("Eso no es un numero... vuelve a probar")
                continue
        while True:        
            numero2 = input("Pon el segundo numero: ")
            if numero2.isdigit():
                numero2 = int(numero2)
                break
            else:
                print("Eso no es un numero... vuelve a probar")
                continue
                
        resultado = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es: {resultado}")

    if opcion == "2":
        while True:
            numero1 = input("Pon el primer numero: ")
            if numero1.isdigit():
                numero1 = int(numero1)
                break
            else:
                print("Eso no es un numero... vuelve a probar")
                continue
        while True:        
            numero2 = input("Pon el segundo numero: ")
            if numero2.isdigit():
                numero2 = int(numero2)
                break
            else:
                print("Eso no es un numero... vuelve a probar")
                continue
                
        resultado = numero1 - numero2
        print(f"El resultado de {numero1} menos {numero2} es: {resultado}")

    if opcion == "3":
        while True:
            numero1 = input("Pon el primer numero: ")
            if numero1.isdigit():
                numero1 = int(numero1)
                break
            else:
                print("Eso no es un numero... vuelve a probar")
                continue
        while True:        
            numero2 = input("Pon el segundo numero: ")
            if numero2.isdigit():
                numero2 = int(numero2)
                break
            else:
                print("Eso no es un numero... vuelve a probar")
                continue
                
        resultado = numero1 * numero2
        print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")

    if opcion == "4":
        while True:
            numero1 = input("Pon el primer numero: ")
            if numero1.isdigit():
                numero1 = int(numero1)
                break
            else:
                print("Eso no es un numero... vuelve a probar")
                continue
        while True:        
            numero2 = input("Pon el segundo numero: ")
            if numero2.isdigit():
                numero2 = int(numero2)
                break
            else:
                print("Eso no es un numero... vuelve a probar")
                continue
                
        resultado = numero1 / numero2
        resto = numero1 % numero2
        print(f"Dividiendo {numero1} entre {numero2} da: {resultado} y el resto es: {resto}")
    
    if opcion == "5":
        print("Adiós...")
        exit()