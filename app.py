import streamlit as st
import joblib
import numpy as np

# Memuat model regresi linear yang sudah disimpan
lin_reg_loaded = joblib.load ('lin_reg_model.joblib')

# Judul aplikasi
st.title("prediksi Gaji Berdasarkan Lama Bekerja")

# Input tahun pengalaman kerja
years_experience = st.number_input("Masukan jumlah tahun bekerja:", min_value=0.0, step=0.1)

# Prediksi gaji
if st.button("Prediksi Gaji")
  gaji = lin_reg_loaded.predict([[years_experience]])
  st.write(f"Gaji seseorang setelah bekerja selama {years_experience} tahun adalah ${gaji[0]:,.2f})
