import streamlit as st
from src.forecast_demand import forecast_demand

st.title("📊 GenAI Demand Forecast Dashboard")
df = forecast_demand("data/demand.csv")
st.line_chart(df.set_index("ds")["yhat"])
