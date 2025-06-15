import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import time
import warnings
warnings.filterwarnings("ignore")


lista_alumnos = [("Leonardo S", 24, 1.82), 
                ("Piero T", 25, 1.71), 
                ("Marta B", 35, 1.66), 
                ("Silvia P", 37, 1.63), 
                ("Faro Z", 29, 1.90), 
                ("Miguel N", 27, 1.80), 
                ("Alejandro M", 28, 1.70), 
                ("Cristina M", 32, 1.60), 
                ("Francisco P", 36, 1.74), 
                ("Jorge D", 45, 1.72), 
                ("Jesús L", 41, 1.65), 
                ("Marta G", 30, 1.65), 
                ("Jennifer S", 40, 1.60), 
                ("Diego I", 39, 1.80), 
                ("Antonio C", 23, 1.77), 
                ("Juan M", 32, 1.75), 
                ("David S", 27, 1.70), 
                ("Antonio J", 34, 1.80), 
                ("Carlos H", 27, 1.77), 
                ("Erik U", 28, 1.70), 
                ("Marcos L", 35, 1.80)] 

df = pd.DataFrame(lista_alumnos, columns=['nombre', 'edad', 'altura_cm'])

X = df[['edad']]
y= df['altura_cm']

X_train, _, y_train, _ = train_test_split(X, y, test_size = 0.20, random_state = 10)

lm = LinearRegression()
lm.fit(X_train, y_train)

# cuando se trabaja con with lo cierra automa... no hace falta f.close()

with open("./model/model_lr.pkl", "wb") as f:
    pickle.dump(lm, f)

f.close()