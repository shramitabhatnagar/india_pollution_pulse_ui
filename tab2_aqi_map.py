# components/tab2_aqi_map.py
import streamlit as st
import pydeck as pdk
import pandas as pd                    # ← MUST be imported here
from .aqi_utils import get_aqi_color, calculate_station_aqi

def show_tab2(df, regions):
    st.subheader("AQI Map (Colored by Air Quality Index)")

    # Filters
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        all_pollutants = sorted(df['pollutant'].unique())
        selected_pollutants2 = st.multiselect("Pollutants", options=all_pollutants, default=[], key="p2")
    with col2:
        selected_regions2 = st.multiselect("Regions", options=list(regions.keys()), default=[], key="r2")
    with col3:
        all_states = sorted(df['state'].unique())
        selected_states2 = st.multiselect("States", options=all_states, default=[], key="s2")
    with col4:
        top_n2 = st.selectbox("Top N", [5, 10, 15, "All"], index=3, key="t2")

    # Apply Filters
    filtered_df2 = df.copy()
    if selected_pollutants2:
        filtered_df2 = filtered_df2[filtered_df2['pollutant'].isin(selected_pollutants2)]
    if selected_regions2:
        region_states = []
        for reg in selected_regions2:
            region_states.extend(regions[reg])
        filtered_df2 = filtered_df2[filtered_df2['state'].isin(region_states)]
    if selected_states2:
        filtered_df2 = filtered_df2[filtered_df2['state'].isin(selected_states2)]
    if top_n2 != "All":
        top_stations = filtered_df2.groupby('station')['max_val'].max().nlargest(top_n2).index
        filtered_df2 = filtered_df2[filtered_df2['station'].isin(top_stations)]

    # Calculate AQI for each station
    aqi_data = []
    for station in filtered_df2['station'].unique():
        station_data = filtered_df2[filtered_df2['station'] == station]
        aqi = calculate_station_aqi(station_data)
        color = get_aqi_color(aqi)
        row = station_data.iloc[0]
        aqi_data.append({
            'station': station,
            'latitude': row['latitude'],
            'longitude': row['longitude'],
            'state': row['state'],
            'region': row['region'],
            'aqi': aqi,
            'color': color
        })

    map_df2 = pd.DataFrame(aqi_data)

    # Pydeck Map
    view_state = pdk.ViewState(latitude=22.5, longitude=78.5, zoom=4.2, pitch=50)

    india_outline = pdk.Layer(
        "GeoJsonLayer",
        "https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson",
        stroked=True,
        filled=False,
        get_line_color=[100, 100, 100],
        line_width_min_pixels=1.5,
        opacity=0.8
    )

    column_layer = pdk.Layer(
        "ColumnLayer",
        map_df2,
        get_position=["longitude", "latitude"],
        get_elevation="aqi",
        elevation_scale=60,
        radius=16000,
        get_fill_color="color",
        pickable=True,
        auto_highlight=True
    )

    deck = pdk.Deck(
        layers=[india_outline, column_layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/dark-v11",
        tooltip={
            "html": "<b>Station:</b> {station}<br>"
                    "<b>AQI:</b> {aqi}<br>"
                    "<b>Region:</b> {region}<br>"
                    "<b>State:</b> {state}",
            "style": {"background": "#1f2a44", "color": "white", "padding": "12px"}
        }
    )

    st.pydeck_chart(deck)