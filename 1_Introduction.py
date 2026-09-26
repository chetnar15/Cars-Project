import streamlit as st
import pandas as pd

st.set_page_config(page_title="Introduction", page_icon="🏠", layout="wide")

df = pd.read_csv("Cars.csv")

st.title("🏠 Introduction")
st.markdown("""
### 🚗 About the Project
This project explores a used-car dataset using **Python, Pandas, Matplotlib, Seaborn and Streamlit**.

The goal is to understand the dataset, identify patterns in car prices and explore factors such as
manufacturing year, kilometers driven, fuel type, transmission and location.
""")

c1, c2, c3 = st.columns(3)
c1.metric("Total Records", f"{df.shape[0]:,}")
c2.metric("Total Columns", df.shape[1])
c3.metric("Target Variable", "Price")

st.subheader("📋 Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)

st.subheader("🔎 Main Features")
st.markdown("""
- **Name** — Car model/name
- **Location** — City where the car is available
- **Year** — Manufacturing year
- **Kilometers_Driven** — Distance driven
- **Fuel_Type** — Fuel category
- **Transmission** — Manual or Automatic
- **Owner_Type** — Ownership category
- **Mileage, Engine, Power** — Vehicle specifications
- **Seats** — Number of seats
- **Price** — Used-car selling price
""")
