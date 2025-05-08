from utils import *
from vars import *
import emoji

# 1 si es jugador / 0 PC
turno = True
barcos_pc_cpy = barcos_pc.copy()
barcos_jugador_cpy = barcos_jugador.copy()

"""
Init tableros
"""
clear_console()
print(emoji.emojize(TITLE))
print("=" * 50)

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

while True:                                                    # Mientras haya acertado el disparo
    print("El turno es del:", "JUGADOR" if turno else "PC")
    if turno:
        turno = ejecutar_turno(turno, tablero_pc, barcos_pc_cpy, tablero_jugador_tiros)
        if hay_ganador(barcos_pc_cpy, MSG_GANARDOR):
            break
    else:
        # turno PC
        turno = ejecutar_turno(turno, tablero_jugador, barcos_jugador_cpy)
        if hay_ganador(barcos_pc_cpy, MSG_PERDEDOR):
            break