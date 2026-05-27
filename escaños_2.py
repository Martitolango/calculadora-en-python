# Diccionario principal de la sesión
# Guarda datos del censo, votos, partidos, escaños y umbral

sesion = {
    "censo": 0,
    "votos_blancos": 0,
    "votos_nulos": 0,
    "partidos": [],
    "escanos": 0,
    "umbral": 0
}


# Función para calcular el censo provisional
# Suma votos de partidos + votos en blanco + votos nulos

def censo_provisional(a, b, c):
    return a + b + c


# Función para introducir todos los datos de la sesión

def introducir_datos():

    # Limpiar lista de partidos antes de empezar
    sesion["partidos"] = []

    # Pedir número de partidos
    while True:
        np = input("Cuántos partidos se han presentado?: ")

        if np.isdigit() and int(np) > 1:
            np = int(np)
            break

        print("Número inválido.")

    # Pedir el censo
    while True:
        censo = input("Introduce el censo: ")

        if censo.isdigit():
            sesion["censo"] = int(censo)
            break

        print("Número inválido.")

    # Pedir votos en blanco
    while True:
        votos_b = input("Votos en blanco: ")

        if votos_b.isdigit():
            sesion["votos_blancos"] = int(votos_b)
            break

        print("Número inválido.")

    # Pedir votos nulos
    while True:
        votos_n = input("Votos nulos: ")

        if votos_n.isdigit():
            sesion["votos_nulos"] = int(votos_n)
            break

        print("Número inválido.")

    # Pedir umbral porcentual
    while True:
        umbral = input("Umbral (%): ")

        if umbral.isdigit():
            sesion["umbral"] = int(umbral)
            break

        print("Número inválido.")

    # Pedir número de escaños
    while True:
        escaños = input("Escaños: ")

        if escaños.isdigit() and int(escaños) >= 5:
            sesion["escanos"] = int(escaños)
            break

        print("Escaños inválidos (mínimo 5).")

    # Pedir datos de cada partido
    for i in range(np):

        while True:

            nombre = input(f"Nombre del partido {i+1}: ").strip()
            votos = input("Votos: ").strip()

            # Validar nombre
            if not nombre:
                print("Nombre inválido.")
                continue

            # Validar votos
            if not votos.isdigit():
                print("Votos inválidos.")
                continue

            votos = int(votos)

            # Comprobar nombres duplicados
            duplicado = False

            for p in sesion["partidos"]:

                if p["nombre"].lower() == nombre.lower():
                    duplicado = True
                    break

            if duplicado:
                print("Ese partido ya existe.")
                continue

            # Añadir partido a la lista
            sesion["partidos"].append({
                "nombre": nombre,
                "votos": votos,
                "escaños": 0
            })

            break

    # Calcular votos totales
    total_votos = censo_provisional(

        sum(p["votos"] for p in sesion["partidos"]),

        sesion["votos_blancos"],

        sesion["votos_nulos"]

    )

    # Comprobar que no se supera el censo
    if total_votos > sesion["censo"]:

        print("ERROR: Los votos superan el censo.")
        print("Se borrarán los datos.")

        sesion["partidos"] = []


# Función para mostrar los partidos registrados

def listar_partidos():

    if not sesion["partidos"]:
        print("No hay partidos registrados.")
        return

    # enumerate() devuelve:
    # índice + elemento de la lista
    #
    # i = número de posición
    # p = diccionario del partido

    for i, p in enumerate(sesion["partidos"], 1):

        print(
            f"{i}. {p['nombre']} | "
            f"Votos: {p['votos']} | "
            f"Escaños: {p['escaños']}"
        )


# Función para editar un partido

