# components/data_loader.py  (Updated version)

import streamlit as st
import pandas as pd
import pyodbc
import os

@st.cache_data(ttl=300)
def load_latest_data():
    conn_str = os.getenv("AZURE_SQL_CONNECTION_STRING")
    if not conn_str:
        st.error("Connection string not found in App Settings.")
        return pd.DataFrame()

    try:
        conn = pyodbc.connect(conn_str)
        df = pd.read_sql("""
            SELECT station, latitude, longitude, pollutant, min_val, max_val, avg_val, last_update, state
            FROM vw_latest_pollution
            WHERE latitude IS NOT NULL AND longitude IS NOT NULL
        """, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Database connection failed: {str(e)}")
        return pd.DataFrame()


@st.cache_data(ttl=300)
def load_historical_data():
    conn_str = os.getenv("AZURE_SQL_CONNECTION_STRING")
    if not conn_str:
        return pd.DataFrame()

    try:
        conn = pyodbc.connect(conn_str)
        df_hist = pd.read_sql("""
            SELECT *
            FROM pollution_raw        -- ← Change to your actual table name
            
        """, conn)
        conn.close()

        df_hist['last_update'] = pd.to_datetime(df_hist['last_update'])
        df_hist['date'] = df_hist['last_update'].dt.date
        df_hist['hour'] = df_hist['last_update'].dt.hour
        return df_hist
    except Exception as e:
        st.warning(f"Historical data load failed: {str(e)}")
        return pd.DataFrame()