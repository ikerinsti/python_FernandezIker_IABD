import random

def mostrar_menu():
    print("Escoge a que jugar")
    print("1. Pedra - Paper -Tissores")
    print("2. Penjat")
    print("3. Tres en ratlla")
    print("4. Blackjack")
    opcio = int(input("Escribe el numero: "))

    match opcio:
        case 1:
            PedraPaperTissores()
        case 2:
            Penjat()
        case 3:
            TresEnRatlla()
        case 4:
            Blackjack()



def PedraPaperTissores():
    print("Has escogido Piedra Papel Tijera")
    print("Piedra es = 1, Papel es = 2, Tijera es = 3")
    puntuacionUser = 0
    puntuacionIa = 0
    while True:
        if puntuacionIa == 3:
            print(f"Ha ganado la IA con una puntuacion de {puntuacionIa} - {puntuacionUser}")
            break
        elif puntuacionUser == 3:
            print(f"Has ganado a la IA con una puntuacion de {puntuacionUser} - {puntuacionIa}")
            break
        opcionUser = int(input("Escoge que tirar: "))
        opcionIa = random.randint(1,3)
        if opcionUser > 3:
            print("Escoge entre 1, 2 o 3")
        
        if opcionUser == opcionIa:
            print("Los dos habeis sacado lo mismo")

        elif opcionUser == 1:
            if opcionIa == 2:
                puntuacionIa += 1
                print("La IA ha sacado papel, has perdido")
            else:
                puntuacionUser += 1
                print("La IA ha sacado tijeras, has ganado")
        elif opcionUser == 2:
            if opcionIa == 3:
                puntuacionIa += 1
                print("La IA ha sacado tijeras, has perdido")
            else:
                puntuacionUser += 1
                print("La IA ha sacado piedra, has ganado")
        elif opcionUser == 3:
            if opcionIa == 1:
                puntuacionIa += 1
                print("La IA ha sacado piedra, has perdido")
            else:
                puntuacionUser += 1
                print("La IA ha sacado papel, has ganado")


        print(f"Tu puntuacion es {puntuacionUser} y la de la IA {puntuacionIa}")

             

def Penjat():
    PALABRAS = [
        "red",
        "web",
        "bit",
        "dato",
        "nube",
        "base",
        "nodo",
        "texto",
        "bucle",
        "clave",
        "disco",
        "raton",
        "codigo",
        "python",
        "matriz",
        "puerto",
        "bloque",
        "memoria",
        "funcion",
        "consola",
    ]

    palabra_secreta = random.choice(PALABRAS)
    letras_usadas = []
    intentos = len(palabra_secreta) * 2

    print("¡Bienvenido al juego del Ahorcado!")

    while intentos > 0:

        palabra_oculta = ""
        for letra in palabra_secreta:
            if letra in letras_usadas:
                palabra_oculta += letra + " "
            else:
                palabra_oculta += "_ "

        print(f"\nPalabra: {palabra_oculta}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        print(f"Intentos restantes: {intentos}")

        if "_" not in palabra_oculta:
            print("\n¡Felicidades! ¡Has adivinado la palabra!")
            break

        letra = input("\nIntroduce una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introduce una sola letra válida.")
            continue

        if letra in letras_usadas:
            print("Ya has probado esa letra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra_secreta:
            print(f"¡Acierto! La letra '{letra}' está en la palabra.")
        else:
            print(f"La letra '{letra}' no está.")
            intentos -= 1

    if intentos == 0:
        print(f"\n¡Has perdido! La palabra era: {palabra_secreta}")


def TresEnRatlla():

    tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    combinaciones = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),  # Filas
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),  # Columnas
        (0, 4, 8),
        (2, 4, 6),  # Diagonales
    ]

    jugador = "X"
    turnos = 0
    ganador = None

    while True:
        dibujo_tablero = f'''
        {tablero[0]} | {tablero[1]} | {tablero[2]} 
        ---+---+---
        {tablero[3]} | {tablero[4]} | {tablero[5]} 
        ---+---+---
        {tablero[6]} | {tablero[7]} | {tablero[8]} 
            '''
        print(dibujo_tablero)

        if ganador:
            print(f"¡Enhorabuena! Ha ganado el jugador {ganador}.")
            break
        elif turnos == 9:
            print("¡Empate! Se han completado todas las casillas.")
            break

        eleccion = int(input(f"Turno de {jugador}. Elige casilla (1-9): ")) - 1

        if eleccion < 0 or eleccion > 8 or tablero[eleccion] in ["X", "O"]:
            print("Casilla no válida o ya ocupada. Intenta de nuevo.")

        tablero[eleccion] = jugador
        turnos += 1

        for a, b, c in combinaciones:
            if tablero[a] == tablero[b] == tablero[c] == jugador:
                ganador = jugador
                break

        if not ganador:
            jugador = "O" if jugador == "X" else "X"

