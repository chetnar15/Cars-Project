import streamlit as st
import pandas as pd

st.set_page_config(page_title="Conclusion", page_icon="📝", layout="wide")
df = pd.read_csv("Cars.csv")

st.title("📝 Conclusion / Summary")

st.subheader("🔑 Key Findings")
st.markdown("""
### 🚗 1. Used-Car Prices
Car prices vary according to several factors, including vehicle age, kilometers driven,
brand/model, fuel type and transmission.

### 📅 2. Manufacturing Year
Newer vehicles generally tend to have higher resale prices than older vehicles.

### 🛣️ 3. Kilometers Driven
Higher usage can be associated with lower resale value.

### ⛽ 4. Fuel Type
The dataset contains multiple fuel categories, allowing comparison of their distribution.

### ⚙️ 5. Transmission
Both Manual and Automatic vehicles are represented in the dataset.

### 📍 6. Location
Car availability differs across cities, showing variation in the used-car market.

### ❌ 7. Missing Values
Some vehicle attributes contain missing values. These should be handled before using the
dataset for machine-learning or predictive modeling.
""")

c1, c2, c3 = st.columns(3)
c1.metric("Total Cars", f"{df.shape[0]:,}")
c2.metric("Features", df.shape[1])
if "Price" in df.columns:
    c3.metric("Average Price", f"{df['Price'].mean():.2f}")

st.success("""
### ✅ Overall Conclusion
EDA helps us understand the used-car market and identify patterns related to car prices.
The analysis can be extended with machine-learning models for used-car price prediction.
""")
