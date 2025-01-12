import pickle
import streamlit as st
import pandas as pd
import math

#load model
with open('model2.pkl', 'rb') as fileP:
    loaded_model2 = pickle.load(fileP)

def predict2_data(input_data):
        pred_p = loaded_model2.predict(input_data)
        pred_roundedp = math.floor(pred_p)
        st.write(f'Prediksi Jumlah Penduduk Terpapar Terdampak Bencana Abrasi: {pred_roundedp} jiwa')

if __name__ == '__main__':
    predict2_data()