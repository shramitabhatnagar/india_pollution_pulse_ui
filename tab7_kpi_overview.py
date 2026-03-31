# components/tab7_kpi_overview.py
import streamlit as st
import plotly.graph_objects as go
from .aqi_utils import calculate_station_aqi   # ← Correct import

def show_tab7(df):
    st.subheader("🎯 AQI Overview & KPIs")

    if df.empty:
        st.warning("No data available for AQI calculation.")
        return

    # Calculate AQI for each station
    aqi_list = []
    for station in df['station'].unique():
        station_data = df[df['station'] == station]
        aqi_list.append(calculate_station_aqi(station_data))

    avg_aqi = int(sum(aqi_list) / len(aqi_list)) if aqi_list else 0

    # KPI Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("National Average AQI", avg_aqi)
    with col2:
        st.metric("Total Stations", len(df['station'].unique()))
    with col3:
        severe = sum(1 for x in aqi_list if x > 300)
        st.metric("Stations in Severe Zone", severe)

    # AQI Gauge Chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_aqi,
        title={"text": "National Air Quality Index"},
        gauge={
            'axis': {'range': [0, 500]},
            'bar': {'color': "darkred"},
            'steps': [
                {'range': [0, 50], 'color': "green"},
                {'range': [51, 100], 'color': "lightgreen"},
                {'range': [101, 200], 'color': "yellow"},
                {'range': [201, 300], 'color': "orange"},
                {'range': [301, 400], 'color': "red"},
                {'range': [401, 500], 'color': "darkred"}
            ]
        }
    ))
    fig.update_layout(template="plotly_dark", height=450)
    st.plotly_chart(fig, use_container_width=True)