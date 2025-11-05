YEARS = ["2020", "2021", "2022", "2023", "2024"]

AGB_DATA_TYPE_MAP = {
    "AGB": "Aboveground Biomass",
    "POTENTIAL": "Tree Carbon Sequestration Potential"
}

AGB_DATA_TYPE_MIN_MAX = {
    "AGB": (0, 2500),
    "POTENTIAL": (0, 2)
}

AGB_DATA_TYPE_CAPTION = {
    "AGB": "Aboveground Biomass (kg)",
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
    "mean": "Average",
    "standard_deviation": "Standard Deviation"
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

VECTOR_FIELDS_COLORED = {
    "AGB": "total_agb",
    "POTENTIAL": "mean",
    "AGB_DENSITY": "total_agb_density",
}

VECTOR_DATA_TYPE_CAPTION = {
    "AGB": "Total AGB (kg)",
    "AGB_DENSITY": "Total AGB Density (Mg/ha)",
    "POTENTIAL": "Tree Carbon Sequestration Potential"
}

TITILER_SERVER = "https://sequestree-titiler-endpoint.hf.space"