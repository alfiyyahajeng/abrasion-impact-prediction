import streamlit as st
import predict1
import predict2
import pandas as pd

def main():
    st.title('Aplikasi Prediksi Dampak Abrasi: Luasan dan Populasi Terpapar')
    st.write('Aplikasi ini memanfaatkan teknologi pembelajaran mesin untuk memprediksi persentase luasan wilayah dan jumlah penduduk yang terpapar bencana abrasi. Dengan memasukkan data geografis dan demografis, aplikasi ini memberikan proyeksi untuk membantu pengambilan keputusan terkait mitigasi bencana dan perencanaan wilayah pesisir.')
    menu = ['Home','Predict']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.title('Selamat Datang di Aplikasi Prediksi Bencana Abrasi')
    else :
        st.title('Prediksi Presentase Luasan & Penduduk Terpapar Bencana Abrasi di Kabupaten Sambas')

        jarak = st.number_input(label='Jarak ke Ibu Kota Kabupaten (km)', value=0, min_value=0)
        jumlah_p = st.number_input('Jumlah Penduduk', value=0, min_value=0)
        padat_p = st.number_input('Kepadatan Penduduk', value=0, min_value=0)
        perempuan = st.number_input('Jumlah Penduduk Perempuan', value=0, min_value=0)
        lansia = st.number_input('Jumlah Usia Lansia (60 ke atas)', value=0, min_value=0)
        anak = st.number_input('Jumlah Penduduk Usia Anak (0-14 tahun)', value=0, min_value=0)
        hamil = st.number_input('Jumlah Penduduk Ibu Hamil', value=0, min_value=0)
        pendidikan = st.number_input('Jumlah Penduduk SMA/sederajat', value=0, min_value=0)
        luas = st.number_input('Luas Wilayah (Ha)', value=0, min_value=0)

        input_data = pd.DataFrame({
        'Jarak ke Ibu Kota Kabupaten (km)' : [jarak],
        'Jumlah Penduduk' : [jumlah_p],
        'Kepadatan Penduduk': [padat_p],
        'Perempuan': [perempuan],
        'Usia Lansia (60 ke atas)': [lansia],
        'Usia Anak (0-14 tahun)': [anak],
        'Ibu Hamil': [hamil],
        'Tingkat Pendidikan (SMA/sederajat)': [pendidikan],
        'Luas Wilayah (Ha)': [luas]
        })
        if st.button('Prediksi'):
            predict1.predict1_data(input_data)
            predict2.predict2_data(input_data)

if __name__ == '__main__':
    main()
