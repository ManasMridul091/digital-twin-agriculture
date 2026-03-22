import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
import joblib

# 🔴 Load dataset once (performance improvement)
data = pd.read_csv("dataset/crop_recommendation.csv")

# 🔴 Train model
def train_model():
    X = data[['N','P','K','temperature','humidity','ph','rainfall']]
    y = data['label']

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    joblib.dump(model, "model.pkl")


# 🔴 Load trained model
def load_model():
    return joblib.load("model.pkl")


# 🔴 Yield Prediction Function (NEW 🔥)
def predict_yield(temp, humidity, rainfall):
    # Simple synthetic model (easy to explain in viva)
    yield_value = (0.5 * temp + 0.3 * humidity + 0.2 * rainfall) / 10
    return round(yield_value, 2)


# 🔴 Digital Twin Simulation Engine
def get_random_day_prediction(model):
    
    # pick random row (simulated sensor data)
    row = data.sample(1).iloc[0]

    # ML prediction
    prediction = model.predict([[
        row['N'], row['P'], row['K'],
        row['temperature'], row['humidity'],
        row['ph'], row['rainfall']
    ]])[0]

    # 🔴 Improved irrigation logic
    if row['humidity'] < 45 and row['rainfall'] < 100:
        irrigation = "High Priority 🚨"
    elif row['humidity'] < 60:
        irrigation = "Moderate ⚠️"
    else:
        irrigation = "Not Required ✅"

    # 🔴 Yield prediction
    yield_pred = predict_yield(
        float(row['temperature']),
        float(row['humidity']),
        float(row['rainfall'])
    )

    # 🔴 Return clean JSON-safe data
    return {
        "temperature": round(float(row['temperature']), 2),
        "humidity": round(float(row['humidity']), 2),
        "rainfall": round(float(row['rainfall']), 2),
        "ph": round(float(row['ph']), 2),
        "crop": str(prediction),
        "irrigation": irrigation,
        "yield": yield_pred
    }