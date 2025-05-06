from utils import *
from var import *

# Variables globales
touche = True
turno = 1 # 1 si es jugador / 0 PC
tablero_jugador_tiros = []
tirados = []

"""
Init tableros
"""
clear_console()
print("========================================================")

tablero_jugador = crear_tablero()
tablero_jugador_tiros = crear_tablero()
# TODO: generar barcos
tablero_jugador = colocar_barcos(tablero_jugador, barcos_jugador)
print("Tablero del juhgador con barcos cargados:")
print_tablero(tablero_jugador)

tablero_pc = crear_tablero()
tablero_pc = colocar_barcos(tablero_pc, barcos_pc)
print("Tablero del PC con barcos cargados:")
print_tablero(tablero_pc)

# disparar([0, 2], tablero_jugador)
# print(tablero_jugador)

while touche:
    if turno:
        casilla = [int(x) for x in input("Introduce dos nº separados por comma (fila, col): ").split(',')]
        if casilla in tirados:
            print("punto gastado; intentalo de nuevo")
            casilla = [int(x) for x in input("Introduce dos nº separados por comma (fila, col): ").split(',')]
        tirados.append(casilla)
        turno, tablero_pc = disparar(casilla, tablero_pc, barcos_pc)
        tablero_jugador_tiros[casilla[0], casilla[1]] = "X" if turno else "A"
        print('tablero PC tras disparos')
        print_tablero(tablero_pc)
        print('tablero MIO tiros tras disparos')
        print_tablero(tablero_jugador_tiros)
        print(barcos_pc)    
    else:
        # turno PC
        dispara_random()
        casilla = [int(x) for x in input("Introduce dos nº separados por comma (fila, col): ").split(',')]
        if casilla in tirados:
            print("punto gastado; intentalo de nuevo")
            casilla = [int(x) for x in input("Introduce dos nº separados por comma (fila, col): ").split(',')]
        tirados.append(casilla)
        _, tablero_jugador  = disparar(casilla, tablero_jugador, barcos_jugador)
        print('tablero JUGADOR tras disparos')
        print_tablero(tablero_jugador)
        print(barcos_pc)