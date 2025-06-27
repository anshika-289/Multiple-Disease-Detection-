import streamlit as st
import pickle

# Load model
heart_disease_model = pickle.load(open("models/heart_disease_model.sav", "rb"))

def heart_form():
    st.title("❤️ Heart Disease Prediction")
    st.markdown("Please enter the required information below:")

    with st.form("heart_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input("Age", min_value=1, max_value=120)
            sex = st.selectbox("Sex", ["Male (1)", "Female (0)"])
            cp = st.selectbox("Chest Pain Type", ["Typical Angina (0)", "Atypical Angina (1)", "Non-anginal Pain (2)", "Asymptomatic (3)"])
            rbp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0.0, max_value=250.0)
            sc = st.number_input("Serum Cholesterol (mg/dl)", min_value=0.0, max_value=800.0)
        with col2:
            fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["True (1)", "False (0)"])
            restecg = st.selectbox("Resting ECG Results", ["Normal (0)", "Having ST-T wave abnormality (1)", "Showing probable/definite left ventricular hypertrophy (2)"])
            thalach = st.number_input("Max Heart Rate Achieved", min_value=0.0, max_value=250.0)
            exang = st.selectbox("Exercise Induced Angina", ["Yes (1)", "No (0)"])
        with col3:
            oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0)
            slope = st.selectbox("Slope of ST Segment", ["Upsloping (0)", "Flat (1)", "Downsloping (2)"])
            ca = st.number_input("Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4)
            thal = st.selectbox("Thalassemia", ["Normal (1)", "Fixed Defect (2)", "Reversible Defect (3)"])

        submitted = st.form_submit_button("🔍 Predict Heart Disease")

        if submitted:
            input_data = [[
                age,
                int(sex.split("(")[-1][0]),
                int(cp.split("(")[-1][0]),
                rbp,
                sc,
                int(fbs.split("(")[-1][0]),
                int(restecg.split("(")[-1][0]),
                thalach,
                int(exang.split("(")[-1][0]),
                oldpeak,
                int(slope.split("(")[-1][0]),
                ca,
                int(thal.split("(")[-1][0])
            ]]

            prediction = heart_disease_model.predict(input_data)

            if prediction[0] == 1:
                st.error("💔 The person has a risk of Heart Disease.")
                st.markdown("#### ✅ Health Recommendations:")
                st.markdown("""
                - Follow a heart-healthy diet (low in salt and cholesterol)  
                - Regular cardiovascular exercises  
                - Quit smoking and alcohol  
                - Regular checkups and manage stress levels
                """)
            else:
                st.success("🎉 The person does not have Heart Disease.")
                st.markdown("#### 💡 Health Tips:")
                st.markdown("""
                - Continue a healthy lifestyle to maintain heart health  
                - Stay physically active  
                - Monitor blood pressure and cholesterol levels annually
                """)

if __name__ == "__main__":
    heart_form()
