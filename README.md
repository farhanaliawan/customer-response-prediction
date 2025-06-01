# Customer Response Prediction 📊

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![MLflow](https://img.shields.io/badge/MLflow-1.30-brightgreen?logo=mlflow)
![License](https://img.shields.io/badge/License-MIT-yellow)

A machine learning application to predict customer responses to marketing campaigns using a Random Forest model, FastAPI backend, Streamlit frontend, and MLflow for experiment tracking. Built as part of **Assignment 4**, this project demonstrates data preprocessing, model training, experiment tracking, API development, and deployment.

---

## 🚀 Project Overview

This project predicts whether customers will respond positively to a marketing campaign. It uses a Random Forest model trained on customer data, with a FastAPI backend for predictions and a Streamlit frontend for user interaction. MLflow tracks experiments, logging metrics like accuracy, precision, and training time.

### Features
- **Model**: Random Forest Classifier
- **Backend**: FastAPI for serving predictions
- **Frontend**: Streamlit for an interactive UI
- **Experiment Tracking**: MLflow to log metrics and parameters
- **Deployment**: Deployable to Azure App Service

---

## 📂 Project Structure

```
customer-response-prediction/
├── app.py                  # Streamlit frontend for user interaction
├── label_encoders.pkl      # Label encoders for categorical features
├── main.py                 # FastAPI backend for predictions
├── model.pkl               # Trained Random Forest model
├── requirements.txt        # Dependencies
├── training.py             # Model training script with MLflow logging
├── training.ipynb          # Jupyter Notebook version of the training script
├── marketing_campaign.csv  # Dataset used for training
├── mlflow_screenshot.png   # MLflow UI screenshot
├── streamlit_interface.png # Streamlit frontend screenshot
└── README.md               # Project documentation
```

---

## 🛠️ Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites
- Python 3.9+
- Git
- Azure CLI (for deployment)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/customer-response-prediction.git
   cd customer-response-prediction
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI Backend**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   - Access the API at `http://localhost:8000/docs`.

4. **Run the Streamlit Frontend**:
   In a separate terminal:
   ```bash
   streamlit run app.py
   ```
   - Open `http://localhost:8501` to interact with the app.

5. **View MLflow Experiments**:
   ```bash
   mlflow ui
   ```
   - Open `http://localhost:5000` to see experiment logs.

---

## 📈 MLflow Experiment Tracking

- **Experiment Name**: `Customer_Response_Prediction`
- **Logged Metrics**:
  - Accuracy: 0.852657144991638
  - Precision: 0.6666666666666666
  - Recall: 0.08695652173913043
  - F1 Score: 0.15384615384615385
  - Training Time: 0.24502181816101074 seconds
- **Logged Parameters**:
  - `n_estimators`: 100
  - `max_depth`: 5

### MLflow UI Screenshot
![MLflow UI Screenshot](![output](https://github.com/user-attachments/assets/ae3d4f04-e310-47a2-8aa8-4f586709d66a)
)
*Caption: MLflow UI showing the Customer_Response_Prediction experiment with logged metrics and parameters.*

---

## 🌐 Deployed Application

After deployment to Azure App Service, the application will be live at the following URLs (to be updated after deployment):

- **API**: `https://mlapp-fastapi.azurewebsites.net/docs`
- **Frontend**: `https://mlapp-streamlit.azurewebsites.net`

---

## 📝 Assignment Details

This project fulfills the requirements of **Assignment 4**:
- **Step 1: Model Training** ✅ - Trained a Random Forest model (`training.py` or `training.ipynb`).
- **Step 2: Create API using FastAPI** ✅ - Implemented in `main.py`.
- **Step 3: Build Frontend** ✅ - Streamlit app in `app.py`.
- **Step 4: Use MLflow** ✅ - Logged metrics and parameters, screenshot in `mlflow_screenshot.png`.
- **Step 5: Deployment** ⏳ - To be deployed to Azure App Service.

---

## 🖼️ Screenshots

### Streamlit Frontend
![Streamlit Interface](streamlit_interface.png)
*Caption: Streamlit interface for entering customer data and predicting response.*

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ by [Your Name] on June 2, 2025**
