# components/tab1_map.py
import streamlit as st
import pydeck as pdk
import pandas as pd

def show_tab1(df, regions):
    st.subheader("All Pollutants Map")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        all_pollutants = sorted(df['pollutant'].unique())
        selected_pollutants1 = st.multiselect("Pollutants", options=all_pollutants, default=[], key="p1")
    with col2:
        selected_regions1 = st.multiselect("Regions", options=list(regions.keys()), default=[], key="r1")
    with col3:
        all_states = sorted(df['state'].unique())
        selected_states1 = st.multiselect("States", options=all_states, default=[], key="s1")
    with col4:
        top_n1 = st.selectbox("Top N", [5, 10, 15, "All"], index=3, key="t1")

    filtered_df1 = df.copy()
    if selected_pollutants1:
        filtered_df1 = filtered_df1[filtered_df1['pollutant'].isin(selected_pollutants1)]
    if selected_regions1:
        region_states = []
        for reg in selected_regions1:
            region_states.extend(regions[reg])
        filtered_df1 = filtered_df1[filtered_df1['state'].isin(region_states)]
    if selected_states1:
        filtered_df1 = filtered_df1[filtered_df1['state'].isin(selected_states1)]
    if top_n1 != "All":
        top_stations = filtered_df1.groupby('station')['max_val'].max().nlargest(top_n1).index
        filtered_df1 = filtered_df1[filtered_df1['station'].isin(top_stations)]

    map_df1 = filtered_df1.groupby(['station', 'latitude', 'longitude']).agg({
        'max_val': 'max', 'min_val': 'min', 'avg_val': 'mean',
        'pollutant': lambda x: ', '.join(sorted(x.unique())),
        'last_update': 'max', 'state': 'first', 'region': 'first'
    }).reset_index()

    def tooltip1(row):
        station_data = filtered_df1[filtered_df1['station'] == row['station']]
        lines = [f"{r['pollutant']}: min {r['min_val'] or 'N/A'} / max {r['max_val'] or 'N/A'} / avg {r['avg_val'] or 'N/A'}" 
                 for _, r in station_data.iterrows()]
        return f"<b>Station:</b> {row['station']}<br><b>Region:</b> {row['region']}<br><b>State:</b> {row['state']}<br><br>" + "<br>".join(lines)

    map_df1['tooltip_details'] = map_df1.apply(tooltip1, axis=1)

    view_state = pdk.ViewState(latitude=22.5, longitude=78.5, zoom=4.2, pitch=50)

    india_outline = pdk.Layer(
        "GeoJsonLayer",
        "https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson",
        stroked=True, filled=False, get_line_color=[100, 100, 100],
        line_width_min_pixels=1.5, opacity=0.8
    )

    column_layer = pdk.Layer(
        "ColumnLayer", map_df1,
        get_position=["longitude", "latitude"],
        get_elevation="max_val", elevation_scale=800, radius=15000,
        get_fill_color=[255, 80, 60], pickable=True, auto_highlight=True
    )

    deck = pdk.Deck(
        layers=[india_outline, column_layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/dark-v11",
        tooltip={"html": "{tooltip_details}", "style": {"background": "#1f2a44", "color": "white", "padding": "12px"}}
    )

    st.pydeck_chart(deck)