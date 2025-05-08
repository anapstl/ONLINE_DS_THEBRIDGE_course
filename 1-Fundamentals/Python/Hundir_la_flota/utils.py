import emoji
import numpy as np
import os
import random
import time
from termcolor import colored
from vars import *

tirados_jugador = []
tirados_pc = []

def eleccion_tipo_juego():
    """
    Elección de tipo de juego: (0) Demo y (1) Completo.
    """
    while True:
        try:
            mensaje = (
                "Por favor, elige la versión que desea probar:\n"
                "\tPulsa 0️⃣  para la versión Demo.\n"
                "\tPulsa 1️⃣  para la versión completa.\n"
            )
            vers_elegida = int(input(mensaje))

            return bool(vers_elegida)
        except ValueError as e:
            print(colored(f"Entrada inválida: {e}. Intenta de nuevo.", "red"))

def run_ansi_codes_4_colors():
    clr = lambda: os.system('color')
    return None

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

def crear_tablero(tamaño=TAMANO_TABLERO):
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
    print("==================================================================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", barcos) if DEBUG_MODE else None
    for barco in barcos:
        for i in barco:
            tablero[i[0], i[1]] = "O"
    return tablero

def disparar(turno:bool, casilla:list, barcos:list, tablero:np.ndarray, tablero_jugador_tiros:np.ndarray=None):
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
    print("---------------------------------------casilla", casilla) if DEBUG_MODE else None
    print("---------------------------------------barcos", barcos) if DEBUG_MODE else None

    for barco in barcos:
        print("barco de for disparar:", barco) if DEBUG_MODE else None
        if casilla in barco:
            print(colored('TOUCHE 🎯', "yellow"))
            # Actualiza la casilla del barco tocado con "X"
            tablero[casilla[0], casilla[1]] = "X"
            tablero_jugador_tiros[casilla[0], casilla[1]] = "X"
            barco.remove(casilla)
            # Comprobar si se han tocado todas las casillas del barco.
            if len(barco) == 0:
                print(colored("BARCO HUNDIDO 🥳", "yellow"))
            return turno, tablero

    # En caso de fallo actualiza la casilla en el tablero con una "A"
    print("agua") if DEBUG_MODE else None
    tablero[casilla[0], casilla[1]] = "A"
    if type(tablero_jugador_tiros) is np.ndarray:
        tablero_jugador_tiros[casilla[0], casilla[1]] = "A"
    # En este caso se hace el cambio de turno.
    print(colored("CAMBIO TURNO", "magenta"))
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
                print("Tirados jugador:", tirados_jugador) if DEBUG_MODE else None
                return casilla
            except ValueError as e:
                print(colored(f"Entrada inválida: {e}. Intenta de nuevo.", "red"))
    else:
        print("El PC elige los números:")
        time.sleep(2)
        while True:
            # Generar coordenadas aleatorias
            casilla = [random.randint(0, 9) for _ in range(2)]
            print(casilla)
            # Validar que no sea un tiro repetido
            if casilla not in tirados_pc:
                tirados_pc.append(casilla)
                print("Tirados PC:", tirados_pc) if DEBUG_MODE else None
                return casilla
            print("Tiro repetido; PC intenta de nuevo.")

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
            print(colored(emoji.emojize(msg),"yellow"))
            return True
    return False

