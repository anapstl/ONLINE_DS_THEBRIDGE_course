from utils import *
from var import *

clear_console()

tablero_j = crear_tablero()
print('---------------- Tablero jugador')
tablero_j_mod = colocar_barcos(tablero_j, barcos_jugador)
print(tablero_j_mod)

tablero_rv = crear_tablero()
print('---------------- Tablero rival')
tablero_rv_mod = colocar_barcos(tablero_rv, barcos_jugador)
print(tablero_rv_mod)

disparar([0, 2], tablero_j_mod)
print(tablero_j_mod)
