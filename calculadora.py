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
                
        resultadosum = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es: {resultadosum}")
exit()