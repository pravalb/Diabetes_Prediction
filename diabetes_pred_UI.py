# -*- coding: utf-8 -*-

!pip install streamlit
import streamlit as st

import pickle

import numpy as np


# model = pickle.load (open('model.pkl','rb'))


def main():
    st.title("ADBMS FINAL PROJECT")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">DIABETES PREDICTION APPLICATION </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    hbp = st.radio("HIGH BLOOD PRESSURE", ('Yes','No'))
    hchol = st.selectbox("HIGH CHOLESTROL", ('Yes','No'))
    BMI = st.text_input("BMI", "Enter Value between 0-98")
    SMOKER = st.selectbox("SMOKER", ('Yes','No'))
    STROKE = st.selectbox("STROKE", ('Yes','No'))
    heart = st.selectbox("HEART DISEASE OR ATTACK", ('Yes','No'))
    phyact = st.selectbox("PHYSICAL ACTIVITY", ('Yes','No'))
    heavyal = st.selectbox("HEAVY ALCOHOL CONSUMPTION", ('Yes','No'))
    genhlth = st.selectbox("GENERAL HEALTH", ('Yes','No'))
    AGE = st.text_input("Age","Enter Age")

    #

    if st.button("Predict"):
        output = predict_forest(oxygen, humidity, temperature)
        st.success('The probability of diabetes is {}'.format(output))

    # if output > 0.5:
    #    st.markdown(danger_html,unsafe_allow_html=True)
    # else:
    #   st.markdown(safe_html,unsafe_allow_html=True)


if __name__ == '__main__':
    main()

from google.colab import drive

drive.mount('/content/drive')

!streamlit run diabetes_pred_UI.py



