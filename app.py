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

FILE = "observations.csv"

COLUMNS = [
    "Date", "Location", "Latitude", "Longitude",
    "Habitat", "Pollinator", "Count",
    "Temperature", "Notes"
]

if not os.path.exists(FILE):
    pd.DataFrame(columns=COLUMNS).to_csv(FILE, index=False)

data = pd.read_csv(FILE)

st.divider()
st.header("📸 Add Observation")

with st.form("observation_form"):

    photo = st.file_uploader(
        "📷 Upload a pollinator photo",
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

    c1, c2 = st.columns(2)

    with c1:
        latitude = st.number_input(
            "🌐 Latitude",
            value=36.190000,
            format="%.6f"
        )

    with c2:
        longitude = st.number_input(
            "🌐 Longitude",
            value=5.410000,
            format="%.6f"
        )

    habitat = st.selectbox(
        "🌱 Habitat",
        ["Natural area", "Agricultural area", "Urban area"]
    )

    pollinator = st.selectbox(
        "🐝 Pollinator group",
        ["Bee", "Butterfly", "Hoverfly", "Other", "Unknown"]
    )

    count = st.number_input(
        "🔢 Number of individuals",
        min_value=1,
        value=1
    )

    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        value=20.0
    )

    notes = st.text_area(
        "📝 Notes",
        placeholder="Write your observation here..."
    )

    save = st.form_submit_button("💾 Save Observation")

if save:

    new_row = pd.DataFrame([{
        "Date": str(observation_date),
        "Location": location,
        "Latitude": latitude,
        "Longitude": longitude,
        "Habitat": habitat,
        "Pollinator": pollinator,
        "Count": count,
        "Temperature": temperature,
        "Notes": notes
    }])

    data = pd.concat([data, new_row], ignore_index=True)
    data.to_csv(FILE, index=False)

    st.success("✅ Observation saved successfully!")

    if photo:
        st.image(
            photo,
            caption="Uploaded pollinator observation",
            width=400
        )

st.divider()
st.header("🗺️ Biodiversity Map")

if not data.empty:

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
        st.map(map_data)
    else:
        st.info("No valid coordinates available.")

else:
    st.info("Add observations to display the biodiversity map.")

st.divider()
st.header("📊 Biodiversity Dashboard")

if not data.empty:

    f1, f2 = st.columns(2)

    with f1:
        habitat_filter = st.selectbox(
            "🌱 Filter by habitat",
            ["All"] + sorted(data["Habitat"].dropna().unique().tolist())
        )

    with f2:
        pollinator_filter = st.selectbox(
            "🐝 Filter by pollinator",
            ["All"] + sorted(data["Pollinator"].dropna().unique().tolist())
        )

    filtered = data.copy()

    if habitat_filter != "All":
        filtered = filtered[
            filtered["Habitat"] == habitat_filter
        ]

    if pollinator_filter != "All":
        filtered = filtered[
            filtered["Pollinator"] == pollinator_filter
        ]

    a, b, c, d = st.columns(4)

    with a:
        st.metric("🔎 Observations", len(filtered))

    with b:
        st.metric(
            "🐝 Individuals",
            int(pd.to_numeric(
                filtered["Count"],
                errors="coerce"
            ).fillna(0).sum())
        )

    with c:
        st.metric(
            "🦋 Pollinator groups",
            filtered["Pollinator"].nunique()
        )

    with d:
        st.metric(
            "🌱 Habitats",
            filtered["Habitat"].nunique()
        )

    st.subheader("🐝 Pollinator groups")
    st.bar_chart(
        filtered["Pollinator"].value_counts()
    )

    st.subheader("🌱 Habitats")
    st.bar_chart(
        filtered["Habitat"].value_counts()
    )

    st.subheader("📋 Observation Records")
    st.dataframe(
        filtered,
        use_container_width=True
    )

    csv = filtered.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download observations CSV",
        csv,
        "biowatch_setif_observations.csv",
        "text/csv"
    )

else:
    st.info("No observations recorded yet.")

st.divider()
st.caption(
    "BioWatch Sétif — Digital monitoring of pollinator biodiversity "
    "under environmental change."
)
