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


    
    
