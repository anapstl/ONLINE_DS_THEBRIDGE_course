import numpy as np
import os
import time

def clear_console():
    '''
    Limpia la consola.
    '''
    clear = lambda: os.system('cls')
    clear()
    return None

def pretty_tablero(tablero:np.ndarray):
    '''
    Imprime tablero sin comillas.
    Parametro de entrada:
        tablero: de tipo _numpy.ndarray_, que se desea imprimir.
    '''
    for tb in tablero:
        print(*tb)
    return None

def crear_tablero(tamaño=10):
    """
    Crea un tablero de dimensión `tamaño x tamaño` relleno con '_'. 
    Parametros:
        tamaño: _int_, valor por defecto 10.
    """
    return np.full((tamaño, tamaño), "_")

# def colocar_barco(barco, tablero):
#     """
#     Coloca un barco en el tablero. El barco es una lista de coordenadas.
#     """
#     for casilla in barco:
#         tablero[casilla[0], casilla[1]] = "O"
#     return tablero

def colocar_barcos(tablero, barco):  # update a lista de lista
# barco_jugador = [[[0, 3],[0, 4], [0, 5], [0, 6]], [[4, 7],[5, 7], [6, 7]], [[8, 8],[8, 9]],[[1, 7]]]
    for i in barco:
        for j in i:
            tablero[j[0], j[1]] = "O"
    return tablero

def disparar(casilla:list, barcos:list, tablero:np.ndarray, *tablero_jugador_tiros:np.ndarray):
    '''
    Función de disparar para el Jugador. 
    Parametros de entrada:
        casilla: _lista_ de 2 valores _int_ que representa las coordenadas [row, col] del disparo
        barcos:  _lista_ de barcos correspondiente al turno
        tablero: _np.ndarray_, matriz sobre cual se ejecuta el disparo segun el turno
        tablero_jugador_tiros:  _np.ndarray_, arg opcional, el tablero de tiros del Jugador para actualizar los tiros
    Devuelve:
        (True/False, tablero): booleano: que representa si ha acertado o no, y el
        tablero actualizado
    '''
    print("---------------------------------------casilla", casilla)
    print("---------------------------------------barcos", barcos)

    for barco in barcos:
        print("barco de for disparar:", barco)
        if casilla in barco:
            print('TOUCHE')
            # pintarlo con "X"
            tablero[casilla[0], casilla[1]] = "X"
            if tablero_jugador_tiros:
                tablero_jugador_tiros[0][casilla[0], casilla[1]] = "X"
            barco.remove(casilla)
            if len(barco) == 0:
                print("BARCO HUNDIDO")
            return True, tablero

    # agua
    print("agua")
    tablero[casilla[0], casilla[1]] = "A"
    if tablero_jugador_tiros:
        tablero_jugador_tiros[0][casilla[0], casilla[1]] = "A"
    print("CAMBIO TURNO")
    return False, tablero

def get_xy_tiro(turno:bool):
    if turno:
        
    return casilla

# def colocar_barcos(barco, tablero):
#     pass

# def crear_barco(eslora):
#     pass