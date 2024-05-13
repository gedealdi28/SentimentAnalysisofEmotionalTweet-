# Contents of main.py
import eda
import prediction
import streamlit as st

PAGES = {
    "EDA": eda,
    "Model Prediction": prediction
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()