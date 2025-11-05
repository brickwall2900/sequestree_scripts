import streamlit as st
from data_resolver import *
import views.vectors_view as vectors_view
import views.rasters_view as rasters_view
from config import *

st.title("Spatial Assessment and Backcasting of Tree Carbon Sequestration (CS) in Quezon City, Philippines")

# options
data_resolver = DataResolver(RemoteDataResolver())

def map_to_value(dict):
    def _do_stuff(input):
        return dict[input]
    return _do_stuff

def build_year_dict(ext):
    return {year: data_resolver.resolve_file(folder_name + year + ext) for year in YEARS}

option_selected = st.sidebar.selectbox("Choose:", list(OPTION_MAP.keys()), format_func=map_to_value(OPTION_MAP))
if option_selected == "RASTERS":
    # there are different sidebar options
    # above ground biomass, tree cabon seq potential
    data_type = st.sidebar.selectbox("Data Type:", list(AGB_DATA_TYPE_MAP.keys()), format_func=map_to_value(AGB_DATA_TYPE_MAP), key="_sq_data_type")
    model = st.sidebar.selectbox("Model:", list(MODEL_MAP.keys()), format_func=map_to_value(MODEL_MAP), key="_sq_model")

    folder_name = f"{option_selected}/{data_type}_{model}/"

    ext = ".tif"
    files = build_year_dict(ext)

    min, max = AGB_DATA_TYPE_MIN_MAX[data_type]
    caption = AGB_DATA_TYPE_CAPTION[data_type]

    print(f"The files are is {files}")

    rasters_view.run(files, caption, min, max)
elif option_selected == "VECTORS":
    data_type = st.sidebar.selectbox("Data Type:", list(ZONE_DATA_TYPE_MAP.keys()), format_func=map_to_value(ZONE_DATA_TYPE_MAP), key="_sq_data_type")
    view_type = st.sidebar.selectbox("View Type:", list(VIEW_TYPE_MAP.keys()), format_func=map_to_value(VIEW_TYPE_MAP), key="_sq_view_type")
    model = st.sidebar.selectbox("Model:", list(MODEL_MAP.keys()), format_func=map_to_value(MODEL_MAP), key="_sq_model")

    folder_name = f"{option_selected}/{data_type}_{model}_{view_type}/"

    ext = ".gpkg"
    files = build_year_dict(ext)

    fields = VECTOR_FIELDS[view_type][data_type]
    field_colored = VECTOR_FIELDS_COLORED[data_type]
    legend = VECTOR_DATA_TYPE_CAPTION[data_type]

    vectors_view.run(files, field_colored, fields, legend)