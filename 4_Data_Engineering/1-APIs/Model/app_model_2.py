from flask import Flask, request, jsonify
import os
import pickle
# from sklearn.model_selection import cross_val_score
# import pandas as pd

# 1. Endpoint que devuelva la predicción de los nuevos datos enviados mediante argumentos en la llamada

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def main():
    return 'API del modelo'

@app.route("/prediccion")
def prediccion():
    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)

    modelo = pickle.load(open("data/advertising_model.pkl", "rb"))
    prediccion = modelo.predict([[int(tv), int(radio), int(newspaper)]])

    return f"la prediccion es: {round(prediccion[0], 2)}"
# http://127.0.0.1:5000/prediccion?tv=30&radio=40&newspaper=50

@app.route('/prediccion_2/<int:tv>/<int:radio>/<int:newspaper>')
def prediccion_2(tv, radio, newspaper):
    modelo = pickle.load(open("data/advertising_model.pkl", "rb"))
    pred_2 = modelo.predict([[int(tv), int(radio), int(newspaper)]])
    return f"la prediccion es: {round(pred_2[0], 2)}"


@app.route('/prediccion_3')
def prediccion_3():
    data = request.get_json()
    modelo = pickle.load(open("data/advertising_model.pkl", "rb"))
    pred_2 = modelo.predict([[data['tv'], data['radio'], data['newspaper']]])
    return f"la prediccion es: {round(pred_2[0], 2)}"

"""
    [50, 60, 70]

    {
        "tv": 50,
        "radio": 60,
        "newspaper": 70
    }
"""

app.run()
