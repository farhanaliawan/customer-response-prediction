# Customer Response Prediction 📊

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![MLflow](https://img.shields.io/badge/MLflow-1.30-brightgreen?logo=mlflow)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68-orange?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.10-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow)

A machine learning application to predict customer responses to marketing campaigns using a Random Forest model, FastAPI backend, Streamlit frontend, and MLflow for experiment tracking. Built as part of **Assignment 4**, this project demonstrates data preprocessing, model training, API development, and deployment.

---

## 🚀 Project Overview

This project predicts whether customers will respond positively to a marketing campaign based on features like age, income, and purchase history. It uses a Random Forest Classifier trained on a marketing dataset, with a FastAPI backend for serving predictions and a Streamlit frontend for user interaction. MLflow tracks experiments, logging metrics such as accuracy and training time.

### Features
- **Model**: Random Forest Classifier
- **Backend**: FastAPI for API endpoints
- **Frontend**: Streamlit for an interactive UI
- **Experiment Tracking**: MLflow for logging metrics and parameters
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

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/customer-response-prediction.git
   cd customer-response-prediction
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   - Alternatively, install manually:
     ```bash
     pip install mlflow scikit-learn pandas numpy matplotlib streamlit requests fastapi uvicorn
     ```

3. **Prepare the Dataset**:
   - Ensure `marketing_campaign.csv` is in the project directory. Download it from [here](https://colab.research.google.com/drive/1b5jxIsejuqeY0Hr9AeDyTHdxoe5tkFsT) if needed.

### Running the Project
1. **Train the Model**:
   - Run the training script to generate `model.pkl` and `label_encoders.pkl`:
     ```bash
     python training.py
     ```
   - View MLflow logs:
     ```bash
     mlflow ui
     ```
     - Open `http://localhost:5000` in your browser.

2. **Run the FastAPI Backend**:
   - In a terminal:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```
   - Access the API docs at `http://localhost:8000/docs`.

3. **Run the Streamlit Frontend**:
   - In a separate terminal:
     ```bash
     streamlit run app.py
     ```
   - Open `http://localhost:8501` to interact with the app.

---

## 📈 MLflow Experiment Tracking

- **Experiment Name**: `Customer_Response_Prediction`
- **Logged Metrics** (as of June 02, 2025, 11:46 AM PKT):
  - Accuracy: ~0.85
  - Precision: ~0.67
  - Recall: ~0.09
  - F1 Score: ~0.15
  - Training Time: ~0.25 seconds
- **Logged Parameters**:
  - `n_estimators`: 100
  - `max_depth`: 5

### MLflow UI Screenshot
![MLflow UI Screenshot](https://github.com/farhanaliawan/customer-response-prediction/blob/main/output.PNG?raw=true)
*Caption: MLflow UI showing the Customer_Response_Prediction experiment with logged metrics and parameters.*

---

## 🌐 Deployed Application

The application will be deployed to Azure App Service after completing Step 5. Current status: **In Progress**. Check back for updated URLs:

- **API**: `https://mlapp-fastapi.azurewebsites.net/docs`
- **Frontend**: `https://mlapp-streamlit.azurewebsites.net`

---

## 📝 Assignment Details

This project fulfills the requirements of **Assignment 4**:
- **Step 1: Model Training** ✅ - Trained a Random Forest model (`training.py` or `training.ipynb`) on June 02, 2025.
- **Step 2: Create API using FastAPI** ✅ - Implemented in `main.py`.
- **Step 3: Build Frontend** ✅ - Streamlit app in `app.py`.
- **Step 4: Use MLflow** ✅ - Logged metrics and parameters, screenshot in `mlflow_screenshot.png`.
- **Step 5: Deployment** ⏳ - To be deployed to Azure App Service.

---

## 🖼️ Screenshots

### Streamlit Frontend
![Streamlit Interface](https://github.com/farhanaliawan/customer-response-prediction/blob/main/Capture.PNG?raw=true)
*Caption: Streamlit interface for entering customer data and predicting response.*

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with a clear description of your changes.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ by [Your Name] on June 02, 2025, 12:10 PM PKT**
