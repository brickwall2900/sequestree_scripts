#!/usr/bin/env python
# coding: utf-8

# In[2]:

def run(title, rasters, caption, range_min, range_max):
    import streamlit as st
    import leafmap.foliumap as foliumap
    import folium
    from branca.colormap import linear
    from leafmap.foliumap import SplitControl

    st.set_page_config(layout="wide")
    st.title(title)

    biomass_rasters = rasters

    col1, col2 = st.columns(2)
    with col1:
        left_year = st.selectbox("Left Map (Year)", list(biomass_rasters.keys()), index=0)
    with col2:
        right_year = st.selectbox("Right Map (Year)", list(biomass_rasters.keys()), index=len(biomass_rasters)-1)

    m = foliumap.Map(center=[14.65, 121.05], zoom=12, basemap=None, tiles=None)

    print(biomass_rasters[left_year])
    print(biomass_rasters[right_year])
    m.split_map(
        left_layer=biomass_rasters[left_year],
        right_layer=biomass_rasters[right_year],
        left_args={'palette': 'Greens', 'vmin': range_min, 'vmax': range_max},
        right_args={'palette': 'Greens', 'vmin': range_min, 'vmax': range_max},
    )
    colormap = linear.Greens_09.scale(0, 2000)
    colormap.caption = caption

    m.add_colorbar(colors=colormap.colors, vmin=range_min, vmax=range_max, caption=caption)

    m.to_streamlit(height=600)

