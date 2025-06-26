# # -*- coding: utf-8 -*-
# """
# Created on Tue Mar 11 21:18:10 2025

# @author: Abhishek
# """

# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu
# from joblib import load


# #loading the saved models

# diabetes_model = pickle.load(open('C:/Users/om-31406/Desktop/Anshika/PROJECTS/HealthGuard/models/diabetes_model.sav', 'rb'))

# heart_disease_model = pickle.load(open('C:/Users/om-31406/Desktop/Anshika/PROJECTS/HealthGuard/models/heart_disease_model.sav', 'rb'))

# parkinsons_model = pickle.load(open('C:/Users/om-31406/Desktop/Anshika/PROJECTS/HealthGuard/models/parkinsons_model.sav', 'rb'))


# scaler1 = load('C:/Users/om-31406/Desktop/Anshika/PROJECTS/HealthGuard/models/std_scaler_diabetes.bin')

# scaler2 = load('C:/Users/om-31406/Desktop/Anshika/PROJECTS/HealthGuard/models/std_scaler_parkinsons.bin')


# #sidebar for navigate

# with st.sidebar:
#     selected = option_menu('Multiple Disease Prediction System', 
#                            ['Diabetes Prediction',
#                             'Heart Disease Prediction',
#                             'Parkinsons Prediction'],
#                            icons = ['activity', 'heart', 'person'],
#                            default_index = 0)
   
# if selected == 'Diabetes Prediction':
#     st.title('Diabetes Prediction System')
    
#     #getting the input data from the user
#     #columns
    
#     col1, col2, col3 = st.columns(3)
    
    
#     with col1:
#         Pregnancies = st.text_input('Number of Pregnancies')
#     with col2:
#         Glucose = st.text_input('Glucose Level')
#     with col3:
#         BloodPressure = st.text_input('Blood Pressure Value')
#     with col1:
#         SkinThickness = st.text_input('Skin Thickness value')
#     with col2:    
#         Insulin = st.text_input('Insulin Level')
#     with col3:    
#         BMI = st.text_input('BMI value')
#     with col1:    
#         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
#     with col2:
#         Age = st.text_input('Age of the person')
    
#     #code for Prediction
#     diab_diagnosis = ''
    
#     #creating a button for Prediction
    
#     if st.button('Diabetes Test Result'):
        
#         std_data = scaler1.transform([[Pregnancies, Glucose, BloodPressure
#                                          , SkinThickness, Insulin, BMI,
#                                          DiabetesPedigreeFunction, Age]])
#         diab_prediction = diabetes_model.predict(std_data)
        
#         if diab_prediction[0] == 0:
#            diab_diagnosis = 'The person is not Diabetic'
#         else:
#           diab_diagnosis = 'The person is Diabetic'
              
#         st.success(diab_diagnosis)
    
# if selected == 'Heart Disease Prediction':
#     st.title('Heart Disease Prediction System')
    
#     #getting the input data from the user
#     #columns
    
#     col1, col2, col3 = st.columns(3)
    
    
#     with col1:
#         Age = st.text_input('Age of the person')
#     with col2:
#         Sex = st.text_input('Sex of the person (1 = male; 0 = female)')
#     with col3:
#         cp = st.text_input('Chest Pain Types')
#     with col1:
#         rbp = st.text_input('Resting Blood Pressure')
#     with col2:    
#         sc = st.text_input('Serum Cholestrol in mg/dl')
#     with col3:    
#         fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')
#     with col1:    
#         restecg = st.text_input('Resting ElectroCardiographic Results')
#     with col2:
#         thalach = st.text_input('Maximum Heart Rate achieved')
#     with col3:
#         exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
#     with col1:
#         oldpeak = st.text_input('ST depression induced by exercise')
#     with col2:
#         slope = st.text_input('Slope of the peak exercise ST segment')
#     with col3:
#         ca = st.text_input('Major vessels colored by flouroscopy')
#     with col1:
#         thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
        
