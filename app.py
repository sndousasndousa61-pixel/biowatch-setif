import streamlit as st
import pandas as pd
from datetime import date
from supabase import create_client

st.set_page_config(
    page_title="BioWatch Sétif",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 BioWatch Sétif")
st.subheader("AI-assisted monitoring of local pollinator biodiversity")

# -------------------------
# SUPABASE
# -------------------------

try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)
except Exception as e:
    st.error("Supabase connection is not configured.")
    st.stop()

# -------------------------
# ADD OBSERVATION
# -------------------------

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

    pollinator = st.selectbox(
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

    notes = st.text_area("📝 Notes")

    submitted = st.form_submit_button(
        "💾 Save Observation"
    )

# -------------------------
# SAVE
# -------------------------

if submitted:

    try:

        observation = {
            "observation_date": str(observation_date),
            "location": location,
            "latitude": float(latitude),
            "longitude": float(longitude),
            "habitat": habitat,
            "pollinator": pollinator,
            "observation_count": int(count),
            "temperature": float(temperature),
            "notes": notes
        }

        supabase.table(
            "observations"
        ).insert(
            observation
        ).execute()

        st.success("✅ Observation saved successfully!")

        if photo is not None:
            st.image(
                photo,
                caption="Observation photo",
                width=400
            )

    except Exception as e:
        st.error(f"❌ Could
