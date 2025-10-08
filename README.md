# 🌲 Algerian Forest Fires Prediction 🔥  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) 
[![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange)](https://scikit-learn.org/stable/) 
[![Flask](https://img.shields.io/badge/Web-Framework-ff69b4)](https://flask.palletsprojects.com/) 
[![Deployed on Railway](https://img.shields.io/badge/Deployed-Railway-brightgreen)](https://modelbuildingdemo-production.up.railway.app/predict)

> ⚠️ **Note:** This is an **experimental project** created to explore the process of **machine learning model building and deployment**.  
> The live demo is hosted on **Railway**: [https://modelbuildingdemo-production.up.railway.app/predict](https://modelbuildingdemo-production.up.railway.app/predict)

---

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [📁 Project Structure](#-project-structure)
- [📊 Dataset Description](#-dataset-description)
- [⚙️ Installation & Setup](#️-installation--setup)
- [🚀 Usage](#-usage)
- [🧠 Machine Learning Workflow](#-machine-learning-workflow)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Future Improvements](#-future-improvements)
- [📜 License](#-license)
- [👨‍💻 Author](#-author)

---

## 📌 Project Overview

**Algerian Forest Fires Prediction** is a simple but complete **machine learning project** designed to **predict the likelihood of a forest fire** based on meteorological and environmental parameters.

This project demonstrates:
- ✅ End-to-end ML pipeline (EDA → Feature Engineering → Model Training → Deployment)
- 🌐 Building and serving a prediction API using Flask
- ☁️ Deploying the model to the cloud (Railway platform)

---

## 📁 Project Structure

```

├── .ebextensions/                          # AWS Elastic Beanstalk deployment configs (optional)
├── Notebooks/
│   ├── 2.0-EDA And FE Algerian Forest Fires.ipynb   # Data exploration and feature engineering
│   └── 3.0-Model Training.ipynb                     # Model training and evaluation
├── data/
│   ├── Algerian_forest_fires_cleaned_dataset.csv   # Cleaned dataset
│   └── Algerian_forest_fires_dataset_UPDATE.csv    # Original dataset
├── models/
│   ├── ridge.pkl                                   # Trained ML model
│   └── scaler.pkl                                  # Data scaler for preprocessing
├── templates/
│   ├── home.html                                   # Web interface homepage
│   └── index.html                                  # Result page
├── application.py                                  # Flask application
├── requirements.txt                                # Python dependencies
└── README.md                                       # Project documentation

````

---

## 📊 Dataset Description

The dataset is derived from the **Algerian Forest Fires Dataset**, containing meteorological variables and fire records.  
Key features include:

| Feature            | Description                      |
|--------------------|----------------------------------|
| Temperature        | Daily average temperature        |
| RH                 | Relative Humidity (%)            |
| Ws                 | Wind Speed (km/h)                |
| Rain               | Daily Rainfall (mm)              |
| FFMC, DMC, DC, ISI | Fire weather indices             |
| Classes            | Target variable (fire / no fire) |

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally 👇:

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/algerian-forest-fires.git
cd algerian-forest-fires
````

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask application**

```bash
python application.py
```

Your app will be running at:
👉 `http://127.0.0.1:5000/`

---

## 🚀 Usage

* Visit the web interface or directly access the deployed API endpoint:
  🌐 **Live API:** [https://modelbuildingdemo-production.up.railway.app/predict](https://modelbuildingdemo-production.up.railway.app/predict)
* Input meteorological parameters to predict whether a **fire is likely**.
* The model responds with a **binary classification**: `Fire` or `No Fire`.

---

## 🧠 Machine Learning Workflow

1. **Exploratory Data Analysis (EDA)** – Understand feature distributions, correlations, and trends.
2. **Feature Engineering** – Data cleaning, encoding, scaling, and feature selection.
3. **Model Training** – Ridge Regression model trained and serialized with `pickle`.
4. **API Deployment** – Model served with Flask API for real-time predictions.
5. **Cloud Deployment** – Hosted on [Railway](https://railway.app/) for public access.

---

## 🛠️ Tech Stack

| Category             | Tools                                     |
| -------------------- | ----------------------------------------- |
| **Language**         | Python                                    |
| **Data Analysis**    | Pandas, NumPy, Matplotlib, Seaborn        |
| **Machine Learning** | scikit-learn                              |
| **Web Framework**    | Flask                                     |
| **Frontend**         | HTML, CSS (Jinja2 Templates)              |
| **Deployment**       | Railway, AWS Elastic Beanstalk (optional) |
| **Serialization**    | pickle                                    |

---

## 📈 Future Improvements

* 🔥 Add ensemble models like Random Forest or XGBoost
* 🧪 Automate pipeline with MLflow for experiment tracking
* 📊 Create a dashboard for fire risk visualization
* ☁️ Integrate CI/CD for seamless deployment updates

---

## 📜 License

This project is released under the [MIT License](LICENSE).

---
