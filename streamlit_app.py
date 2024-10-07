import streamlit as st
import pandas as pd
import numpy as np

# Judul aplikasi
st.title("Menggunakan Obrolan di Streamlit")
st.write("Saya menggunakan Streamlit untuk menampilkan grafik")

# Menggunakan st.file_uploader untuk upload file CSV
uploaded_file = st.file_uploader("Pilih file CSV untuk diunggah", type=["csv"])

# Cek apakah ada file yang diunggah
if uploaded_file is not None:
    # Membaca file CSV
    df_sales = pd.read_csv(uploaded_file, encoding="iso-8859-1")
    
    # Menampilkan informasi dasar tentang dataframe
    st.write("Statistik data:")
    st.write(df_sales.describe())
    
    # Mendapatkan unique product lines
    product_lines = df_sales["PRODUCTLINE"].unique()
    
    # Membuat DataFrame dengan ORDERDATE sebagai index dan product lines sebagai kolom
    df_productline_sales = df_sales.pivot_table(values='QUANTITYORDERED', index='ORDERDATE', columns='PRODUCTLINE', fill_value=0)
    
    # Membuat Area Chart
    st.title("Area Chart")
    st.area_chart(df_productline_sales)
    
    # Membuat Line Chart
    st.title("Line Chart")
    st.line_chart(df_productline_sales)
    
    # Membuat Bar Chart
    st.title("Bar Chart")
    st.bar_chart(df_productline_sales)
    
else:
    st.write("Silakan unggah file CSV untuk melihat isi dan statistiknya.")

# Tambahkan footer atau pemisah
st.markdown("---")