#     Age = float(Age) if Age else 0.0
#     Sex = int(Sex) if Sex else 0  # assuming Sex is an integer
#     cp = int(cp) if cp else 0
#     rbp = float(rbp) if rbp else 0.0
#     sc = float(sc) if sc else 0.0
#     fbs = int(fbs) if fbs else 0
#     restecg = int(restecg) if restecg else 0
#     thalach = float(thalach) if thalach else 0.0
#     exang = int(exang) if exang else 0
#     oldpeak = float(oldpeak) if oldpeak else 0.0
#     slope = int(slope) if slope else 0
#     ca = int(ca) if ca else 0
#     thal = int(thal) if thal else 0
    
#     #code for Prediction
#     heart_diagnosis = ''
    
#     #creating a button for Prediction
    
#     if st.button('Heart Disease Test Result'):
        
#         heart_prediction = heart_disease_model.predict([[Age, Sex, cp
#                                          , rbp, sc, fbs,
#                                          restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
#         if heart_prediction[0] == 0:
#            heart_diagnosis = 'The person does not have a Heart Disease'
#         else:
#           heart_diagnosis = 'The person has a Heart Disease'
              
#         st.success(heart_diagnosis)
    
# if selected == 'Parkinsons Prediction':
#     st.title('Parkinsons Prediction System')
    
#     #getting the input data from the user
#     #columns
    
#     col1, col2, col3, col4, col5 = st.columns(5)
    
    
#     with col1:
#         fo = st.text_input('MDVP:Fo(Hz)')
#     with col2:
#         fhi = st.text_input('MDVP:Fhi(Hz)')
#     with col3:
#         flo = st.text_input('MDVP:Flo(Hz)')
#     with col4:
#         jitter_percent = st.text_input('MDVP:Jitter(%)')
#     with col5:
#         jitter_abs = st.text_input('MDVP:Jitter(Abs)')
#     with col1:
#         RAP = st.text_input('MDVP:RAP')
#     with col2:
#         PPQ = st.text_input('MDVP:PPQ')
#     with col3:
#         DDP = st.text_input('MDVP:DDP')
#     with col4:
#         shimmer = st.text_input('MDVP:Shimmer')
#     with col5:
#         shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
#     with col1:
#         APQ3 = st.text_input('Shimmer:APQ3')
#     with col2:
#         APQ5 = st.text_input('Shimmer:APQ5')
#     with col3:
#         APQ = st.text_input('MDVP:APQ')
#     with col4:
#         DDA = st.text_input('Shimmer:DDA')
#     with col5:
#         NHR = st.text_input('NHR')
#     with col1:
#         HNR = st.text_input('HNR')
#     with col2:
#         RPDE = st.text_input('RPDE')
#     with col3:
#         DFA = st.text_input('DFA')
#     with col4:
#         spread1 = st.text_input('Spread 1')
#     with col5:
#         spread2 = st.text_input('Spread 2')
#     with col1:
#         D2 = st.text_input('D2')
#     with col2:
#         PPE = st.text_input('PPE')
        
        
    
    
#     #code for Prediction
#     parkinsons_diagnosis = ''
    
#     #creating a button for Prediction
    
#     if st.button('Parkinsons Test Result'):
        
#         std_data = scaler2.transform([[fo, fhi, flo, jitter_percent, jitter_abs,
#                       RAP, PPQ, DDP,shimmer, shimmer_dB, APQ3, APQ5,
#                       APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
#         parkinsons_prediction = parkinsons_model.predict(std_data)
        
#         if parkinsons_prediction[0] == 0:
#            parkinsons_diagnosis = "The person does not have Parkinson's Disease"
#         else:
#           parkinsons_diagnosis = "The person has Parkinson's Disease"
              
#         st.success(parkinsons_diagnosis)















    
    
    
    
    
    
    
    
    
    
    
    
    
import streamlit as st
from streamlit_option_menu import option_menu

# --- Set page config ---
st.set_page_config(page_title="HealthGuard+", page_icon="🩺", layout="wide")

# --- Top navbar ---
selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Diseases"],
    icons=["house", "info-circle", "heart-pulse"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding": "0!important", "background-color": "#f9f9f9"},
        "icon": {"color": "blue", "font-size": "20px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0 10px"},
        "nav-link-selected": {"background-color": "#d9eaf7"},
    }
)

# --- Page Routing ---
if selected == "Home":
    from pages.home import home
    home()

elif selected == "About":
    from pages.about import about
    about()

elif selected == "Diseases":
    from pages.diseases import diseases
    diseases()


    
    
