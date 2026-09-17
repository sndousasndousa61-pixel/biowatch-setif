import streamlit as st
from datetime import date

st.set_page_config(
    page_title="BioWatch Sétif",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 BioWatch Sétif")
st.subheader("AI-assisted monitoring of local pollinator biodiversity")

st.write(
    "A citizen-science platform for monitoring pollinators "
    "under environmental change."
)

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
        value=1,
        step=1
    )

    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        min_value=-20.0,
        max_value=60.0,
        value=20.0,
        step=0.5
    )

    notes = st.text_area(
        "📝 Notes",
        placeholder="Flower visited, behavior, habitat details..."
    )

    submitted = st.form_submit_button(
        "💾 Save Observation"
    )

if submitted:
    st.success("✅ Observation recorded successfully!")

    if photo is not None:
        st.image(
            photo,
            caption="Uploaded observation",
            width=400
        )

    st.write("**Date:**", observation_date)
    st.write("**Location:**", location)
    st.write("**Habitat:**", habitat)
    st.write("**Pollinator:**", organism)
    st
