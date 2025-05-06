import numpy as np
import os

def clear_console():
    clear = lambda: os.system('cls')
    clear()
    return None

def crear_tablero():
    tablero = np.full((10, 10), " ")
    return tablero

def colocar_barcos(tablero, barco):  # update a lista de lista
# barcos_jugador = [[[0, 3],[0, 4], [0, 5], [0, 6]], [[4, 7],[5, 7], [6, 7]], [[8, 8],[8, 9]],[[1, 7]]]
    for i in barco:
        for j in i:
        # tablero[i[0], i[1]] = "0"    # row, col
            tablero[j[0], j[1]] = "O"
    return tablero

def disparar(casilla, tablero):
    tablero[casilla[0], casilla[1]] = "+"

# def crear_tablero(tamanio):
#     pass

# def colocar_barcos(barco, tablero):
#     pass


# def crear_barco(eslora):
#     pass