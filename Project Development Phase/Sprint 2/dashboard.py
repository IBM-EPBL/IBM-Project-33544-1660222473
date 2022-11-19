import streamlit as st
import joblib
import pandas as pd
st.title("Heart Disease Prediction")
col1, col2, col3 = st.columns(3)



Age = col1.number_input("Enter your age")

chest_pain_type = col2.selectbox("Enter chest pain type?",["1","2","3","4"])

BP = col3.number_input("Enter BP level")

chol = col1.number_input("Enter cholestrol level")

maxhr = col2.number_input("Enter max heartrate")

exe_angina = col3.selectbox("Do you have exercise angina?",["Yes", "No"])

ST_depr = col1.number_input("Enter ST depression value")

ST_slope = col2.selectbox("Enter ST slope value",["1","2","3"])

no_of_vess = col3.selectbox("No of vessels of fluro",["0","1","2","3"])

thall = col2.number_input("Enter thallium level")

#st.button('Predict')


model = joblib.load('hdp_model.pkl')

df_pred = pd.DataFrame([[Age,chest_pain_type,BP,chol,maxhr,exe_angina,ST_depr,ST_slope,no_of_vess,thall]],columns= ['Age','Chest pain type','BP','Cholesterol','Max HR','Exercise angina','ST depression','Slope of ST','Number of vessels fluro','Thallium'])

df_pred['Exercise angina'] = df_pred['Exercise angina'].apply(lambda x: 1 if x == 'Yes' else 0)
        

model = joblib.load('hdp_model.pkl')
prediction = model.predict(df_pred)

if st.button('Predict', key = 0):
    if (df_pred['Age']>=120).bool() | (df_pred['Age']<1).bool()  | (df_pred['Cholesterol']<20).bool() | (df_pred['Cholesterol']>600).bool() | (df_pred['BP']>180).bool() | (df_pred['BP']>120).bool() | (df_pred['Max HR']>450).bool() | (df_pred['Max HR']<=0).bool() | (df_pred['Thallium']>8).bool() | (df_pred['Thallium']<0 ).bool() | (df_pred['ST depression']>6).bool() | (df_pred['ST depression']<0).bool():
        if (df_pred['Age']>=120).bool() | (df_pred['Age']<1).bool():
            st.write('<p class="big-font">Invalid AGE.. Please fill in appropriate data.</p>',unsafe_allow_html=True) 
        if (df_pred['Cholesterol']<20).bool() | (df_pred['Cholesterol']>600).bool():
            st.write('<p class="big-font">Extremely low or high cholestrol level.. Please fill in appropriate data.</p>',unsafe_allow_html=True)
        if (df_pred['BP']>180).bool() or (df_pred['BP']>120).bool():
            st.write('<p class="big-font">Blood pressure extremely high.. Contact medical professional immediately!</p>',unsafe_allow_html=True)
        if (df_pred['Max HR']>2000).bool() | (df_pred['Max HR']<=0).bool():
            st.write('<p class="big-font">Invalid max heartrate.. Please fill in appropriate data.</p>',unsafe_allow_html=True)
        if (df_pred['Thallium']>7).bool() | (df_pred['Thallium']<0).bool():
            st.write('<p class="big-font">Invalid Thallium value.. Please fill in appropriate data.</p>',unsafe_allow_html=True)
        if (df_pred['ST depression']>6).bool() | (df_pred['ST depression']<0).bool():
            st.write('<p class="big-font">Invalid ST depression value.. Please fill in appropriate data.</p>',unsafe_allow_html=True)
    elif(prediction[0]=='Absence'):
        st.title('Result, Heart Disease Absent')
    else:
        st.title('Result, Heart Disease Present')