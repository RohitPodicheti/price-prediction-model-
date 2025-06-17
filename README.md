
# 🏠 Real Estate Price Prediction Model

This project is a machine learning-based web application that predicts real estate property prices based on features like the number of rooms, bedrooms, square footage, parking availability, and price per square foot. It’s built using Python, trained using Linear Regression, and deployed with Streamlit.

---

## 📊 Features

- Predict real estate prices using simple input fields
- Visualize data distribution and feature relationships (EDA)
- Streamlit-powered interactive web app
- Clean and minimal UI

---

## 🧠 Machine Learning Model

- **Algorithm**: Linear Regression
- **Features used**:
  - `rooms`
  - `bedrooms`
  - `area_sqft`
  - `parking`
  - `price_per_sqft`
- **Performance Metrics**:
  - R² Score
  - RMSE

---

## 🛠️ Project Structure

```
real_estate_price_predictor/
├── app/
│   └── app.py                 # Streamlit application
├── data/
│   └── real_estate_data.csv   # Dataset
├── model/
│   └── realestate_model.pkl   # Trained ML model
├── notebooks/
│   └── eda_and_model.ipynb    # EDA and training notebook
├── requirements.txt
└── README.md
```

---

## 🚀 Run Locally

### 🔧 Setup

1. Clone the repository:

```bash
git clone https://github.com/RohitPodicheti/price-prediction-model-.git
cd price-prediction-model-
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app/app.py
```

---

## 🌐 Deployment

The app can be deployed on [Streamlit Cloud](https://streamlit.io/cloud) in 2 minutes. Just connect this GitHub repo and Streamlit will handle the rest!

---

## 📈 Sample Input

| Rooms | Bedrooms | Area (sqft) | Parking | Price/sqft | → Predicted Price |
|-------|----------|-------------|---------|------------|--------------------|
| 3     | 2        | 1000        | 1       | 180        | ₹1,80,000          |

---

## 📌 Future Enhancements

- Add location-based features
- Use advanced models like Random Forest or XGBoost
- Include more visualizations in the UI

---

## 🙋‍♂️ Author

[Rohit Podicheti](https://github.com/RohitPodicheti)

 STEAMLIT MODEL LINK -(https://house-price-prediction-modell.streamlit.app/)
