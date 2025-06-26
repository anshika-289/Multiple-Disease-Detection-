import streamlit as st
import pickle
from joblib import load

# Load model and scaler
parkinsons_model = pickle.load(open("models/parkinsons_model.sav", "rb"))
scaler = load("models/std_scaler_parkinsons.bin")

def parkinsons_form():
    st.title("🧠 Parkinson's Disease Prediction")
    st.markdown("Please enter the voice metrics below for prediction:")

    with st.form("parkinsons_form"):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            fo = st.number_input("MDVP:Fo(Hz)")
            RAP = st.number_input("MDVP:RAP")
            APQ3 = st.number_input("Shimmer:APQ3")
            RPDE = st.number_input("RPDE")
            fhi = st.number_input("MDVP:Fhi(Hz)")
            PPQ = st.number_input("MDVP:PPQ")
        with col2:
            APQ5 = st.number_input("Shimmer:APQ5")
            DFA = st.number_input("DFA")
            flo = st.number_input("MDVP:Flo(Hz)")
            DDP = st.number_input("MDVP:DDP")
            APQ = st.number_input("MDVP:APQ")
            spread1 = st.number_input("Spread 1")
        with col3:
            jitter_percent = st.number_input("MDVP:Jitter(%)")
            jitter_abs = st.number_input("MDVP:Jitter(Abs)")
            shimmer = st.number_input("MDVP:Shimmer")
            shimmer_dB = st.number_input("MDVP:Shimmer(dB)")
            DDA = st.number_input("Shimmer:DDA")
        with col4:
            NHR = st.number_input("NHR")
            HNR = st.number_input("HNR")
            spread2 = st.number_input("Spread 2")
            D2 = st.number_input("D2")
            PPE = st.number_input("PPE")

        submitted = st.form_submit_button("🔍 Predict Parkinson's Disease")

        if submitted:
            input_data = scaler.transform([[
                fo, fhi, flo, jitter_percent, jitter_abs,
                RAP, PPQ, DDP, shimmer, shimmer_dB,
                APQ3, APQ5, APQ, DDA, NHR, HNR,
                RPDE, DFA, spread1, spread2, D2, PPE
            ]])

            prediction = parkinsons_model.predict(input_data)

            if prediction[0] == 1:
                st.error("🧠 The person is likely to have Parkinson's Disease.")
                st.markdown("#### ✅ Health Management Tips:")
                st.markdown("""
                - Consult a neurologist for a detailed diagnosis  
                - Engage in physical therapy and voice exercises  
                - Take prescribed medication regularly  
                - Maintain a well-balanced diet
                """)
            else:
                st.success("🎉 The person does not have Parkinson's Disease.")
                st.markdown("#### 💡 Preventive Advice:")
                st.markdown("""
                - Stay physically active and mentally engaged  
                - Regular health checkups, especially after age 50  
                - Monitor speech or coordination changes
                """)

if __name__ == "__main__":
    parkinsons_form()
