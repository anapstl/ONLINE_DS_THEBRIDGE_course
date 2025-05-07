import numpy as np

def crear_tablero():
    tablero = np.full((10,10), "_")
    return tablero


# barco_1 = [[0,3], [0,4], [0,5], [0,6]]
# barco_jugador = [[[0,3], [0,4], [0,5], [0,6]], [[4,7], [5,7], [6,7]], [[8,8], [8,9]], [[1,7]]]

def colocar_barcos(tablero, barcos):
    for i in barcos:
        for j in i:
            # print(j)
            tablero[j[0], j[1]] = "O"
        
    return tablero

def disparo(tablero):
    fila = int(input("selecciona la fila:"))
    col = int(input("selecciona la col:"))
    if tablero[fila,col] == "O":
        tablero[fila,col] = "X"
        print("IMPACTO")
    elif tablero[fila, col] == "A" or tablero[fila, col] == "X":
        print("repetido")
        disparo()
    else: 
        tablero[fila,col] = "A"
        print("Falaste")

    return tablero