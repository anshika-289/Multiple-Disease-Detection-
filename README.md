# 🧠 Multiple Disease Detection

Multiple Disease Detection is a Streamlit-based machine learning web app designed to predict the likelihood of common health conditions using pre-trained classification models. This project aims to promote early detection and self-assessment in an accessible and user-friendly way.

## 🚀 Features

- 🩺 Disease prediction for:
  - Diabetes
  - Heart Disease
  - Parkinson’s Disease
- 📊 Easy-to-use interface for inputting medical information
- 🧠 Pre-trained ML models for real-time health risk assessment
- 🔐 Data privacy — everything runs locally in the app
- ✅ Built with Streamlit, scikit-learn, and Python

## 🗂️ Project Structure

Multiple Disease Detection/
├── app.py # Main entry point for Streamlit app
├── requirements.txt # Required packages
├── data/ # Health datasets (CSV)
│ ├── diabetes.csv
│ ├── heart_disease_data.csv
│ └── parkinsons.csv
├── models/ # Trained ML models and scalers
│ ├── *.sav
│ └── *.bin
├── pages/ # Streamlit multipage files
│ ├── home.py
│ ├── about.py
│ ├── diseases.py
│ ├── diabetes_form.py
│ ├── heart_form.py
│ └── parkinsons_form.py
├── processing/ # Jupyter notebooks for training
│ ├── Diabetes_Prediction.ipynb
│ ├── Heart_Disease_Detection.ipynb
│ └── Parkinson_Detection.ipynb

bash
Copy
Edit

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/multiple-disease-detection.git
cd multiple-disease-detection
(Optional) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Running the App
bash
Copy
Edit
streamlit run app.py
👩‍💻 Developed By
Anshika Verma
B.Tech in Computer Science (AI Specialization)
Graduating in 2027

📚 Acknowledgements
Open-source ML & health datasets

Streamlit & scikit-learn communities

Mentors and contributors