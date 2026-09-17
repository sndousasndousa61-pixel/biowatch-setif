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

# Create database file if it doesn't exist
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=[
        "Date",
        "Location",
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
        step=0.5
    )

    notes = st.text_area(
        "📝 Notes"
    )

    submitted = st.form_submit_button(
        "💾 Save Observation"
    )

if submitted:

    new_observation = pd.DataFrame([{
        "Date": str(observation_date),
        "Location": location,
        "Habitat": habitat,
        "Pollinator": organism,
        "Count": count,
        "Temperature": temperature,
        "Notes": notes
    }])

    old_data = pd.read_csv(CSV_FILE)
    updated_data = pd.concat(
        [old_data, new_observation],
        ignore_index=True
    )

    updated_data.to_csv(CSV_FILE, index=False)

    st.success("✅ Observation saved successfully!")

st.divider()

st.header("📊 Recorded Observations")

data = pd.read_csv(CSV_FILE)

if len(data) > 0:
    st.dataframe(data, use_container_width=True)
else:
    st.info("No observations recorded yet.")
