import streamlit as st

def show_tab3(df):
    st.subheader("Analytics & Top Polluted Stations")
    top = df.groupby(['station', 'state', 'region'])['max_val'].max().reset_index()
    top = top.sort_values("max_val", ascending=False).head(15)
    st.dataframe(top, use_container_width=True)

    st.subheader("Full Raw Data")
    st.dataframe(df, use_container_width=True)