def ejecutar_turno(modalidad_juego:bool, turno: bool, tablero: np.ndarray, barcos: list, tablero_tiros:np.ndarray= None):
    """
    Ejecución del turno: se consigue la casilla a disparar, se dispara 
    y se actualiza el tablero de tiros.
    Parametros:
        modalidad_juego: si es Demo/ Completo
        turno: _bool_ si es jugador/ pc
        tablero: _np.ndarray_ el tablero del "jugador"
        barcos: _list_ de los barcos a disparar
        tablero_tiros: en el caso del jugador pasamos su tablero a actualizar
    Devuelve:
        turno: _bool_ del turno (1- jugador, 0-pc)
    """
    casilla = get_xy_tiro(turno)
    if type(tablero_tiros) is np.ndarray:
        turno, tablero = disparar(turno, casilla, barcos, tablero, tablero_tiros)
        print("191 turno ------------------", turno) if DEBUG_MODE else None
        if ( modalidad_juego == False):  # and turno (se cambia en disparar por lo tanto aqui no me sirve)
            print("Tablero de tiros:")
            pretty_tablero(tablero_tiros)
    else:
        turno, tablero = disparar(turno, casilla, barcos, tablero)
        print("Tablero del", "JUGADOR" if turno else "PC" )
        pretty_tablero(tablero)
    return turno

def init_juego():
    """
    Método principal del juego. Flujo principal:
        Crear tableros.
        Colocar barcos.
        Logica de turnos.
        Fin de juego.
    """
    # 1 si es JUGADOR / 0 PC
    turno = True

    run_ansi_codes_4_colors()
    clear_console()

    print(emoji.emojize(TITLE))
    print("=" * 60)

    """
    Init tableros
    """
    tablero_jugador = crear_tablero()
    tablero_jugador_tiros = crear_tablero()
    tablero_pc = crear_tablero()

    modalidad_juego = eleccion_tipo_juego()
    print('modalidad_juego', modalidad_juego) if DEBUG_MODE else None
    esloras = ESLORAS_6_BARCOS if modalidad_juego else ESLORAS_2_BARCOS
    barcos_jugador = generar_barcos(esloras)
    barcos_jugador_cpy = barcos_jugador.copy()
    # tablero_jugador = colocar_barcos(tablero_jugador, generar_barcos(esloras))
    tablero_jugador = colocar_barcos(tablero_jugador, barcos_jugador)
    print(colored("Tablero del Jugador con barcos cargados:", "blue"))
    pretty_tablero(tablero_jugador)

    tablero_pc = crear_tablero()
    # tablero_pc = colocar_barcos(tablero_pc, barcos_pc)
    barcos_pc = generar_barcos(esloras)
    barcos_pc_cpy = barcos_pc.copy()
    tablero_pc = colocar_barcos(tablero_pc, barcos_pc)
    print(colored("Tablero del PC con barcos cargados:","green"))
    pretty_tablero(tablero_pc)

    while True:                                                    # Mientras haya acertado el disparo
        print("El turno es del:", "JUGADOR" if turno else "PC")
        if turno:
            turno = ejecutar_turno(modalidad_juego, turno, tablero_pc, barcos_pc_cpy, tablero_jugador_tiros)
            if hay_ganador(barcos_pc_cpy, MSG_GANARDOR):
                break
        else:
            # turno PC
            turno = ejecutar_turno(modalidad_juego, turno, tablero_jugador, barcos_jugador_cpy)
            if hay_ganador(barcos_pc_cpy, MSG_PERDEDOR):
                break

def generar_barcos(esloras: list):
    """
    Genera una lista de barcos que no se solapen y cuyos valores no sean mayores de 10.
    """
    tablero = set()  # Usamos un conjunto para rastrear las posiciones ocupadas
    barcos = []

    for eslora in esloras:
        while True:
            # Generar orientación aleatoria
            orientacion = random.choice(["H", "V"])
            
            if orientacion == "H":  # Horizontal
                fila = random.randint(0, 9)
                col = random.randint(0, 10 - eslora)
                barco = [[fila, col + i] for i in range(eslora)]
            else:  # Vertical
                fila = random.randint(0, 10 - eslora)
                col = random.randint(0, 9)
                barco = [[fila + i, col] for i in range(eslora)]
            
            # Verificar que no se solapen
            if all(tuple(casilla) not in tablero for casilla in barco):
                barcos.append(barco)
                tablero.update(tuple(casilla) for casilla in barco)
                break

    return barcos

# def colocar_barco(barco, tablero):
#     for fila, col in barco:
#         tablero[fila, col] = 'O'