def editar_partido():

    listar_partidos()

    if not sesion["partidos"]:
        return

    idx = input("Número del partido a editar: ")

    # Validar número
    if not idx.isdigit():
        print("Entrada inválida.")
        return

    idx = int(idx) - 1

    # Validar rango
    if idx < 0 or idx >= len(sesion["partidos"]):
        print("Índice inválido.")
        return

    # Editar nombre
    nuevo_nombre = input(
        "Nuevo nombre (enter para mantener): "
    ).strip()

    if nuevo_nombre:

        duplicado = False

        for i, p in enumerate(sesion["partidos"]):

            if i != idx and p["nombre"].lower() == nuevo_nombre.lower():
                duplicado = True
                break

        if duplicado:

            print("Nombre duplicado.")

        else:

            sesion["partidos"][idx]["nombre"] = nuevo_nombre

    # Editar votos
    nuevos_votos = input(
        "Nuevos votos (enter para mantener): "
    ).strip()

    if nuevos_votos.isdigit():

        sesion["partidos"][idx]["votos"] = int(nuevos_votos)

    elif nuevos_votos != "":

        print("Votos no modificados (valor inválido).")


# Función para borrar un partido

def borrar_partido():

    listar_partidos()

    if not sesion["partidos"]:
        return

    idx = input("Número del partido a borrar: ")

    # Validar entrada
    if not idx.isdigit():
        print("Entrada inválida.")
        return

    idx = int(idx) - 1

    # Validar rango
    if idx < 0 or idx >= len(sesion["partidos"]):
        print("Índice inválido.")
        return

    # pop() elimina el partido
    # y devuelve el elemento eliminado

    eliminado = sesion["partidos"].pop(idx)

    print(f"Partido eliminado: {eliminado['nombre']}")


# Función para calcular el reparto D'Hondt

def calcular_dhondt():

    if not sesion["partidos"]:
        print("No hay partidos.")
        return

    # Reiniciar escaños
    for p in sesion["partidos"]:

        p["escaños"] = 0

    # Calcular votos válidos
    votos_validos_totales = sum(
        p["votos"] for p in sesion["partidos"]
    )

    # Calcular umbral mínimo
    umbral_votos = votos_validos_totales * (
        sesion["umbral"] / 100
    )

    # Filtrar partidos que superan el umbral
    sesion["partidos"] = [

        p for p in sesion["partidos"]

        if p["votos"] >= umbral_votos

    ]

    if not sesion["partidos"]:
        print("Ningún partido supera el umbral.")
        return

    # Reparto de escaños D'Hondt
    for _ in range(sesion["escanos"]):

        max_index = 0
        max_cociente = -1

        for idx, p in enumerate(sesion["partidos"]):

            cociente = p["votos"] / (
                p["escaños"] + 1
            )

            if cociente > max_cociente:

                max_cociente = cociente
                max_index = idx

        # Sumar escaño al partido ganador
        sesion["partidos"][max_index]["escaños"] += 1

    print("Cálculo completado.")


# Función para mostrar resultados finales

def mostrar_resultados():

    if not sesion["partidos"]:
        print("No hay resultados calculados.")
        return

    # Crear copia de la lista
    # para no modificar la original

    ordenados = sesion["partidos"][:]

    # Ordenación manual de mayor a menor
    # según número de escaños

    for i in range(len(ordenados)):

        for j in range(i + 1, len(ordenados)):

            if (
                ordenados[j]["escaños"]
                >
                ordenados[i]["escaños"]
            ):

                # Intercambiar posiciones
                ordenados[i], ordenados[j] = (
                    ordenados[j],
                    ordenados[i]
                )

    print("\n=== RESULTADOS FINALES ===")

    for i, p in enumerate(ordenados, 1):

        print(
            f"{i}. {p['nombre']} | "
            f"Votos: {p['votos']} | "
            f"Escaños: {p['escaños']}"
        )


# Menú principal

def menu():

    while True:

        print("""
        ----- MENU -----

        1. Introducir datos
        2. Listar partidos
        3. Editar partido
        4. Borrar partido
        5. Calcular D’Hondt
        6. Mostrar resultados
        7. Salir
        """)

        opcion = input("Elige una opción: ").strip()

        match opcion:

            case "1":
                introducir_datos()

            case "2":
                listar_partidos()

            case "3":
                editar_partido()

            case "4":
                borrar_partido()

            case "5":
                calcular_dhondt()

            case "6":
                mostrar_resultados()

            case "7":

                print("Adiós!")
                break

            case _:

                print("Opción incorrecta.")


# Ejecutar menú

menu()