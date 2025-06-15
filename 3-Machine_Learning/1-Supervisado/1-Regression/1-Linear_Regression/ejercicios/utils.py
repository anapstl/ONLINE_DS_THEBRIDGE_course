import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import time
import warnings
warnings.filterwarnings("ignore")

def load_and_LR(edad_user):

    with open('model/model_lr.pkl', 'rb') as f:
        lm = pickle.load(f) 
    
    f.close()

    edad_2_predict = [[edad_user]]
    altura_predicha = lm.predict(edad_2_predict)
    return altura_predicha

def adivinar():
    flag = False
    while not flag:    
        try:
            edad_user = int(input("Introduce tu edad: "))
            flag = True
            altura_predicha = load_and_LR(edad_user)

            print('🥁 Adivinando tu altura ', end='', flush=True)
            for i in range(1,6):
                time.sleep(2)
                print('.', end='', flush=True)
                time.sleep(2)
            print('🥁 y la altura es: ', end='', flush=True)
            print(round(altura_predicha[0], 2), 'cm')
            time.sleep(2)
        except ValueError:
            print('Entrada inválida. Introduce números enteros.')


# import time
# from utils import load_and_LR

# def animar_mensaje(mensaje, puntos=5, retraso=0.5):
#     print(mensaje, end='', flush=True)
#     for _ in range(puntos):
#         time.sleep(retraso)
#         print('.', end='', flush=True)
#     print()  # Salto de línea al final

# def pedir_edad():
#     while True:
#         try:
#             return int(input("Introduce tu edad: "))
#         except ValueError:
#             print("Entrada inválida. Por favor, introduce un número entero.")

# def adivinar():
#     edad_user = pedir_edad()
#     altura_predicha = load_and_LR(edad_user)

#     animar_mensaje("Adivinando tu altura", puntos=5, retraso=0.4)
#     time.sleep(0.5)
#     print(f"La altura predicha es: {round(altura_predicha[0], 2)} cm")
