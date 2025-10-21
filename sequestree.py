#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
from data_resolver import DataResolver, LocalDataResolver
import rasters_view

st.title("Spatial Assessment and Backcasting of Tree Carbon Sequestration (CS) in Quezon City, Philippines")

choices = [
    "Tree Biomass and Carbon Stock of Quezon City, Philippines - Random Forest Predictions",
    "Tree Biomass and Carbon Stock of Quezon City, Philippines - Geographically Weighted Regression Predictions",
    "Tree Carbon Sequestration Potential of Quezon City, Philippines - Random Forest Predictions",
    "Tree Carbon Sequestration Potential of Quezon City Philippines - Geographically Weighted Regression Predictions",
    "Tree Biomass and Carbon Stock of Quezon City, Philippines Per Zone - Random Forest Predictions",
    "Tree Biomass and Carbon Stock of Quezon City, Philippines Per Zone - Geographically Weighted Regression Predictions",
    "Tree Carbon Sequestration Potential of Quezon City, Philippines Per Zone - Random Forest Predictions",
    "Tree Carbon Sequestration Potential of Quezon City, Philippines Per Zone - Geographically Weighted Regression Predictions"
]

# options
data_resolver = DataResolver(LocalDataResolver())

DATA_TYPE_MAP = {
    "AGB": "Aboveground Biomass",
    "POTENTIAL": "Tree Carbon Sequestration Potential"
}

MODEL_MAP = {
    "RF": "Random Forest",
    "HYBRID": "Hybrid"
}

OPTION_MAP = {
    "RASTERS": "Raw Maps",
    "VECTORS": "Zonal Maps"
}

def map_to_value(dict):
    def _do_stuff(input):
        return dict[input]
    return _do_stuff

YEARS = ["2020", "2021", "2022", "2023", "2024"]

option_selected = st.sidebar.selectbox("Choose:", list(OPTION_MAP.keys()), format_func=map_to_value(OPTION_MAP))
if option_selected == "RASTERS":
    # there are different sidebar options
    # above ground biomass, tree cabon seq potential
    data_type = st.sidebar.selectbox("Data type", list(DATA_TYPE_MAP.keys()), format_func=map_to_value(DATA_TYPE_MAP))
    model = st.sidebar.selectbox("Model", list(MODEL_MAP.keys()), format_func=map_to_value(MODEL_MAP))

    folder_name = f"{option_selected}/{data_type}_{model}/"

    ext = ".tif"
    result = {year: data_resolver.resolve_file(folder_name + year + ext) for year in YEARS}

    if data_type == "AGB":
        rasters_view.run("title here", result, "Aboveground Biomass (kg)", 0, 2500)
    elif data_type == "POTENTIAL":
        rasters_view.run("title here", result, "Tree Carbon Sequestration Potential", 0, 2)
    else:
        raise TypeError("Unknown data type: " + data_type)