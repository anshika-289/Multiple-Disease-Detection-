import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def home():
    st.markdown("## 👋 Welcome to **Multiple Disease Detection**")
    st.markdown("""
        This application is designed to assist users in predicting the likelihood of multiple health conditions using machine learning models. 
        Currently, the system supports predictions for the following diseases:
        
        - **Diabetes**
        - **Heart Disease**
        - **Parkinson's Disease**
        
        Users can input relevant medical data and receive instant predictions based on trained models. This tool aims to aid in early awareness and proactive healthcare decisions.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st_lottie(load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x1gjdldd.json"), height=300)
    with col2:
        st.markdown("### 🩺 Available Features:")
        st.markdown("- Multiple Disease Prediction")
        st.markdown("- Easy-to-use Web Interface")
        st.markdown("- Real-time Result Display")
        st.markdown("- Recommendation on prevention and cure")