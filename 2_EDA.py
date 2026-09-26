import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA", page_icon="📊", layout="wide")
df = pd.read_csv("Cars.csv")

st.title("📊 Exploratory Data Analysis")

c1, c2, c3 = st.columns(3)
c1.metric("Rows", f"{df.shape[0]:,}")
c2.metric("Columns", df.shape[1])
c3.metric("Missing Values", int(df.isnull().sum().sum()))

st.subheader("🔍 Data Preview")
st.dataframe(df.head(10), use_container_width=True)

st.subheader("📈 Numerical Summary")
st.dataframe(df.describe(), use_container_width=True)

st.subheader("❌ Missing Values")
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)
if len(missing):
    st.dataframe(missing.rename("Missing Values").to_frame(), use_container_width=True)
else:
    st.success("No missing values found.")

# Helper to safely find columns
def find_col(*names):
    for n in names:
        if n in df.columns:
            return n
    return None

price = find_col("Price", "price")
fuel = find_col("Fuel_Type", "Fuel Type")
trans = find_col("Transmission", "transmission")
location = find_col("Location", "location")
year = find_col("Year", "year")
kms = find_col("Kilometers_Driven", "Kilometers Driven")

if price:
    st.subheader("💰 Price Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df[price].dropna(), kde=True, ax=ax)
    ax.set_xlabel("Price")
    ax.set_ylabel("Number of Cars")
    st.pyplot(fig)

if fuel:
    st.subheader("⛽ Cars by Fuel Type")
    fig, ax = plt.subplots()
    df[fuel].value_counts().plot(kind="bar", ax=ax)
    ax.set_xlabel("Fuel Type")
    ax.set_ylabel("Number of Cars")
    plt.xticks(rotation=0)
    st.pyplot(fig)

if trans:
    st.subheader("⚙️ Transmission Distribution")
    fig, ax = plt.subplots()
    df[trans].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

if location:
    st.subheader("📍 Top 10 Car Locations")
    fig, ax = plt.subplots()
    df[location].value_counts().head(10).plot(kind="bar", ax=ax)
    ax.set_xlabel("Location")
    ax.set_ylabel("Number of Cars")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)

if year and price:
    st.subheader("📅 Manufacturing Year vs Price")
    plot_df = df[[year, price]].dropna()
    fig, ax = plt.subplots()
    sns.scatterplot(data=plot_df, x=year, y=price, ax=ax)
    ax.set_xlabel("Manufacturing Year")
    ax.set_ylabel("Price")
    st.pyplot(fig)

if kms and price:
    st.subheader("🛣️ Kilometers Driven vs Price")
    plot_df = df[[kms, price]].dropna()
    fig, ax = plt.subplots()
    sns.scatterplot(data=plot_df, x=kms, y=price, ax=ax)
    ax.set_xlabel("Kilometers Driven")
    ax.set_ylabel("Price")
    st.pyplot(fig)
