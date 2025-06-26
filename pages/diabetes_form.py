import streamlit as st
import pickle
from joblib import load

# Load models and scalers
diabetes_model = pickle.load(open("models/diabetes_model.sav", "rb"))
diabetes_scaler = load("models/std_scaler_diabetes.bin")

def diabetes_form():
    st.title("🩸 Diabetes Prediction")
    st.markdown("Please fill in the following details to get your prediction.")

    with st.form("diabetes_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20)
            SkinThickness = st.number_input("Skin Thickness (mm)", min_value=0.0, max_value=100.0)
            DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5)
        with col2:
            Glucose = st.number_input("Glucose Level", min_value=0.0, max_value=300.0)
            Insulin = st.number_input("Insulin Level", min_value=0.0, max_value=900.0)
            Age = st.number_input("Age", min_value=1, max_value=120)
        with col3:
            BloodPressure = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0)
            BMI = st.number_input("BMI", min_value=0.0, max_value=70.0)

        submitted = st.form_submit_button("🔍 Predict Diabetes")

        if submitted:
            input_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
            std_data = diabetes_scaler.transform(input_data)
            prediction = diabetes_model.predict(std_data)

            if prediction[0] == 1:
                st.error("🩺 The person is Diabetic.")
                st.markdown("#### ✅ Health Recommendations:")
                st.markdown("""
                - Maintain a balanced diet with low sugar intake  
                - Regular physical activity (e.g., walking, yoga)  
                - Monitor blood glucose regularly  
                - Stay hydrated and get regular medical checkups
                """)
            else:
                st.success("🎉 The person is not Diabetic.")
                st.markdown("#### 💡 Health Tips:")
                st.markdown("""
                - Maintain a healthy lifestyle to prevent diabetes  
                - Include fiber-rich food and avoid sugary beverages  
                - Stay active at least 30 mins/day  
                - Annual screening is recommended
                """)

if __name__ == "__main__":
    diabetes_form()
