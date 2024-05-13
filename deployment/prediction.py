import pandas as pd
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

def app():
    st.title('Prediksi Feeling mu hari ini ')

    model = load_model('model_lstm_best.keras')

    # Input form
    with st.form ('Prediksi emotion kamu berdasarkan curhatmu'):
        kalimat = st.text_input('Masukkan curhatanmu(dalam bahasa inggris ya :)')
        sub= st.form_submit_button('Submit Data')

        # Jika tombol Submit ditekan
        if sub:
            # Membuat data input
            data_inf = {
                'text': [kalimat],
            }
            df = pd.DataFrame(data_inf)

            # Memprediksi menggunakan model
            prediksi = model.predict(df)
            pred_inf=np.where(prediksi >= 0.5, 1, 0)
            labels = ['Sadness', 'Joy', 'Love', 'Anger', 'Fear', 'Surprise']
            hasil = ""
            for i in range(len(pred_inf[0])):
                if pred_inf[0][i] == 1:
                    hasil = labels[i]

            st.write('Feelingmu hari ini adalah',hasil)
if __name__ == "__main__":
    app()
