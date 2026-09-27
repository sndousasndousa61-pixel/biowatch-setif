import streamlit as st

st.set_page_config(
    page_title="BioWatch Setif",
    page_icon="🌿"
)

st.title("🌿 BioWatch Sétif")

st.header("📸 Add Observation")

st.write("Pollinators: Bees, Butterflies, Hoverflies and other insects.")

location = st.text_input("📍 Location")

habitat = st.selectbox(
    "🌱 Habitat",
    ["Natural", "Agricultural", "Urban"]
)

pollinator = st.selectbox(
    "🐝 Pollinator",
    ["Bee", "Butterfly", "Hoverfly", "Other", "Unknown"]
)

count = st.number_input(
    "Number of individuals",
    min_value=1,
    value=1
)

if st.button("Save Observation"):
    st.success("Observation recorded successfully!")

st.divider()

st.header("🗺️ Biodiversity Map")
st.info("Map module")

st.header("📊 Biodiversity Dashboard")
st.info("Dashboard module")
