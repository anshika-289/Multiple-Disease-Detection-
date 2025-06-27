# 🧠 Multiple Disease Prediction App

 **Multiple Disease Prediction App** is a Streamlit-powered machine learning web application that allows users to predict the likelihood of multiple health conditions based on clinical input data. The app currently supports disease prediction for Diabetes, Heart Disease, and Parkinson’s Disease.

---

## 🚀 Features

- 🎯 **Accurate Predictions** using pre-trained ML models
- 🩺 Disease support for:
  - Diabetes
  - Heart Disease
  - Parkinson’s Disease
- 📊 User-friendly interface for entering health parameters
- 💾 Model persistence using `pickle` and `joblib`
- 📂 Organized and modular codebase

---

## 🧩 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas / NumPy
- Joblib / Pickle

---

## 📁 Project Structure

```
├── app.py                  # Main Streamlit app launcher
├── requirements.txt        # Python dependencies
├── models/                 # Saved ML models (.sav files)
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
├── processing/             # Jupyter notebooks used for training
│   ├── diabetes_prediction.ipynb
│   ├── heart_disease_prediction.ipynb
│   └── parkinsons_prediction.ipynb
├── pages/                  # Streamlit page components
│   ├── home.py
│   ├── about.py
│   └── diseases.py
└── assets/                 # Any images or static files (optional)
```

---

## ▶️ How to Run the App

1. **Clone the Repository**  
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the App**  
   ```bash
   streamlit run app.py
   ```

---

## 📈 Model Training Overview

The models were trained using standard classification algorithms with scikit-learn:

- **Diabetes:** Logistic Regression
- **Heart Disease:** Logistic Regression
- **Parkinson’s Disease:** SVM (Linear Kernel)

Each model was trained in Jupyter notebooks (`/processing/`) using cleaned datasets and serialized for deployment.

---

## 📌 Notes

- Ensure your CSV datasets are properly structured if you retrain the models.
- All models are stored in the `models/` folder and are loaded during runtime.
- Make sure all page modules in `pages/` are present for navigation to work.

---

## 📬 Feedback

Feel free to contribute, suggest improvements, or raise issues!
