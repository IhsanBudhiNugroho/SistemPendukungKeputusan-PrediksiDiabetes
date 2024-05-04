import pickle
import streamlit as st

# Membaca model
try:
    diabetes_model = pickle.load(open('random_forest_model.sav', 'rb'))
    st.success("Model berhasil dimuat.")
except Exception as e:
    st.error("Gagal memuat model:", e)

# Judul web
st.title('Prediksi Penyakit Diabetes')

# Membagi kolom
col1, col2 = st.columns(2)

# Input nilai untuk setiap fitur
with col1:
    Pregnancies = st.text_input('Pregnancies', type='number')
    Glucose = st.text_input('Glucose', type='number')
    BloodPressure = st.text_input('Blood Pressure', type='number')
    SkinThickness = st.text_input('Skin Thickness', type='number')

with col2:
    Insulin = st.text_input('Insulin', type='number')
    BMI = st.text_input('BMI', type='number')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function', type='number')
    Age = st.text_input('Age', type='number')

# Kode untuk prediksi
diab_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    # Memastikan semua input adalah numerik
    if not all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
        st.error("Mohon isi semua kolom dengan angka.")
    else:
        # Melakukan prediksi
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        # Menampilkan hasil prediksi
        if diab_prediction[0] == 1:
            st.success('Pasien terkena Diabetes.')
        else:
            st.success('Pasien tidak terkena Diabetes.')
