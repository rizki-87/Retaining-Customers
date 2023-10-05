import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')
#Memanggil data csv 
    df1 = pd.read_csv('Customer-Churn.csv')
    

#menampilakn 5 data teratas
    st.table(df1.head(5))


    # Visualisasi StreamingTV dan StreamingMovies
    # Menghitung jumlah pelanggan yang menggunakan StreamingTV dan StreamingMovies
    streaming_tv_counts = df1['StreamingTV'].value_counts()
    streaming_movies_counts = df1['StreamingMovies'].value_counts()

    # Membuat visualisasi
    st.title('Visualisasi StreamingTV dan StreamingMovies')

    # Diagram batang StreamingTV
    st.subheader('StreamingTV')
    fig1, ax1 = plt.subplots()
    ax1.bar(streaming_tv_counts.index, streaming_tv_counts.values, color='skyblue')
    ax1.set_title('StreamingTV')
    ax1.set_xlabel('Status StreamingTV')
    ax1.set_ylabel('Jumlah Pelanggan')

    # Diagram batang StreamingMovies
    st.subheader('StreamingMovies')
    fig2, ax2 = plt.subplots()
    ax2.bar(streaming_movies_counts.index, streaming_movies_counts.values, color='lightcoral')
    ax2.set_title('StreamingMovies')
    ax2.set_xlabel('Status StreamingMovies')
    ax2.set_ylabel('Jumlah Pelanggan')

    st.pyplot(fig1)
    st.pyplot(fig2)

    # Menghitung jumlah nilai unik di kolom StreamingTV
    streaming_tv_counts = df1['StreamingTV'].value_counts()

    # Menghitung jumlah nilai unik di kolom StreamingMovies
    streaming_movies_counts = df1['StreamingMovies'].value_counts()

    # Menampilkan hasil
    st.subheader('Distribusi Pelanggan di layanan Streaming TV:')
    st.write("Berlangganan:", streaming_tv_counts['Yes'])
    st.write("Tidak Berlangganan:", streaming_tv_counts['No'])
    st.write("Tidak Ada Internet:", streaming_tv_counts['No internet service'])

    st.subheader('Distribusi Pelanggan di Layanan Streaming Movies:')
    st.write("Berlangganan:", streaming_movies_counts['Yes'])
    st.write("Tidak Berlangganan:", streaming_movies_counts['No'])
    st.write("Tidak Ada Internet:", streaming_movies_counts['No internet service'])

    #menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Terdapat potensi penambahan revenue dari 2810 orang yang belum berlangganan Streaming TV dan 2785 orang yang belum berlanggan Streaming Movies. Strategi marketing/promo bisa segera dibuat untuk akuisisi tersebut diatas.')


    # Distribusi Gender
    # Tampilkan judul aplikasi
    st.title('Distribusi Gender')

    # Buat visualisasi dengan seaborn
    fig, ax = plt.subplots()
    sns.countplot(data=df1, x='gender', palette="Set1", ax=ax)
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.title("Distribusi Gender")
    st.pyplot(fig)

    # Hitung dan tampilkan distribusi gender
    gender_counts = df1['gender'].value_counts()
    st.subheader('Distribusi Gender:')
    st.write(gender_counts)
    
    #menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Jumlah customer laki-laki sejumlah 3555 orang, lebih banyak dari customer perempuan sebanyak 3488 orang.')





    # Hitung distribusi Payment Method
    payment_method_counts = df1['PaymentMethod'].value_counts()

    # Tampilkan judul aplikasi
    st.title('Distribusi Payment Method')

    # Visualisasi lingkaran
    st.subheader('Visualisasi: Distribusi Payment Method')
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(payment_method_counts.values, labels=payment_method_counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title("Distribusi Payment Method")
    ax.axis('equal')
    st.pyplot(fig)

    # Tampilkan hasil distribusi Payment Method
    st.subheader('Distribusi Metode Pembayaran:')
    st.write(payment_method_counts)

    # Distribusi Jenis Kontrak
    # Hitung distribusi jenis kontrak
    contract_counts = df1['Contract'].value_counts()

    # Tampilkan judul aplikasi
    st.title('Distribusi Jenis Kontrak')
#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Cek elektronik merupakan metode pembayaran yang paling banyak digunakan oleh customer untuk membayar tagihan. Untuk menjaga kontinuitas pembayaran tagihan, jumlah customer yang membayar menggunakan autodebet, baik kredit maupun kredit perlu ditingkatkan. Fitur auotdebet mengautomasi pembayaran tagihan, meminimalisir resiko telat membayar tagihan.')


    

    # Visualisasi bar horizontal
    st.subheader('Visualisasi: Distribusi Jenis Kontrak')
    fig, ax = plt.subplots()
    sns.set(style="whitegrid")
    sns.barplot(x=contract_counts.values, y=contract_counts.index, palette='Set2')
    plt.xlabel("Count")
    plt.ylabel("Contract Type")
    plt.title("Distribusi Jenis Kontrak")
    plt.tight_layout()
    st.pyplot(fig)

    # Tampilkan hasil distribusi jenis kontrak
    st.subheader('Distribusi Jenis Kontrak:')
    st.write(contract_counts)
#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Customer yang membayar tagihan per bulan merupakan yang paling banyak. Untuk menjaga loyalitas customer, pembayaran tagihan langsung untuk 1 tahun dan 2 tahun harus ditingkatkan, dengan cara , misal : memberikan potongan harga kepada customer yang langsung membayar tagihan selama satu tahun/ lebih.')



    # Loyalitas Pelanggan
    # Distribusi Loyalitas Pelanggan
    churn_counts = df1['Churn'].value_counts()

    # Membuat plot diagram lingkaran
    plt.figure(figsize=(6, 4))
    sns.set(style="whitegrid")
    sns.countplot(data=df1, x='Churn', palette='Set2')
    plt.xlabel("Churn")
    plt.ylabel("Count")
    plt.title("Distribusi Churn")
    plt.show()
    print()
    print('Distribusi Loyalitas Pelanggan:')
    print(churn_counts)

#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Customer yang loyal jauh lebih banyak dari customer yang berhenti berlangganan. Pola perilaku mereka lah yang akan di pelajari oleh model yang akan dibuat. Agar calon customer yang memiliki trait yang sama, mendapat treatment yang seharusnya.')


        
