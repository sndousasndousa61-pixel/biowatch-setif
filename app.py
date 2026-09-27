import streamlit as st
import pandas as pd
from datetime import date
from supabase import create_client

st.set_page_config(page_title="BioWatch Sétif", page_icon="🌿", layout="wide")

st.title("🌿 BioWatch Sétif")
st.subheader("AI-assisted monitoring of local pollinator biodiversity")

# Supabase connection
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)
except Exception:
    st.error("Supabase connection is not configured.")
    st.stop()

# Add observation
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
        ["Natural area", "Agricultural area", "Urban area"]
    )

    pollinator = st.selectbox(
        "🐝 Pollinator group",
        ["Bee", "Butter
