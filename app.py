import streamlit as st

st.set_page_config(page_title="Car Data Analysis", page_icon="🚗", layout="wide")

st.title("🚗 Car Data Analysis Dashboard")
st.markdown("""
Welcome to the **Car Data Analysis** Streamlit application.

Use the sidebar to explore:
- 🏠 **Introduction** — project and dataset overview
- 📊 **EDA** — charts, statistics, and data exploration
- 📝 **Conclusion / Summary** — key findings and final insights
""")

st.info("Select a page from the sidebar to begin.")
