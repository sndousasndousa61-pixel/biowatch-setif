import streamlit as st
import pandas as pd
from datetime import date
import os

st.set_page_config(
    page_title="BioWatch Sétif",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 BioWatch Sétif")
st.subheader("AI-assisted monitoring of local pollinator biodiversity")

CSV_FILE = "observations.csv"

# Create database
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=[
        "Date",
        "Location",
        "Latitude",
        "Longitude",
        "Habitat",
        "Pollinator",
        "Count",
        "Temperature",
        "Notes"
    ])
    df.to_csv(CSV_FILE, index=False)

st.divider()

st.header("📸 Add Observation")

with st.form("observation_form"):

    photo = st.file_uploader(
        "📷 Upload a photo",
        type=["jpg", "jpeg", "png"]
    )

    observation_date = st.date_input(
        "📅 Date",
        value=date.today()
    )

    location = st.text_input(
        "📍 Location",
        placeholder="Example: Sétif"
    )

    col1, col2 = st.columns(2)

    with col1:
        latitude = st.number_input(
            "🌐 Latitude",
            value=36.1900,
            format="%.6f"
        )

    with col2:
        longitude = st.number_input(
            "🌐 Longitude",
            value=5.4100,
            format="%.6f"
        )

    habitat = st.selectbox(
        "🌱 Habitat type",
        [
            "Natural area",
            "Agricultural area",
            "Urban area"
        ]
    )

    organism = st.selectbox(
        "🐝 Pollinator group",
        [
            "Bee",
            "Butterfly",
            "Hoverfly",
            "Other",
            "Unknown"
        ]
    )

    count = st.number_input(
        "🔢 Number of individuals",
        min_value=1,
        value=1
    )

    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        value=20.0,
        step=0
