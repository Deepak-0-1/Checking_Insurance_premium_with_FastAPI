# ML code
import pickle
import pandas as pd

# importing MLmodel
with open('model/model.pkl','rb') as f:
    model = pickle.load(f)

# Versions of ML model comes from MLFLOW by default when we have deployed the model on cloud
MODEL_VERSION = '1.0.0'

# Get class label from model(important for matching probabilities to class names)
class_label = model.classes_.tolist()

def predict_output(user_input:dict):

    df = pd.DataFrame([user_input])

    # predicted_class
    predicted_class = model.predict(df)[0]

    # Get probabilities of all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    # creat mapping: {class_name: probability}
    class_probs = dict(zip(class_label, map(lambda p: round(p,4), probabilities)))

    return{
        "predicted_category": predicted_class,
        "confidence": round(confidence,4),
        "class_probabilities": class_probs
    }