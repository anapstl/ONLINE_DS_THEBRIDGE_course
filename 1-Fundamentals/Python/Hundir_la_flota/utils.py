import emoji
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
    Función de disparar para el Jugador. Los tiros se representan con "X" si ha tocado barco,
    y con "A" si ha tocado agua.
    Parametros de entrada:
        casilla: _lista_ de 2 valores _int_ que representa las coordenadas [row, col] del disparo
        barcos:  _lista_ de barcos correspondiente al turno
        tablero: _np.ndarray_, matriz sobre cual se ejecuta el disparo segun el turno
        tablero_jugador_tiros:  _np.ndarray_, arg opcional, el tablero de tiros del Jugador para actualizar los tiros
    Devuelve:
        (_True/False_, tablero): booleano: que representa si ha acertado o no, y el
        tablero actualizado
    '''
    print("---------------------------------------casilla", casilla)
    print("---------------------------------------barcos", barcos)

    for barco in barcos:
        print("barco de for disparar:", barco)
        if casilla in barco:
            print('TOUCHE')
            # Actualiza la casilla del barco tocado con "X"
            tablero[casilla[0], casilla[1]] = "X"
            if tablero_jugador_tiros:
                tablero_jugador_tiros[0][casilla[0], casilla[1]] = "X"
            barco.remove(casilla)
            # Comprobar si se han tocado todas las casillas del barco.
            if len(barco) == 0:
                print("BARCO HUNDIDO")
            return turno, tablero

    # En caso de fallo actualiza la casilla en el tablero con una "A"
    print("agua")
    tablero[casilla[0], casilla[1]] = "A"
    if tablero_jugador_tiros:
        tablero_jugador_tiros[0][casilla[0], casilla[1]] = "A"
    # En este caso se hace el cambio de turno.
    print("CAMBIO TURNO")
    return not(turno), tablero

def get_xy_tiro(turno:bool):
    """
    Obtiene las coordenadas del disparo según el turno.
    Si es el turno del jugador, solicita input validado.
    Si es el turno del PC, genera coordenadas aleatorias.
    """
    if turno:
        while True:
            try:
                casilla = [int(x) for x in input("Introduce dos nº separados por comma  (fila, col): ").split(',')]
                # Validar que sean exactamente dos números
                if len(casilla) != 2:
                    raise ValueError("Debes introducir exactamente dos números separados por coma.")
                
                # Validar rango de las coordenadas
                if not (0 <= casilla[0] < 10 and 0 <= casilla[1] < 10):
                    raise ValueError("Las coordenadas deben estar entre 0 y 9.")
                
                # Validar que no sea un tiro repetido
                if casilla in tirados_jugador:
                    print("Tiro repetido; intenta de nuevo.")
                    continue
                
                # Si todo es válido, agregar a la lista de tiros y salir del bucle
                tirados_jugador.append(casilla)
                print("Tirados jugador:", tirados_jugador)
                return casilla
            except ValueError as e:
                print(f"Entrada inválida: {e}. Intenta de nuevo.")
    else:
        print("El PC elige los números:")
        time.sleep(2)
        while True:
            # Generar coordenadas aleatorias
            casilla = [random.randint(0, 9) for _ in range(2)]
            
            # Validar que no sea un tiro repetido
            if casilla not in tirados_pc:
                tirados_pc.append(casilla)
                print("Tirados PC:", tirados_pc)
                return casilla
            print("Tiro repetido; PC intenta de nuevo.")

# def colocar_barco(barco, tablero):
#     for fila, col in barco:
#         tablero[fila, col] = 'O'

# def crear_barco(eslora):
# TODO
#     pass

def hay_ganador(barcos:list, msg:str):
    '''
    Verifica si hay un ganador: comprueba si quedan barcos en el tablero.
    En este caso, si quedan barcos en la lista de _barcos_ que se recibe.
    En caso afirmativo imprime el _msg_ y devuelve _True_ si ha llegado 
    al final, _False_ en caso contrario.
    Parametros:
        barcos: _list_ de los barcos del jugador/pc
        msg: _str_ que se devuelve si se cumple la condición
    Devuelve:
        _True/False_: booleano que marca si hay/no fin de juego.

    '''
    if all(len(barco) == 0 for barco in barcos):
            print(emoji.emojize(msg))
            return True
    return False

def ejecutar_turno(turno, tablero, barcos, tablero_tiros=None):
    casilla = get_xy_tiro(turno)
    turno, tablero = disparar(turno, casilla, barcos, tablero, tablero_tiros)
    pretty_tablero(tablero)
    if tablero_tiros:
        print("Tablero de tiros:")
        pretty_tablero(tablero_tiros)
    return turno