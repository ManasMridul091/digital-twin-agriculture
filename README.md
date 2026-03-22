# 🌾 Digital Twin Smart Agriculture System

## 📌 Overview
The **Digital Twin Smart Agriculture System** is an AI-powered web application that simulates a real-world agricultural environment using machine learning and data-driven modeling.

It creates a **virtual replica (Digital Twin)** of a farm by continuously simulating environmental conditions and providing intelligent predictions for crop selection, irrigation, and yield estimation.

---

## 🌐 Live Demo
👉 https://digital-twin-agriculture.onrender.com

> ⚠️ Note: The app may take 30–60 seconds to load initially due to free cloud hosting.

---

## 🚀 Key Features

### 🔁 Digital Twin Simulation
- Continuous simulation of farm conditions
- Time-based environmental modeling

### 🌱 Crop Prediction (ML Model)
- Uses Random Forest Classifier
- Predicts best crop based on:
  - Temperature
  - Humidity
  - Rainfall
  - Soil nutrients (N, P, K)

### 📈 Yield Prediction
- Estimates crop yield using environmental factors
- Provides production insights

### 💧 Smart Irrigation System
- Intelligent irrigation recommendation:
  - 🚨 High Priority  
  - ⚠️ Moderate  
  - ✅ Not Required  

### 📊 Interactive Dashboard
- Real-time graphs:
  - Temperature
  - Humidity
  - Rainfall
  - Yield
- Smooth animations & live updates

### 🎛️ User Control Panel
- Modify environmental parameters manually
- Observe real-time predictions

---

## 🧠 Digital Twin Concept

This project implements a **Digital Twin** by:

- Representing a physical farm as a virtual model  
- Simulating real-world environmental changes  
- Integrating machine learning for predictions  
- Providing feedback for decision-making  

---

## 🛠️ Tech Stack

| Layer        | Technology Used |
|-------------|----------------|
| Frontend    | HTML, CSS, JavaScript, Chart.js |
| Backend     | Flask (Python) |
| ML Model    | Scikit-learn (Random Forest) |
| Data        | Pandas |
| Deployment  | Render |

---

## 📂 Project Structure
digital_twin_agriculture/
│
├── app.py # Flask backend
├── model.py # ML model & simulation logic
├── model.pkl # Trained model
├── dataset/
│ └── crop_recommendation.csv
├── static/
│ ├── style.css # UI styling
│ └── script.js # Frontend logic
├── templates/
│ └── index.html # Dashboard UI
├── requirements.txt
└── Procfile


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/digital-twin-agriculture.git
cd digital-twin-agriculture

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
python app.py

4️⃣ Open in Browser
http://127.0.0.1:5000/

📊 System Workflow
Dataset simulates real farm sensor data
ML model predicts crop suitability
Yield is estimated using environmental inputs
Digital twin updates continuously
Dashboard visualizes real-time insights
User can interact and modify conditions

🌟 Future Enhancements
🔌 Integration with IoT sensors
🌦️ Weather API integration
🤖 Deep learning models (LSTM)
📱 Mobile application
☁️ Multi-farm digital twin system
👨‍💻 Author

Manas Mridul
B.Tech Electrical & Computer Engineering