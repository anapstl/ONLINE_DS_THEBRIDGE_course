from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import pickle
import sqlite3
import pandas as pd

DB = "advertising.db"

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def main():
    return 'API del ejercicio Flask'

@app.route("/predict", methods=["GET"])
def prediccion():
    try:
        data = request.get_json()
        tv = float(data.get('tv'))
        radio = float(data.get('radio'))
        newspaper = float(data.get('newspaper'))
    except (TypeError, ValueError, AttributeError):
        return jsonify({"error": "Parámetros inválidos"}), 400

    modelo = pickle.load(open("./data/advertising_model.pkl", "rb"))
    pred = modelo.predict([[tv, radio, newspaper]])

    return jsonify({"prediction": round(pred[0], 2)})
# {"tv":100, "radio":200, "newspaper":300}


@app.route("/ingest", methods = ['POST'])
def insert_one():
    data = request.get_json()
    print('------------------------data----------------------',data)
    df = pd.DataFrame(data, columns=['tv', 'radio', 'newspaper', 'sales'])
    conn = sqlite3.connect(DB)
    df.to_sql('campañas', conn, if_exists='append', index=False)
    conn.close()
    return jsonify({"message": "Datos ingresados correctamente"}), 200
    
@app.route('/ingest_2', methods=['POST'])
def ingest_2():
    data = request.get_json()
    data = data.get("data", None)
    print('--------------------------------------', DB)
    con = sqlite3.connect(DB)
    cursor = con.cursor()
    q = 'INSERT INTO "campañas" VALUES(?, ?, ?, ?)'
    cursor.execute(q, data)
    con.commit()
    con.close()

    return "ok"
# {"data": [[100, 100, 200, 3000], [200, 230, 500, 4000]]}


# @app.route('/insert_many', methods=['POST'])
# def insert_many():
#     df = pd.read_csv('./data/campañas.csv', index_col=0)
#     conn = sqlite3.connect(DB)
#     df.to_sql('campañas', conn, if_exists='append', index=False)
#     conn.close()
#     return jsonify({"message": "Insert_multiple correctamente"}), 201

# @app.route('/retrain', methods=['POST'])
# def retrain_model():
#     modelo = pickle.load(open('./data/advertising_model.pkl', 'rb'))
#     conn = sqlite3.connect(DB)
#     df = pd.read_sql('SELECT * FROM campañas', conn)
#     X = df.iloc[:,:-1]
#     y= df['sales']
#     modelo.fit(X, y)
#     with open('Advertising_2.pkl', 'wb') as f:
#         pickle.dump(modelo, f)
#     return jsonify({'message': 'Modelo reentrenado correctamente.'}), 201

app.run()