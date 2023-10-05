import streamlit as st
import pandas as pd
import pickle
import ast
from PIL import Image
import webbrowser

def run():
# Load All Files

    with open('all_process_rizki.pkl', 'rb') as file_1:
        all_process = pickle.load(file_1)


    tenure = st.number_input(label='periode menjadi customer',min_value=1,max_value=72)
    MonthlyCharges = st.number_input(label='jumlah tagihan per bulan',min_value=19,max_value=72)
    Contract = st.selectbox(label='Pilihan Kontrak yang Dipilih Customer',options=[0, 1, 2])
    st.caption('Nilai 0: Month-to-month ,Nilai 1: One year, Nilai 2: Two year')
    OnlineSecurity = st.selectbox(label='Perlindungan dari Malware, Virus, Serangan Hacker, dan Sejenisnya',options=[0, 1, 2])
    st.caption('0: No, 1: No internet service, 2: Yes')
    TechSupport = st.selectbox(label='Layanan Dukungan Tekhnis',options=[0, 1, 2])
    st.caption('0: No, 1: No internet service, 2: Yes')
    PaymentMethod = st.selectbox(label='Metode Pembayaran',options=[0, 1, 2, 3])
    st.caption('0 : Electronic check, 1 : Mailed check, 2: Bank transfer (automatic), 3: Credit card (automatic)')
    InternetService = st.selectbox(label='Metode Pembayaran',options=[0, 1, 2])
    st.caption('0 : No, 1 : DSL, 2: Fiber optic')
    
    

    data_inf = pd.DataFrame({
        'tenure' : tenure,
        'MonthlyCharges' : MonthlyCharges,
        'Contract' : Contract,
        'OnlineSecurity' : OnlineSecurity ,
        'TechSupport' : TechSupport,
        'PaymentMethod' : PaymentMethod ,
        'InternetService' : InternetService,
        }, index =[0])

    st.table(data_inf)


    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        y_pred_inf = all_process.predict(data_inf)

        st.write(y_pred_inf[0])

        if y_pred_inf[0] == 0:
            st.write('Customer berhenti berlangganan/ tidak setia')
            

        else:
            st.write('Customer Setia')
            
