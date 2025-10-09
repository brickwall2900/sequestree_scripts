#!/usr/bin/env python
# coding: utf-8

# In[2]:

def show_stuff():

    import streamlit as st
    import leafmap.foliumap as leafmap
    import folium
    from branca.colormap import linear
    from leafmap.foliumap import SplitControl

    st.set_page_config(layout="wide")
    st.title("Tree Carbon Sequestration Potential of Quezon City, Philippines - Random Forest Predictions")

    biomass_rasters = {
        "2020": "",
        "2021": "",
        "2022": "",
        "2023": "",
        "2024": "",
    }

    col1, col2 = st.columns(2)
    with col1:
        left_year = st.selectbox("Left Map (Year)", list(biomass_rasters.keys()), index=0)
    with col2:
        right_year = st.selectbox("Right Map (Year)", list(biomass_rasters.keys()), index=len(biomass_rasters)-1)

    m = leafmap.Map(center=[14.65, 121.05], zoom=12, basemap=None, tiles=None)

    m.split_map(
        left_layer=biomass_rasters[left_year],
        right_layer=biomass_rasters[right_year],
        left_args={'palette': 'Greens', 'vmin': 0, 'vmax': 2.5},
        right_args={'palette': 'Greens', 'vmin': 0, 'vmax': 2.5},
    )
    colormap = linear.Greens_09.scale(0, 2.5)
    colormap.caption = "CS Potential Score"
    green_palette = colormap.colors  

    m.add_colorbar(colors=colormap.colors, vmin=0, vmax=2.5, caption="CS Potential Score")

    m.to_streamlit(height=600)
