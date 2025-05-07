from utils import *
from var import *
import emoji

# Variables globales

# si ha tocado barco
touche = True
# 1 si es jugador / 0 PC
turno = 1
tirados = []

"""
Init tableros
"""
clear_console()
print("======================================================== HUNDIR LA FLOTA")

tablero_jugador = crear_tablero()
tablero_jugador_tiros = crear_tablero()
tablero_pc = crear_tablero()

# TODO: generar barcos
tablero_jugador = colocar_barcos(tablero_jugador, barcos_jugador)
print("Tablero del jugador con barcos cargados:")
pretty_tablero(tablero_jugador)

tablero_pc = crear_tablero()
tablero_pc = colocar_barcos(tablero_pc, barcos_pc)
print("Tablero del PC con barcos cargados:")
pretty_tablero(tablero_pc)

# disparar([0, 2], tablero_jugador)
# print(tablero_jugador)

while touche:
    print("El turno es del:", "JUGADOR" if turno else "PC")
    if turno:
        casilla = get_xy_tiro(turno)                           # Es el turno del JUGADOR
        # casilla = [int(x) for x in input("Introduce dos nº separados por comma (fila, col): ").split(',')]
        # TODO: ctrl input, chars, nr mayores
        # if casilla in tirados:
        #     print("Tiro repetido; intentalo de nuevo")
        #     casilla = [int(x) for x in input("Introduce dos nº separados por comma (fila, col): ").split(',')]
        # tirados.append(casilla)
        barcos_pc_cpy = barcos_pc.copy()
        turno, tablero_pc = disparar(turno, casilla, barcos_pc_cpy, tablero_pc, tablero_jugador_tiros)  # despues de disparar hay que ver si quedan barcos... sin no Has Ganado
        print("barcos pc", barcos_pc_cpy)
        print('Tablero PC tras disparos')
        pretty_tablero(tablero_pc)
        print('Tablero Tiros Jugador tras disparos')
        pretty_tablero(tablero_jugador_tiros)
        print(barcos_pc)
        if turno and all(len(barco) == 0 for barco in barcos_pc_cpy):
            print("Felicidades, has ganado!")
            break
    else:
        # turno PC
        casilla = get_xy_tiro(turno)
        # casilla = [int(x) for x in input("Introduce dos nº separados por comma (fila, col): ").split(',')]
        # if casilla in tirados:
        #     print("Tiro repetido; intentalo de nuevo")
        #     casilla = [int(x) for x in input("Introduce dos nº separados por comma (fila, col): ").split(',')]
        # tirados.append(casilla)
        barcos_jugador_cpy = barcos_jugador.copy()
        turno, tablero_jugador  = disparar(turno, casilla, barcos_jugador_cpy, tablero_jugador)
        print('tablero JUGADOR tras disparos')
        pretty_tablero(tablero_jugador)
        print(barcos_jugador)
        if (not turno) and all(len(barco) == 0 for barco in barcos_jugador_cpy):
            print(emoji.emojize("El PC ha ganado :crying_face:. ¡Suerte la próxima vez!"))
            break