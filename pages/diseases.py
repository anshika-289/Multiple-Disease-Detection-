import streamlit as st

def diseases():
    st.title("🦠 Disease Prediction Modules")
    st.markdown("Select a disease below to proceed with prediction:")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container():
            st.image("https://img.icons8.com/fluency/96/diabetes.png", width=80)
            st.markdown("### Diabetes")
            if st.button("🔍 Predict Diabetes"):
                st.switch_page("C:/Users/om-31406/Desktop/Anshika/PROJECTS/HealthGuard/pages/diabetes_form.py")

    with col2:
        with st.container():
            st.image("https://cdn-icons-png.flaticon.com/512/833/833472.png", width=80)
            st.markdown("### Heart Disease")
            if st.button("🔍 Predict Heart Disease"):
                st.switch_page("C:/Users/om-31406/Desktop/Anshika/PROJECTS/HealthGuard/pages/heart_form.py")

    with col3:
        with st.container():
            st.image("https://cdn-icons-png.flaticon.com/512/2785/2785447.png", width=80)
            st.markdown("### Parkinson's Disease")
            if st.button("🔍 Predict Parkinson's"):
                st.switch_page("C:/Users/om-31406/Desktop/Anshika/PROJECTS/HealthGuard/pages/parkinsons_form.py")
