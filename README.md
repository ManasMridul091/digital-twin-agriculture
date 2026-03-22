# 🌾 Digital Twin Smart Agriculture System

## 📌 Project Overview
This project implements a **Digital Twin of a Smart Agriculture System** using Machine Learning and Web Technologies.

It simulates a real-world farm by modeling environmental conditions such as temperature, humidity, rainfall, and soil parameters, and provides real-time predictions and insights.

---

## 🚀 Features

- 🌡️ Real-time environmental simulation
- 🌱 Crop prediction using Machine Learning
- 📈 Yield prediction model
- 💧 Smart irrigation recommendation system
- 📊 Live dashboard with dynamic graphs
- 🎛️ User input control panel (interactive simulation)
- 🌐 Web-based interface using Flask

---

## 🧠 Digital Twin Concept

This system acts as a **virtual replica of a farm** by:
- Simulating environmental conditions over time
- Predicting crop suitability
- Providing actionable insights (irrigation, yield)

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **Backend:** Flask (Python)  
- **Machine Learning:** Scikit-learn (Random Forest)  
- **Data Handling:** Pandas  
- **Deployment:** Render  

---

## 📂 Project Structure
digital_twin_agriculture/
│
├── app.py
├── model.py
├── model.pkl
├── dataset/
│ └── crop_recommendation.csv
├── static/
│ ├── style.css
│ └── script.js
├── templates/
│ └── index.html
├── requirements.txt
└── Procfile


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/digital-twin-agriculture.git
cd digital-twin-agriculture

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
python app.py

4️⃣ Open in browser
http://127.0.0.1:5000/

📊 How It Works
Dataset simulates farm sensor data
ML model predicts crop suitability
Yield is estimated using environmental factors
Dashboard visualizes real-time farm conditions
User can modify inputs for simulation

🌟 Future Improvements
Integration with real IoT sensors
Advanced deep learning models (LSTM)
Mobile app interface
Weather API integration

👨‍💻 Author
Manas Mridul