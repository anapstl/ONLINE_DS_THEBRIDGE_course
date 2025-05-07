import utils
import variables as vr


tablero_rival_barcos = utils.crear_tablero()   # mostrar barcos del rival y los disparos del jugador
tablero_rival_disparos = utils.crear_tablero() # disparos del rival hacia mi

tablero_jugador_barcos = utils.crear_tablero() # mostrar barcos del jugador y los disparos del rivalos
tablero_jugador_disparos = utils.crear_tablero() # mis disparos hacia el rival

print("tablero donde se muestran los barcos dek rival y los disparo del jugador")
print(tablero_rival_barcos)



# tablero_rival = utils.crear_tablero()
# tablero_rival = utils.colocar_barcos(tablero_rival, vr.barcos_jugador)
# print("Tablero Rival")
# print(tablero_rival)

# print("_________________________")

# tablero_jugador = utils.crear_tablero()
# tablero_jugador = utils.colocar_barcos(tablero_jugador, vr.barcos_jugador)
# print("Tablero Jugador")
# print(tablero_jugador)

# tablero_jugador = utils.disparo(tablero_jugador)
# print(tablero_jugador)



