from flask import Flask, render_template, jsonify, request
from model import train_model, load_model, get_random_day_prediction
import os

app = Flask(__name__)

if not os.path.exists("model.pkl"):
    train_model()

model = load_model()

@app.route("/")
def index():
    return render_template("index.html")

# API for live simulation
@app.route("/get_data")
def get_data():
    data = get_random_day_prediction(model)
    return jsonify(data)

# API for user input prediction
@app.route("/predict", methods=["POST"])
def predict():
    input_data = request.json
    prediction = model.predict([[
        input_data['N'], input_data['P'], input_data['K'],
        input_data['temperature'], input_data['humidity'],
        input_data['ph'], input_data['rainfall']
    ]])[0]

    return jsonify({"crop": str(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)