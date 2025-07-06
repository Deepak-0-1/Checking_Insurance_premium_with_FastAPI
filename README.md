**🧠 Insurance Premium Prediction API (FastAPI)**

This project is an end-to-end Machine Learning API built with **FastAPI** that predicts insurance premium categories based on user demographic and lifestyle information.

---

**🚀 Features**

- ✅ Predicts insurance premium category (Low / Medium / High)
- ✅ Provides model confidence score and class probabilities
- ✅ Built using FastAPI for high-performance APIs
- ✅ Modular structure with separate schema, model, and API logic
- ✅ Ready for deployment (Docker, Cloud, etc.)

**🏗️ Project Structure**
insurance-premium-api/
├── app.py
│ ├── model
│ │ ├── model/model.pkl # ML Model
│ │ └── predict.py # Prediction logic
│ ├── schema/
│ │ ├── user_input.py # Input data model
│ │ └── prediction_response.py # Output data model
├── requirements.txt
├── README.md
└── .gitignore

**🧪 Input Features**

| Feature | Description |
|--------|-------------|
| `age_group` | Categorical (e.g. "18-25", "26-35", etc.) |
| `bmi` | Body Mass Index |
| `lifestyle_risk` | Score based on habits like smoking, exercise |
| `city_tier` | Tier classification of the city (1/2/3) |
| `income_lpa` | Annual income in Lakhs (INR) |
| `occupation` | Job type (student, private_job, etc.) |

---

## 🧾 Example Request (POST `/predict`)

```json
{
  "age_group": "26-35",
  "bmi": 24.5,
  "lifestyle_risk": "medium",
  "city_tier": 2,
  "income_lpa": 8.5,
  "occupation": "private_job"
}
```

## 🎯 Example Response
```json
Copy code
{
  "predicted_category": "High",
  "confidence": 0.8432,
  "class_probabilities": {
    "Low": 0.01,
    "Medium": 0.15,
    "High": 0.84
  }
}
```

⚙️ Setup Instructions
1. Clone the repo
  git clone https://github.com/yourusername/insurance-premium-api.git
  cd insurance-premium-api

2. Create virtual environment
  python -m venv venv
  source venv/bin/activate   # or venv\Scripts\activate on Windows

3. Install dependencies
  pip install -r requirements.txt

4. Run the API
  uvicorn app.main:app --reload

5. Open in browser
  Swagger UI: http://127.0.0.1:8000/docs
  ReDoc: http://127.0.0.1:8000/redoc


📦 Dependencies
Python 3.8+
FastAPI
Pydantic
Uvicorn
scikit-learn (for model)
joblib / pickle (for model loading)


🧠 Model Details
The model was trained on a dataset containing demographic, lifestyle, and income-related features to predict the premium category. It uses:

1. One-hot encoding for categorical features
2. Random Forest Classifier (or your actual model)
3. Trained using scikit-learn


✨ Author
Deepak Singh
Connect on LinkedIn :- www.linkedin.com/in/deepaksingh917566519721
Mail: dsdeep2324@gmail.com
