import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

st.title('Predecir el precio de tu coche!')
st.header('Introduce los siguientes valores:')

@st.cache_data
def cargar_marca_map():
    with open('marca_map.pkl', 'rb') as f:
        return pkl.load(f)

marca_map = cargar_marca_map()
@st.cache_data
def cargar_model_map():
    with open('model_map.pkl', 'rb') as f:
        return pkl.load(f)
model_map = cargar_model_map()
marca_seleccionada = st.selectbox('Marca:', options=list(marca_map.keys()))
modelo_seleccionado = st.selectbox('Modelo:', options=list(model_map.keys()))
p3 = int(st.number_input('Años antiguedad:'))
p4 = int(st.number_input('KM:'))
p5 = int(st.number_input('CV:'))
p6 = int(st.number_input('Cambio (1 = manual, 0 = automático):'))

@st.cache_data
def cargar_modelo():
    # with open('modelo_polynomial.pkl', 'rb') as f:
    with open('modelo_poly_ridge.pkl', 'rb') as f:
        modelo = pkl.load(f)
    return modelo

modelo = cargar_modelo()

# columnas = ['make_encoded', 'model_encoded', 'anios_antiguedad', 'kms', 'power', 'shift_encoded']
columnas = ['kms', 'power', 'make_encoded', 'model_encoded', 'shift_encoded',
       'anios_antiguedad']

if st.button('Predecir!'):
    make_encoded = marca_map[marca_seleccionada]
    model_encoded = model_map[modelo_seleccionado]

    entrada_dict = {
        'kms': [p4],
        'power': [p5],
        'make_encoded': [make_encoded],
        'model_encoded': [model_encoded],
        'shift_encoded': [p6],
        'anios_antiguedad': [p3]
    }


    entrada_df = pd.DataFrame(entrada_dict, columns=columnas)
    print(entrada_df.info())

    entrada_array = entrada_df.to_numpy()
    precio_predicho = modelo.predict(entrada_array)[0]

    st.success(f'El precio estimado de tu coche es: {precio_predicho:,.2f} €')