def Blackjack():
    print("\n=== JUEGO DE BLACKJACK (21) ===")

    baraja = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(baraja)

    mano_jugador = [baraja.pop(), baraja.pop()]
    mano_crupier = [baraja.pop(), baraja.pop()]

    jugando = True
    while jugando:
        if sum(mano_jugador) > 21 and 11 in mano_jugador:
            mano_jugador[mano_jugador.index(11)] = 1

        puntos_jugador = sum(mano_jugador)

        top_j = ""
        mid_j = ""
        bot_j = ""
        for carta in mano_jugador:
            val = "A" if carta == 11 else str(carta)
            top_j += "+---+ "
            bot_j += "+---+ "
            if len(val) == 1:
                mid_j += f"| {val} | "
            else:
                mid_j += f"|{val} | "

        print("\nTus cartas:")
        print(top_j)
        print(mid_j)
        print(bot_j)
        print(f"Total: {puntos_jugador}")

        val_crupier = (
            "A" if mano_crupier[0] == 11 else str(mano_crupier[0])
        )
        mid_crupier = (
            f"| {val_crupier} |" if len(val_crupier) == 1 else f"|{val_crupier} |"
        )

        print("\nCarta visible del crupier:")
        print("+---+ +---+")
        print(f"{mid_crupier} | ? |")
        print("+---+ +---+")

        if puntos_jugador > 21:
            print("\n¡Te has pasado de 21! Has perdido la partida.")
            return
        elif puntos_jugador == 21:
            print("\n¡Tienes 21 exactos!")
            break

        opcion = input("\n¿Quieres pedir carta (1) o plantarte (2)?: ")
        if opcion == "1":
            mano_jugador.append(baraja.pop())
        elif opcion == "2":
            jugando = False
        else:
            print("Opción no válida. Introduce 1 o 2.")

    print("\n--- Turno del Crupier ---")
    while sum(mano_crupier) < 17:
        if sum(mano_crupier) > 21 and 11 in mano_crupier:
            mano_crupier[mano_crupier.index(11)] = 1
        mano_crupier.append(baraja.pop())

    if sum(mano_crupier) > 21 and 11 in mano_crupier:
        mano_crupier[mano_crupier.index(11)] = 1

    puntos_crupier = sum(mano_crupier)

    top_c = ""
    mid_c = ""
    bot_c = ""
    for carta in mano_crupier:
        val = "A" if carta == 11 else str(carta)
        top_c += "+---+ "
        bot_c += "+---+ "
        if len(val) == 1:
            mid_c += f"| {val} | "
        else:
            mid_c += f"|{val} | "

    print("\nCartas finales del crupier:")
    print(top_c)
    print(mid_c)
    print(bot_c)
    print(f"Total del crupier: {puntos_crupier}")

    if puntos_crupier > 21:
        print("\n¡El crupier se ha pasado de 21! ¡Has ganado!")
    elif puntos_jugador > puntos_crupier:
        print(
            f"\n¡Has ganado! Tu puntuación ({puntos_jugador}) es superior a la del crupier ({puntos_crupier})."
        )
    elif puntos_jugador < puntos_crupier:
        print(
            f"\nHas perdido. El crupier tiene más puntos ({puntos_crupier}) que tú ({puntos_jugador})."
        )
    else:
        print(
            f"\n¡Empate! Ambos tenéis {puntos_jugador} puntos."
        )


mostrar_menu()