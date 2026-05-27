while True:
    print("OPCIÓNES:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Que quieres hacer (1-4): ")
    
    if opcion == "1":
        while True:
            numero1 = input("Pon el primer numero: ")
            if numero1.isdigit():
                numero1 = int(numero1)
                continue
            else:
                print("Eso no es un numero... vuelve a probar")
                
            numero2 = input("Pon el segundo numero: ")
                if numero2.isdigit():
                    numero2 = int(numero2)
                    continue
                else:
                    print("Eso no es un numero... vuelve a probar")
            resultadosum = numero1 + numero2
            print(f"La suma de {numero1} y {numero2} es: {resultadosum}")
        exit()