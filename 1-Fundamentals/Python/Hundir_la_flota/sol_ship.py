# ...existing code...

import random

def colocar_barcos(tablero):
    """
    Coloca 6 barcos en el tablero:
    - 3 barcos de eslora 2
    - 2 barcos de eslora 3
    - 1 barco de eslora 4
    """
    barcos = [2, 2, 2, 3, 3, 4]
    for eslora in barcos:
        while True:
            barco = crear_barco(eslora)
            if validar_barco(barco, tablero):
                colocar_barco(barco, tablero)
                break

def crear_barco(eslora):
    """
    Crea un barco de longitud `eslora` en posiciones aleatorias.
    """
    orientacion = random.choice(['H', 'V'])
    if orientacion == 'H':
        fila = random.randint(0, 9)
        col = random.randint(0, 10 - eslora)
        return [[fila, col + i] for i in range(eslora)]
    else:
        fila = random.randint(0, 10 - eslora)
        col = random.randint(0, 9)
        return [[fila + i, col] for i in range(eslora)]

def validar_barco(barco, tablero):
    """
    Verifica que el barco no se superponga con otros y esté dentro del tablero.
    """
    for fila, col in barco:
        if fila < 0 or fila >= 10 or col < 0 or col >= 10 or tablero[fila, col] != "_":
            return False
    return True

def main():
    """
    Flujo principal del juego.
    """
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()

    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_maquina)

    print("¡Comienza el juego!")
    # Implementar la lógica de turnos y disparos aquí...

# Ejecutar el flujo principal
if __name__ == "__main__":
    main()

# ----------------------------------------------
import numpy as np
import random
from utils import crear_tablero, colocar_barcos, disparar

def turno_jugador(tablero_rival):
    """
    Lógica del turno del jugador.
    """
    print("\nTu turno:")
    while True:
        try:
            fila = int(input("Introduce la fila (0-9): "))
            col = int(input("Introduce la columna (0-9): "))
            if 0 <= fila < 10 and 0 <= col < 10:
                resultado = disparar([fila, col], tablero_rival)
                print(f"Resultado: {resultado}")
                break
            else:
                print("Coordenadas fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Introduce números enteros.")
    return resultado

def turno_maquina(tablero_jugador):
    """
    Lógica del turno de la máquina.
    """
    print("\nTurno de la máquina:")
    while True:
        fila = random.randint(0, 9)
        col = random.randint(0, 9)
        if tablero_jugador[fila, col] not in ["X", "A"]:  # Evitar disparar en la misma casilla
            resultado = disparar([fila, col], tablero_jugador)
            print(f"La máquina disparó en ({fila}, {col}) y el resultado fue: {resultado}")
            break
    return resultado

def verificar_fin_juego(tablero):
    """
    Verifica si el juego ha terminado (si no quedan barcos en el tablero).
    """
    return "O" not in tablero

def main():
    """
    Flujo principal del juego.
    """
    # Crear tableros
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()

    # Colocar barcos
    print("Colocando barcos...")
    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_maquina)

    # Mostrar el tablero del jugador (sin mostrar el de la máquina)
    print("\nTu tablero:")
    print(tablero_jugador)

    # Turnos alternos
    turno_actual = "jugador"
    while True:
        if turno_actual == "jugador":
            resultado = turno_jugador(tablero_maquina)
            if verificar_fin_juego(tablero_maquina):
                print("\n¡Felicidades! Has ganado.")
                break
            if resultado == "Agua":
                turno_actual = "maquina"
        else:
            resultado = turno_maquina(tablero_jugador)
            if verificar_fin_juego(tablero_jugador):
                print("\nLa máquina ha ganado. ¡Suerte la próxima vez!")
                break
            if resultado == "Agua":
                turno_actual = "jugador"

        # Mostrar tableros actualizados
        print("\nTu tablero:")
        print(tablero_jugador)
        print("\nTablero de la máquina (oculto):")
        print(np.where(tablero_maquina == "O", "_", tablero_maquina))  # Ocultar barcos de la máquina

if __name__ == "__main__":
    main()


    # _____________________________________

    import random

def generar_barcos():
    """
    Genera una lista de barcos que no se solapen y cuyos valores no sean mayores de 10.
    """
    tablero = set()  # Usamos un conjunto para rastrear las posiciones ocupadas
    barcos = []
    longitudes = [4, 3, 3, 2]  # Longitudes de los barcos

    for longitud in longitudes:
        while True:
            # Generar orientación aleatoria
            orientacion = random.choice(["H", "V"])
            
            if orientacion == "H":  # Horizontal
                fila = random.randint(0, 9)
                col = random.randint(0, 10 - longitud)
                barco = [[fila, col + i] for i in range(longitud)]
            else:  # Vertical
                fila = random.randint(0, 10 - longitud)
                col = random.randint(0, 9)
                barco = [[fila + i, col] for i in range(longitud)]
            
            # Verificar que no se solapen
            if all(tuple(casilla) not in tablero for casilla in barco):
                barcos.append(barco)
                tablero.update(tuple(casilla) for casilla in barco)
                break

    return barcos

# Generar barcos
barcos_jugador = generar_barcos()
print(barcos_jugador)


# ---------------------------------------------- OPT MAIN

from utils import *
from var import *
import emoji

# def verificar_ganador(barcos, mensaje_ganador):
#     if all(len(barco) == 0 for barco in barcos):
#         print(emoji.emojize(mensaje_ganador))
#         return True
#     return False

# def ejecutar_turno(turno, tablero, barcos, tablero_tiros=None):
#     casilla = get_xy_tiro(turno)
#     turno, tablero = disparar(turno, casilla, barcos, tablero, tablero_tiros)
#     pretty_tablero(tablero)
#     if tablero_tiros:
#         print("Tablero de tiros:")
#         pretty_tablero(tablero_tiros)
#     return turno

# Inicialización
clear_console()
print(emoji.emojize("======================================================== HUNDIR LA FLOTA :ship::bomb:"))

tablero_jugador = crear_tablero()
tablero_jugador_tiros = crear_tablero()
tablero_pc = crear_tablero()

tablero_jugador = colocar_barcos(tablero_jugador, barcos_jugador)
tablero_pc = colocar_barcos(tablero_pc, barcos_pc)

while True:
    clear_console()
    print("El turno es del:", "JUGADOR" if turno else "PC")
    
    if turno:
        turno = ejecutar_turno(turno, tablero_pc, barcos_pc, tablero_jugador_tiros)
        if verificar_ganador(barcos_pc, "Felicidades, has ganado!:trophy:"):
            break
    else:
        turno = ejecutar_turno(turno, tablero_jugador, barcos_jugador)
        if verificar_ganador(barcos_jugador, "El PC ha ganado :crying_face:. ¡Suerte la próxima vez!"):
            break
