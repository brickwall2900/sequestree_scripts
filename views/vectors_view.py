import geopandas as gpd  
import streamlit as st
import folium
import mapclassify
from folium.features import GeoJsonTooltip
from branca.colormap import StepColormap
from streamlit_folium import st_folium

def run(files, field_color_col, fields_alias_map: dict, legend):
    st.set_page_config(layout="wide")

    gpkg_files = files

    selected_year = st.selectbox("Select Year", list(gpkg_files.keys()), index=len(gpkg_files)-1)

    gdf = gpd.read_file(gpkg_files[selected_year])
    color_column = field_color_col

    classifier = mapclassify.Quantiles(gdf[color_column].dropna(), k=5)
    labels = ["Very Low", "Low", "Moderate", "High", "Very High"]
    bin_edges = classifier.bins

    colors = ["#AF0000", "#AF6000", "#AFA300", "#86AF00", "#027621"]

    colormap = StepColormap(
        colors=colors,
        index=bin_edges,
        vmin=gdf[color_column].min(),
        vmax=gdf[color_column].max()
    )

    def add_custom_legend(m, colors, labels, title):
        legend_html = f"""
        <div style="
            position: fixed; 
            bottom: 50px; left: 50px; width: 220px; 
            z-index:9999; font-size:14px;
            background-color: white; padding: 10px; border:2px solid grey;
            color: black;
            border-radius: 5px;
        ">
            <b>{title}</b><br>
        """
        for color, label in zip(colors, labels):
            legend_html += f"""
            <div style="display:flex; align-items:center; margin:2px 0;">
                <div style="width:20px; height:20px; background-color:{color}; 
                            margin-right:8px; border:1px solid black;"></div>
                {label}
            </div>
            """
        legend_html += "</div>"
        m.get_root().html.add_child(folium.Element(legend_html))

    m = folium.Map(location=[14.65, 121.05], zoom_start=12, tiles=None)

    def style_function(feature):
        val = feature["properties"].get(color_column)
        if val is None:
            return {"fillColor": "#ffffff", "color": "black", "weight": 1, "fillOpacity": 0.0}
        try:
            fill = colormap(val)
        except Exception:
            fill = "#ffffff"
        return {"fillColor": fill, "color": "black", "weight": 1, "fillOpacity": 0.7}

    folium.GeoJson(
        gdf,
        style_function=style_function,
        tooltip=GeoJsonTooltip(
            fields=list(fields_alias_map.keys()),
            aliases=list(fields_alias_map.values()),
            localize=True,
            sticky=True
        ),
        name=f"Barangay Statistics {selected_year}"
    ).add_to(m)

    add_custom_legend(m, colors, labels, legend + f" - {selected_year} (Quantile)")

    st_folium(m, width=1200, height=700)