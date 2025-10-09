#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import importlib

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

choice = st.sidebar.selectbox("Select map to display:", choices)

module_map = {
    choices[0]: "visualization",
    choices[1]: "visualization_copy",
    choices[2]: "visualization_copy_copy",
    choices[3]: "visualization_copy_copy_copy",
    choices[4]: "zonal",
    choices[5]: "zonal_copy",
    choices[6]: "zonal_copy_copy",
    choices[7]: "zonal_copy_copy_copy"
}

module_name = module_map.get(choice)
if module_name:
    thing = importlib.import_module(module_name)
    if hasattr(thing, "show_stuff"):
        thing.show_stuff()
    else:
        st.error("Not implemented!")
else:
    st.error("Selected option not found in module map. This should NOT happen!")