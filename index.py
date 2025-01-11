import pickle
import streamlit as st
import numpy as np
import pandas
import sklearn


diabetes_model = pickle.load(open("C:\\Users\\Hp\\OneDrive\\Desktop\\mini_project\\Multiple-Disease-Prediction-System\diabetes_prediction_model.sav", "rb"))
HeartDisease_model = pickle.load(open("C:\\Users\\Hp\\OneDrive\\Desktop\\mini_project\\Multiple-Disease-Prediction-System\heart_model (1).sav", "rb"))
parkinsons_model = pickle.load(
    open("C:\\Users\\Hp\\OneDrive\\Desktop\\mini_project\\Multiple-Disease-Prediction-System\\Parkison's_disease_prediction_model.sav", 'rb'))


with st.sidebar:
    selected = st.selectbox("Multiple Disease Prediction System",
                            ["Heart Disease Prediction", "Diabetes Prediction", "Parkinson's Disease Prediction"])


if selected == "Heart Disease Prediction":
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age',min_value=0,step=1)
    with col2:
        sex = st.number_input('Sex',min_value=0,step=1)
    with col3:
        cp = st.number_input('Chest Pain types',min_value=0,step=1)
    with col1:
        trestbps = st.number_input('Resting Blood Pressure',min_value=0,step=1)
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',min_value=0,step=1)
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl',min_value=0,step=1)
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results',min_value=0,step=1)
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',min_value=0,step=1)
    with col3:
        exang = st.number_input('Exercise Induced Angina',min_value=0,step=1)
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',min_value=0,step=1)
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy',min_value=0,step=1)
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',min_value=0,step=1)

    heart_diagnosis = ''

    
    if st.button('Heart Disease Test Result'):
        heart_prediction = HeartDisease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


if selected == "Diabetes Prediction":
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies',min_value=0,step=1)
    with col2:
        Glucose = st.number_input('Glucose Level',min_value=0,step=1)
    with col3:
        BloodPressure = st.number_input('Blood Pressure value',min_value=0,step=1)
    with col1:
        SkinThickness = st.number_input('Skin Thickness value',min_value=0,step=1)
    with col2:
        Insulin = st.number_input('Insulin Level',min_value=0,step=1)
    with col3:
        BMI = st.number_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.number_input('Age of the Person',min_value=0,step=1)

    
    diab_diagnosis = ''

    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


if selected == "Parkinson's Disease Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')
    with col1:
        Jitter_percent = st.number_input('MDVP:Jitter(%)')
    with col2:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')
    with col3:
        RAP = st.number_input('MDVP:RAP')
    with col1:
        PPQ = st.number_input('MDVP:PPQ')
    with col2:
        DDP = st.number_input('Jitter:DDP')
    with col3:
        Shimmer = st.number_input('MDVP:Shimmer')
    with col1:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
    with col2:
        APQ3 = st.number_input('Shimmer:APQ3')
    with col3:
        APQ5 = st.number_input('Shimmer:APQ5')
    with col1:
        APQ = st.number_input('MDVP:APQ')
    with col2:
        DDA = st.number_input('Shimmer:DDA')
    with col3:
        NHR = st.number_input('NHR')
    with col1:
        HNR = st.number_input('HNR')
    with col2:
        RPDE = st.number_input('RPDE')
    with col3:
        DFA = st.number_input('DFA')
    with col1:
        spread1 = st.number_input('spread1')
    with col2:
        spread2 = st.number_input('spread2')
    with col3:
        D2 = st.number_input('D2')
    with col1:
        PPE = st.number_input('PPE')

   
    parkinsons_diagnosis = ''

    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                           Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                           DFA, spread1, spread2, D2, PPE]])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
