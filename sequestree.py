#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
from data_resolver import DataResolver, LocalDataResolver
import rasters_view
import vectors_view

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

AGB_DATA_TYPE_MAP = {
    "AGB": "Aboveground Biomass",
    "POTENTIAL": "Tree Carbon Sequestration Potential"
}

ZONE_DATA_TYPE_MAP = {
    "AGB": "Tree Biomass and Carbon Stock",
    "AGB_DENSITY": "Tree Biomass and Carbon Stock Density",
    "POTENTIAL": "Tree Carbon Sequestration Potential"
}

MODEL_MAP = {
    "RF": "Random Forest",
    "HYBRID": "Hybrid"
}

VIEW_TYPE_MAP = {
    "BRGY": "Barangay",
    "DIST": "District"
}

OPTION_MAP = {
    "RASTERS": "Raw Maps",
    "VECTORS": "Zonal Maps"
}

AGB_FIELDS = {
    "average_agb": "Average AGB (kg)",
    "standard_deviation": "Standard Deviation (kg)",
    "total_agb": "Total AGB (kg)",
    "total_bgb": "Total BGB (kg)",
    "total_agb_c_stock": "Total AGB C Stock (kg)",
    "total_bgb_c_stock": "Total BGB C Stock (kg)",
    "total_agb_co2_stock": "Total AGB CO₂ Stock (kg)",
    "total_bgb_co2_stock": "Total BGB CO₂ Stock (kg)"
}

POTENTIAL_FIELDS = {
    "mean": "Mean (kg)",
    "standard_deviation": "Standard Deviation (kg)"
}

AGB_DENSITY_FIELDS = {
    "total_agb_density": "Total AGB Density (Mg/ha)",
    "total_bgb_density": "Total BGB Density (Mg/ha)",
    "total_agb_c_stock_density": "Total AGB C Stock Density (Mg/ha)",
    "total_bgb_c_stock_density": "Total BGB C Stock Density (Mg/ha)",
    "total_agb_co2_stock_density": "Total AGB CO₂ Stock Density (Mg/ha)",
    "total_bgb_co2_stock_density": "Total BGB CO₂ Stock Density (Mg/ha)"
}

VECTOR_FIELDS = {
    "BRGY": {
        "AGB": {"barangay": "Barangay"} | AGB_FIELDS,
        "POTENTIAL": {"barangay": "Barangay"} | POTENTIAL_FIELDS,
        "AGB_DENSITY": {"barangay": "Barangay"} | AGB_DENSITY_FIELDS,
    },
    "DIST": {
        "AGB": {"district": "District"} | AGB_FIELDS,
        "POTENTIAL": {"district": "District"} | POTENTIAL_FIELDS,
        "AGB_DENSITY": {"district": "District"} | AGB_DENSITY_FIELDS,
    }
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
    data_type = st.sidebar.selectbox("Data Type", list(AGB_DATA_TYPE_MAP.keys()), format_func=map_to_value(AGB_DATA_TYPE_MAP))
    model = st.sidebar.selectbox("Model", list(MODEL_MAP.keys()), format_func=map_to_value(MODEL_MAP))

    folder_name = f"{option_selected}/{data_type}_{model}/"

    ext = ".tif"
    result = {year: data_resolver.resolve_file(folder_name + year + ext) for year in YEARS}

    if data_type == "AGB":
        rasters_view.run(result, "Aboveground Biomass (kg)", 0, 2500)
    elif data_type == "POTENTIAL":
        rasters_view.run(result, "Tree Carbon Sequestration Potential", 0, 2)
    else:
        raise TypeError("Unknown data type: " + data_type)
elif option_selected == "VECTORS":
    data_type = st.sidebar.selectbox("Data Type", list(ZONE_DATA_TYPE_MAP.keys()), format_func=map_to_value(ZONE_DATA_TYPE_MAP))
    view_type = st.sidebar.selectbox("View Type", list(VIEW_TYPE_MAP.keys()), format_func=map_to_value(VIEW_TYPE_MAP))
    model = st.sidebar.selectbox("Model", list(MODEL_MAP.keys()), format_func=map_to_value(MODEL_MAP))

    folder_name = f"{option_selected}/{data_type}_{model}_{view_type}/"

    ext = ".gpkg"
    result = {year: data_resolver.resolve_file(folder_name + year + ext) for year in YEARS}

    fields = VECTOR_FIELDS[view_type][data_type]
    field_colored = ""
    match data_type:
        case "AGB":
            field_colored = "total_agb"
        case "POTENTIAL":
            field_colored = "mean"
        case "AGB_DENSITY":
            field_colored = "total_agb_density"
        case _:
            raise TypeError("Should NOT happen!")

    vectors_view.run(result, field_colored, fields)