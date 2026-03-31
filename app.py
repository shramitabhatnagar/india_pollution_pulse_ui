# app.py
import streamlit as st
import time
from components import (
    load_latest_data,
    load_historical_data,
    regions,
    show_tab1,
    show_tab2,
    show_tab3,
    show_tab4,
    show_tab5,
    show_tab6,
    show_tab7
)

st.set_page_config(page_title="India Pollution Pulse", layout="wide", page_icon="🌫️")

st.markdown("""
    <style>
        .stApp { background-color: #0a0a0a; color: #e0e0e0; }
        header { background-color: #0a0a0a !important; }
        h1, h2, h3 { color: #bb86fc !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: #bb86fc;'>🌫️ India Pollution Pulse</h1>", unsafe_allow_html=True)

# Load Data
df = load_latest_data()
df_hist = load_historical_data()

if df.empty:
    st.warning("No recent data found.")
    st.stop()

st.caption(f"Last data fetched: **{df['last_update'].max()}**")

# Add region column
df = df.copy()
df['region'] = df['state'].apply(
    lambda x: next((reg for reg, states in regions.items() if x in states), "Other")
)

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🗺️ All Pollutants Map", 
    "🟥 AQI Map", 
    "📊 Analytics",
    "📈 Time Trends",
    "🏙️ Regional Comparison",
    "⏰ Hourly Patterns",
    "🎯 AQI Overview & KPIs"
])

with tab1:  show_tab1(df, regions)
with tab2:  show_tab2(df, regions)
with tab3:  show_tab3(df)
with tab4:  show_tab4(df_hist)
with tab5:  show_tab5(df)
with tab6:  show_tab6(df_hist)
with tab7:  show_tab7(df)

# Auto Refresh
time.sleep(60)
st.rerun()