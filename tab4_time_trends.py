# components/tab4_time_trends.py
import streamlit as st
import plotly.express as px
import pandas as pd

def show_tab4(df_hist):
    st.subheader("📈 Time Series Trends - How pollution is changing over time")

    if df_hist.empty:
        st.info("Historical data not loaded yet. Please check your ETL table name.")
        return

    pollutant = st.selectbox("Select Pollutant", sorted(df_hist['pollutant'].unique()), key="trend_poll")

    # National Trend
    trend = df_hist[df_hist['pollutant'] == pollutant].groupby('last_update')['avg_val'].mean().reset_index()

    fig = px.line(trend, x='last_update', y='avg_val',
                  title=f"{pollutant} Trend Over Time (National Average)",
                  markers=True, template="plotly_dark")
    fig.update_layout(xaxis_title="Time", yaxis_title="Average Value")
    st.plotly_chart(fig, use_container_width=True)