import streamlit as st

st.set_page_config(
    page_title="BioWatch Sétif",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 BioWatch Sétif")

st.subheader("Digital monitoring of local pollinator biodiversity")

st.write(
    "A citizen-science platform for collecting and exploring "
    "pollinator observations."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("📸 Add Observation")
    st.write("Record a new biodiversity observation.")

with col2:
    st.header("🗺️ Explore Biodiversity")
    st.write("Explore observations and biodiversity patterns.")
