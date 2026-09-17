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

# Create the observations file
if not os.path.exists(CSV_FILE):
    empty_data = pd.DataFrame(columns=[
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
    empty_data.to_csv(CSV_FILE, index=False)

st.divider()

# -------------------------
# ADD OBSERVATION
# -------------------------

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
        value=1,
        step=1
    )

    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        value=20.0,
        step=0.5
    )

    notes = st.text_area(
        "📝 Notes",
        placeholder="Write your observations here..."
    )

    submitted = st.form_submit_button(
        "💾 Save Observation"
    )


# -------------------------
# SAVE OBSERVATION
# -------------------------

if submitted:

    new_observation = pd.DataFrame({
        "Date": [str(observation_date)],
        "Location": [location],
        "Latitude": [latitude],
        "Longitude": [longitude],
        "Habitat": [habitat],
        "Pollinator": [organism],
        "Count": [count],
        "Temperature": [temperature],
        "Notes": [notes]
    })

    old_data = pd.read_csv(CSV_FILE)

    updated_data = pd.concat(
        [old_data, new_observation],
        ignore_index=True
    )

    updated_data.to_csv(
        CSV_FILE,
        index=False
    )

    st.success("✅ Observation saved successfully!")

    if photo is not None:
        st.image(
            photo,
            caption="Observation photo",
            width=400
        )
# -------------------------
# BIODIVERSITY MAP
# -------------------------

st.divider()

st.header("🗺️ Biodiversity Map")

data = pd.read_csv(CSV_FILE)

# Add missing coordinate columns to old data
if "Latitude" not in data.columns:
    data["Latitude"] = None

if "Longitude" not in data.columns:
    data["Longitude"] = None

data.to_csv(CSV_FILE, index=False)

map_data = data[
    ["Latitude", "Longitude"]
].dropna()

if not map_data.empty:
    st.map(
        map_data,
        zoom=11
    )
else:
    st.info(
        "No coordinates available for the map yet."
    )


# -------------------------
# OBSERVATIONS TABLE
# -------------------------

st.divider()

st.header("📊 Recorded Observations")

data = pd.read_csv(CSV_FILE)

if not data.empty:

    st.dataframe(
        data,
        use_container_width=True
    )

else:

    st.info(
        "No observations recorded yet."
    )
