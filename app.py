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

# Create database file if it does not exist
if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=[
        "Date",
        "Location",
        "Latitude",
        "Longitude",
        "Habitat",
        "Pollinator",
        "Count",
        "Temperature",
        "Notes"
    ]).to_csv(CSV_FILE, index=False)

st.divider()

# =========================
# ADD OBSERVATION
# =========================

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
            value=36.190000,
            format="%.6f"
        )

    with col2:
        longitude = st.number_input(
            "🌐 Longitude",
            value=5.410000,
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
        "📝 Notes"
    )# =========================
# DASHBOARD
# =========================

st.divider()

st.header("📊 Biodiversity Dashboard")

if not data.empty:

    total_observations = len(data)
    total_individuals = int(data["Count"].sum())
    pollinator_groups = data["Pollinator"].nunique()
    habitats = data["Habitat"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🔎 Observations",
            total_observations
        )

    with col2:
        st.metric(
            "🐝 Individuals",
            total_individuals
        )

    with col3:
        st.metric(
            "🌿 Pollinator groups",
            pollinator_groups
        )

    with col4:
        st.metric(
            "🏞️ Habitats",
            habitats
        )

    st.subheader("🐝 Observations by Pollinator Group")

    pollinator_counts = data["Pollinator"].value_counts()

    st.bar_chart(pollinator_counts)

    st.subheader("🌱 Observations by Habitat")

    habitat_counts = data["Habitat"].value_counts()

    st.bar_chart(habitat_counts)

else:

    st.info(
        "Add observations to see the biodiversity dashboard."
    )

    submitted = st.form_submit_button(
        "💾 Save Observation"
    )


# =========================
# SAVE
# =========================

if submitted:

    new_observation = pd.DataFrame({
        "Date": [str(observation_date)],
        "Location": [location],
        "Latitude": [float(latitude)],
        "Longitude": [float(longitude)],
        "Habitat": [habitat],
        "Pollinator": [organism],
        "Count": [int(count)],
        "Temperature": [float(temperature)],
        "Notes": [notes]
    })

    data = pd.read_csv(CSV_FILE)

    # Make sure old files have the new columns
    for column in new_observation.columns:
        if column not in data.columns:
            data[column] = None

    data = pd.concat(
        [data, new_observation],
        ignore_index=True
    )

    data.to_csv(
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


# =========================
# MAP
# =========================

st.divider()

st.header("🗺️ Biodiversity Map")

data = pd.read_csv(CSV_FILE)

if "Latitude" in data.columns and "Longitude" in data.columns:

    map_data = data[[
        "Latitude",
        "Longitude"
    ]].copy()

    map_data["Latitude"] = pd.to_numeric(
        map_data["Latitude"],
        errors="coerce"
    )

    map_data["Longitude"] = pd.to_numeric(
        map_data["Longitude"],
        errors="coerce"
    )

    map_data = map_data.dropna()

    if len(map_data) > 0:

        st.map(
            map_data,
            latitude="Latitude",
            longitude="Longitude",
            zoom=11
        )

    else:

        st.info(
            "Add an observation with coordinates to display the map."
        )

else:

    st.info(
        "Map coordinates are not available yet."
    )


# =========================
# TABLE
# =========================

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
