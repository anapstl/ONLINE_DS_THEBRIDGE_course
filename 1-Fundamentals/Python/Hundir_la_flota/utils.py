import numpy as np
import os

def clear_console():
    clear = lambda: os.system('cls')
    clear()

def print_tablero(tablero):
    """
    Imprime tablero.
    """
    for tb in tablero:
        print(*tb)

def crear_tablero(tamaño=10):
    """
    Crea un tablero de tamaño `tamaño x tamaño` relleno con '_'. 
    Valor por defecto 10. 
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

def disparar(casilla, tablero, barcos):
    print("-------------casilla", casilla)

    for barco in barcos:
        print(barco)
        if casilla in barco:
            print('touche')
            # pintarlo con "X"
            tablero[casilla[0], casilla[1]] = "X"
            barco.remove(casilla)
            return True, tablero
        else:
            # agua
            print("agua")
            tablero[casilla[0], casilla[1]] = "A"
            print("disparar, cambio de turno")
            return False, tablero

def dispara_random():
    pass

# def crear_tablero(tamanio):
#     pass

# def colocar_barcos(barco, tablero):
#     pass


# def crear_barco(eslora):
#     pass