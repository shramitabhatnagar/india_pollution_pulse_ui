# components/tab6_hourly_patterns.py
import streamlit as st
import plotly.express as px

def show_tab6(df_hist):
    st.subheader("⏰ Hourly & Daily Pollution Patterns")

    if df_hist.empty:
        st.info("Historical data not available.")
        return

    # Hourly Heatmap
    fig_heat = px.density_heatmap(
        df_hist, x='hour', y='pollutant', z='avg_val',
        title="Average Pollution Level by Hour of the Day",
        color_continuous_scale='Viridis', template="plotly_dark"
    )
    st.plotly_chart(fig_heat, use_container_width=True)

    # Daily Trend
    daily = df_hist.groupby(['date', 'pollutant'])['avg_val'].mean().reset_index()
    fig_daily = px.line(daily, x='date', y='avg_val', color='pollutant',
                        title="Daily Average Pollution Trend by Pollutant",
                        template="plotly_dark")
    st.plotly_chart(fig_daily, use_container_width=True)