import numpy as np
import os
import random
import time

tirados_jugador = []
tirados_pc = []

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

def colocar_barcos(tablero:np.ndarray, barcos:list):  # update a lista de lista
    """
    Coloca los barcos en el tablero. Es una lista de barcos y cada barco es una lista de coordenadas.
    Los barcos se representan con el simbolo "O".
    Parametros de entrada:
        tablero: _np.ndarray_ respresentando el tablero
        barcos: _list_ la lista de listas de barcos
    Devuelve:
        tablero: _np.ndarray_ el tablero actualizado con los barcos
    """
    # barco_jugador = [[[0, 3],[0, 4], [0, 5], [0, 6]], [[4, 7],[5, 7], [6, 7]], [[8, 8],[8, 9]],[[1, 7]]]
    for barco in barcos:
        for i in barco:
            tablero[i[0], i[1]] = "O"
    return tablero

def disparar(turno:bool, casilla:list, barcos:list, tablero:np.ndarray, *tablero_jugador_tiros:np.ndarray):
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
            return turno, tablero

    # agua
    print("agua")
    tablero[casilla[0], casilla[1]] = "A"
    if tablero_jugador_tiros:
        tablero_jugador_tiros[0][casilla[0], casilla[1]] = "A"
    print("CAMBIO TURNO")
    return not(turno), tablero

def get_xy_tiro(turno:bool):
    if turno:
        casilla = [int(x) for x in input("Introduce dos nº separados por comma (fila, col): ").split(',')]
        # TODO: ctrl input, chars, nr mayores
        while (casilla in tirados_jugador):
            print("Tiro repetido; intentalo de nuevo")
            casilla = [int(x) for x in input("Introduce dos nº separados por comma (fila, col): ").split(',')]
        print("Tirados jugador antes", tirados_jugador)
        tirados_jugador.append(casilla)
        print("Tirados jugador despues", tirados_jugador)
    else:
        print("El PC elige los números:")
        time.sleep(2)
        # Las coordenadas de tiros del PC se generan de forma aleatoria.
        casilla = [random.randint(0,9) for _ in range(2)]
        time.sleep(2)
        print(casilla)
        while (casilla in tirados_pc):
            print("Tiro repetido; PC intenta de nuevo")
            casilla = [random.randint(0,9) for _ in range(2)]
        tirados_pc.append(casilla)
    return casilla

# def colocar_barcos(barco, tablero):
#     pass

# def crear_barco(eslora):
#     pass