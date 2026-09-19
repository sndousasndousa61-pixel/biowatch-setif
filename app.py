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

# =========================
# CREATE DATA FILE
# =========================

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


# =========================
# ADD OBSERVATION
# =========================

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
    )

    submitted = st.form_submit_button(
        "💾 Save Observation"
    )


# =========================
# SAVE OBSERVATION
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
# LOAD DATA
# =========================

data = pd.read_csv(CSV_FILE)

# Make sure old data has all required columns
required_columns = [
    "Date",
    "Location",
    "Latitude",
    "Longitude",
    "Habitat",
    "Pollinator",
    "Count",
    "Temperature",
    "Notes"
]

for column in required_columns:
    if column not in data.columns:
        data[column] = None


# =========================
# MAP
# =========================

st.divider()
st.header("🗺️ Biodiversity Map")

map_data = data[
    ["Latitude", "Longitude"]
].copy()

map_data["Latitude"] = pd.to_numeric(
    map_data["Latitude"],
    errors="coerce"
)

map_data["Longitude"] = pd.to_numeric(
    map_data["Longitude"],
    errors="coerce"
)

map_data = map_data.dropna()

if not map_data.empty:

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


# =========================
# OBSERVATIONS TABLE
# =========================

st.divider()
st.header("📋 Recorded Observations")

if not data.empty:

    st.dataframe(
        data,
        use_container_width=True
    )

else:

    st.info(
        "No observations recorded yet."
    )


# =========================
# DASHBOARD
# =========================

st.divider()
st.header("📊 Biodiversity Dashboard")

# Habitat filter
habitat_filter = st.selectbox(
    "🌱 Filter by habitat",
    [
        "All",
        "Natural area",
        "Agricultural area",
        "Urban area"
    ]
)

# Apply filter
if habitat_filter == "All":

    dashboard_data = data

else:

    dashboard_data = data[
        data["Habitat"] == habitat_filter
    ]


if not dashboard_data.empty:

    # -------------------------
    # KEY INDICATORS
    # -------------------------

    total_observations = len(
        dashboard_data
    )

    total_individuals = int(
        pd.to_numeric(
            dashboard_data["Count"],
            errors="coerce"
        ).fillna(0).sum()
    )

    pollinator_groups = dashboard_data[
        "Pollinator"
    ].nunique()

    habitats = dashboard_data[
        "Habitat"
    ].nunique()

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


    # -------------------------
    # POLLINATOR CHART
    # -------------------------

    st.subheader(
        "🐝 Observations by Pollinator Group"
    )

    pollinator_counts = (
        dashboard_data["Pollinator"]
        .value_counts()
    )

    st.bar_chart(
        pollinator_counts
    )


    # -------------------------
    # HABITAT CHART
    # -------------------------

    st.subheader(
        "🌱 Observations by Habitat"
    )

    habitat_counts = (
        dashboard_data["Habitat"]
        .value_counts()
    )

    st.bar_chart(
        habitat_counts
    )

else:

    st.info(
        "No observations available for this habitat."
)
