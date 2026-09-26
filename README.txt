# 🚗 Car Data Analysis Dashboard

An interactive **Car Data Analysis Dashboard** built using **Python, Pandas, Matplotlib, Seaborn, and Streamlit**.
The project performs Exploratory Data Analysis (EDA) on a used-car dataset and presents the results through an easy-to-use multi-page web application.

---

## 📌 Project Overview

The used-car market contains various factors that can influence the value of a vehicle, such as:

* Manufacturing year
* Kilometers driven
* Fuel type
* Transmission type
* Location
* Engine
* Power
* Mileage
* Ownership history

This project analyzes these attributes to understand patterns and relationships within the dataset.

The analysis is presented through a **Streamlit web application** containing three dedicated pages:

1. 🏠 **Introduction**
2. 📊 **Exploratory Data Analysis (EDA)**
3. 📝 **Conclusion / Summary**

---

## 🎯 Objectives

The main objectives of this project are:

* Understand the structure of the used-car dataset.
* Perform data exploration and statistical analysis.
* Identify missing values and data-quality issues.
* Analyze the distribution of car prices.
* Explore car distribution by fuel type and transmission.
* Analyze car availability across different locations.
* Study the relationship between manufacturing year and price.
* Study the relationship between kilometers driven and price.
* Present the analysis through an interactive Streamlit dashboard.

---

## 🖥️ Application Pages

### 🏠 1. Introduction

The Introduction page provides an overview of:

* Project purpose
* Dataset
* Number of records and columns
* Dataset preview
* Important features

---

### 📊 2. Exploratory Data Analysis

The EDA page contains:

#### Dataset Overview

* Number of rows
* Number of columns
* Total missing values

#### Data Preview

Displays sample records from the dataset.

#### Statistical Analysis

Uses descriptive statistics such as:

* Count
* Mean
* Standard deviation
* Minimum
* Maximum
* Quartiles

#### Missing Value Analysis

Identifies columns containing missing values.

#### Visualizations

The dashboard includes visualizations such as:

* 💰 Price Distribution
* ⛽ Fuel Type Distribution
* ⚙️ Transmission Distribution
* 📍 Top Car Locations
* 📅 Manufacturing Year vs Price
* 🛣️ Kilometers Driven vs Price

---

### 📝 3. Conclusion / Summary

The final page summarizes the major observations obtained from the EDA.

It discusses factors such as:

* Car prices
* Vehicle age
* Kilometers driven
* Fuel type
* Transmission
* Location
* Missing values

The project can also be extended into a **Machine Learning-based Car Price Prediction system**.

---

## 📂 Dataset

The project uses a used-car dataset containing information about different vehicles.

### Important Features

| Feature             | Description                     |
| ------------------- | ------------------------------- |
| `Name`              | Name/model of the car           |
| `Location`          | City where the car is available |
| `Year`              | Manufacturing year              |
| `Kilometers_Driven` | Distance driven by the car      |
| `Fuel_Type`         | Type of fuel used               |
| `Transmission`      | Manual or Automatic             |
| `Owner_Type`        | Ownership category              |
| `Mileage`           | Fuel efficiency                 |
| `Engine`            | Engine capacity                 |
| `Power`             | Engine power                    |
| `Seats`             | Number of seats                 |
| `Price`             | Selling price of the car        |

---

## 🛠️ Technologies Used

| Technology      | Purpose                             |
| --------------- | ----------------------------------- |
| 🐍 Python       | Programming language                |
| 🐼 Pandas       | Data manipulation and analysis      |
| 📊 Matplotlib   | Data visualization                  |
| 📈 Seaborn      | Statistical visualization           |
| 🌐 Streamlit    | Interactive web application         |
| 🗃️ CSV         | Dataset format                      |
| 🔧 Git & GitHub | Version control and project hosting |

---

## 📁 Project Structure

```text
Car_Streamlit_App/
│
├── app.py
├── Cars.csv
├── requirements.txt
├── README.md
│
└── pages/
    ├── 1_Introduction.py
    ├── 2_EDA.py
    └── 3_Conclusion.py
```

## 📦 Requirements

The project uses the following Python libraries:

```text
streamlit
pandas
matplotlib
seaborn
```

These are also included in:

```text
requirements.txt
```

---

## 📊 Key Insights

The exploratory analysis helps identify several patterns in the used-car dataset:

* Car prices differ considerably across vehicles.
* Manufacturing year is an important characteristic when analyzing resale prices.
* Kilometers driven can provide useful information about vehicle usage.
* Fuel type and transmission show different distributions within the dataset.
* Car availability varies across different locations.
* Missing values need to be handled carefully before predictive modeling.

> **Note:** These observations are based on exploratory analysis and do not by themselves establish causation.

---

## 🚀 Future Improvements

The project can be further enhanced by adding:

* 🤖 Car Price Prediction using Machine Learning
* 🔍 Interactive filters
* 📈 Additional visualizations
* 📊 Interactive Plotly charts
* 🧹 Advanced data preprocessing
* 🏷️ Brand-wise price analysis
* ⛽ Fuel-type price comparison
* ⚙️ Automatic vs Manual price comparison
* 📍 Location-wise analysis
* 📱 Improved responsive dashboard design
* ☁️ Deployment using Streamlit Community Cloud

---

## 🌐 Deployment

This application can be deployed using **Streamlit Community Cloud**.

General deployment process:

```text
GitHub Repository
        ↓
Streamlit Community Cloud
        ↓
Select app.py
        ↓
Deploy
        ↓
Live Web Application
```

After deployment, the project can be shared through a public URL.

---

## 🎓 Project Use

This project is suitable for:

* Data Analytics portfolio
* Python project
* Exploratory Data Analysis project
* Streamlit project
* College project
* Internship portfolio
* GitHub portfolio
* Resume project

---

## 👩‍💻 Author

**Chetna Rajak**

Aspiring Data Analyst | Python | SQL | Excel | Power BI | Machine Learning

---

## ⭐ If You Like This Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is intended for **educational and portfolio purposes**.

---

### 🔗 Project Workflow

```text
Car Dataset
     ↓
Data Loading
     ↓
Data Exploration
     ↓
Data Cleaning / Missing Value Analysis
     ↓
Statistical Analysis
     ↓
Exploratory Data Analysis
     ↓
Data Visualization
     ↓
Insights & Conclusion
     ↓
Streamlit Dashboard
```
