import streamlit as st 
import pandas as pd 
import pickle as pk 

st.set_page_config(
    page_title="Loan Prediction App",
    page_icon="🏦",
    layout="centered"
)
 
model=pk.load(open('model.pkl','rb')) 
scaler=pk.load(open('scaler.pkl','rb')) 

 
st.header('Heart_Disease_Prediction_app')
Age = st.slider('Choose Your Age', 0, 100) 
Sex= st.selectbox('Choose your Sex',['Male','Female']) 
Chest_pain_type = st.slider('Choose Your Chest pain type', 1, 4)  
BP = st.slider('Choose Your BP level', 0, 200)
Cholesterol = st.slider('Choose Your Cholesterol level', 0, 600)
FBS_over_120= st.selectbox('Choose your FBS over 120',['Yes','No']) 
EKG_results = st.slider('Choose Your EKG results', 0, 2)
Max_HR = st.slider('Choose Your Max HR level', 0, 250)
Exercise_angina= st.selectbox('Choose your Exercise angina',['Yes','No']) 
ST_depression = st.slider('Choose Your ST depression',min_value=0.0, max_value=6.7, value=0.0, step=0.1,format="%.1f")
Slope_of_ST = st.slider('Choose Your Slope of ST', 0,3)
Number_of_vessels_fluro = st.slider('Choose Your Number of vessels fluro', 0, 3)
Thallium = st.select_slider('Choose Your Thallium level', options=[3, 6, 7])


if Sex =='Male': 
    sex = 0
else: 
    sex = 1
 
if FBS_over_120 =='Yes': 
    FBS =1
else: 
    FBS = 0

if Exercise_angina =='Yes': 
    Ea =1
else: 
    Ea = 0

 
if st.button("Predict"): 
    pred_data =pd.DataFrame([[Age,sex,Chest_pain_type,BP,Cholesterol,FBS,EKG_results,Max_HR,Ea,ST_depression,Slope_of_ST,Number_of_vessels_fluro,Thallium]],columns=['Age','Sex','Chest pain type','BP','Cholesterol','FBS over 120','EKG results','Max HR','Exercise angina','ST depression','Slope of ST','Number of vessels fluro','Thallium']) 
    pred_data = scaler.transform(pred_data) 
    predict = model.predict(pred_data)
    if predict[0] == 1: 
        st.error('Warning: Heart Disease Detected') 
    else: 
        st.success('Results: No Heart Disease Detected')