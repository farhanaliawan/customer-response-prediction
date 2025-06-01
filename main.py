from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="Customer Response Prediction API", description="API for predicting customer response to marketing campaigns")

# Define the input schema using Pydantic
class PredictionInput(BaseModel):
    Age: int
    Education: str
    Marital_Status: str
    Income: float
    Total_Children: int
    Recency: int
    Total_Spending: float
    Total_Purchases: int
    NumWebVisitsMonth: int

    class Config:
        json_schema_extra = {
            "example": {
                "Age": 45,
                "Education": "Graduation",
                "Marital_Status": "Married",
                "Income": 60000.0,
                "Total_Children": 2,
                "Recency": 30,
                "Total_Spending": 500.0,
                "Total_Purchases": 10,
                "NumWebVisitsMonth": 5
            }
        }

# Load model and label encoders
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

# Root endpoint for basic testing
@app.get("/")
async def root():
    return {"message": "Welcome to the Customer Response Prediction API"}

# Prediction endpoint
@app.post("/predict")
async def predict(data: PredictionInput):
    # Convert input to DataFrame
    input_data = pd.DataFrame([data.dict()])

    # Encode categorical variables
    for col in ['Education', 'Marital_Status']:
        try:
            input_data[col] = label_encoders[col].transform(input_data[col])
        except ValueError as e:
            return {"error": f"Invalid value for {col}. Must be one of {list(label_encoders[col].classes_)}"}

    # Ensure feature order matches training
    features = ['Age', 'Education', 'Marital_Status', 'Income', 'Total_Children',
                'Recency', 'Total_Spending', 'Total_Purchases', 'NumWebVisitsMonth']
    input_data = input_data[features]

    # Make prediction
    prediction = model.predict(input_data)[0]

    return {"prediction": int(prediction)}