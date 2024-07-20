import sklearn
import pickle
import streamlit as st

model = pickle.load(open('prediksi_mobil.sav', 'rb'))

st.title('Prediksi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input EngineSize Mobil')

predict = ''

if st.button('Prediksi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('Prediksi Harga Mobil Bekas Dalam Ponds :', predict)
    st.write('Prediksi Harga Mobil Bekas Dalam IDR (Juta):', predict*19000)