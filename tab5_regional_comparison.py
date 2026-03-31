# components/tab5_regional_comparison.py
import streamlit as st
import plotly.express as px

def show_tab5(df):
    st.subheader("🏙️ Regional & State Comparison")

    col1, col2 = st.columns(2)

    with col1:
        fig_reg = px.bar(
            df.groupby('region')['max_val'].mean().sort_values(ascending=False).reset_index(),
            x='region', y='max_val',
            title="Average Pollution by Region",
            color='max_val', color_continuous_scale='Reds',
            template="plotly_dark"
        )
        st.plotly_chart(fig_reg, use_container_width=True)

    with col2:
        fig_state = px.bar(
            df.groupby('state')['max_val'].mean().nlargest(10).reset_index(),
            x='max_val', y='state', orientation='h',
            title="Top 10 Most Polluted States",
            template="plotly_dark"
        )
        st.plotly_chart(fig_state, use_container_width=True)