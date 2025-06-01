import streamlit as st
import requests
import pickle

# Load label encoders to get valid options
with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

st.title("Customer Response Prediction")

# Input form
age = st.number_input("Age", min_value=18, max_value=100, value=45)
education = st.selectbox("Education", options=list(label_encoders['Education'].classes_))
marital_status = st.selectbox("Marital Status", options=list(label_encoders['Marital_Status'].classes_))
income = st.number_input("Income", min_value=0.0, value=60000.0)
total_children = st.number_input("Total Children", min_value=0, value=2)
recency = st.number_input("Recency (days since last purchase)", min_value=0, value=30)
total_spending = st.number_input("Total Spending", min_value=0.0, value=500.0)
total_purchases = st.number_input("Total Purchases", min_value=0, value=10)
num_web_visits = st.number_input("Web Visits per Month", min_value=0, value=5)

if st.button("Predict"):
    # Prepare JSON payload
    data = {
        "Age": age,
        "Education": education,
        "Marital_Status": marital_status,
        "Income": income,
        "Total_Children": total_children,
        "Recency": recency,
        "Total_Spending": total_spending,
        "Total_Purchases": total_purchases,
        "NumWebVisitsMonth": num_web_visits
    }
    
    # Send request to FastAPI
    try:
        response = requests.post("http://localhost:8000/predict", json=data)
        prediction = response.json().get("prediction")
        if prediction is not None:
            st.success(f"Prediction: {'Positive' if prediction == 1 else 'Negative'}")
        else:
            st.error(f"Error: {response.json().get('error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to API: {e}")