import streamlit as st
import eda
import model


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Rizki Pria Aditama')
    st.write('Batch     : HCK-007')
    st.write('Tujuan Milestone    :Untuk meminalisir salah prediksi, agar customer yang sebenarnya loyal, tidak diprediksi sebagai customer yang tidak loyal')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Saya adalah seorang data siencetist yang mendapat assigment Liverpool Telekomunikasi, untuk membuat model yang bisa meminimalisir salah prediksi, agar customer yang sebenarnya loyal, tidak dianggap/di prediksi sebagai customer yang tidak loyal.')

    with st.expander("Problem Statement"):
            st.caption('Problem Statement : Menurunkan presentase salah prediksi sebanyak 10 % , terhadap customer yang loyal agar tidak diprekdisi atau dianggap tidak loyal.')

    with st.expander("Kesimpulan"):
        st.caption('Problem stament bisa terpenuhi karena recall score untuk meminimalisir false negative bisa dilakukan sebesar 86%')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model .run()