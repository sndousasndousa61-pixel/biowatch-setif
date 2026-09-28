import streamlit as st
import pandas as pd
from datetime import date
from supabase import create_client

st.set_page_config(page_title="BioWatch Sétif", page_icon="🌿", layout="wide")

st.title("🌿 BioWatch Sétif")
st.caption("AI-assisted monitoring of local pollinator biodiversity")

try:
    db = create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )
except Exception as e:
    st.error("❌ Supabase connection problem")
    st.write(str(e))
    st.stop()

st.divider()
st.header("📸 Add Observation")

with st.form("observation_form"):
    photo = st.file_uploader("📷 Upload a photo", type=["jpg", "jpeg", "png"])
    d = st.date_input("📅 Date", date.today())
    location = st.text_input("📍 Location", "Sétif")

    c1, c2 = st.columns(2)
    lat = c1.number_input("Latitude", value=36.190000, format="%.6f")
    lon = c2.number_input("Longitude", value=5.410000, format="%.6f")

    habitat = st.selectbox(
        "🌱 Habitat",
        ["Natural area", "Agricultural area", "Urban area"]
    )

    pollinator = st.selectbox(
        "🐝 Pollinator group",
        ["Bee", "Butterfly", "Hoverfly", "Other", "Unknown"]
    )

    count = st.number_input("🔢 Number of individuals", 1, 1000, 1)
    temperature = st.number_input("🌡️ Temperature °C", 0.0, 60.0, 20.0)
    notes = st.text_area("📝 Notes")

    save = st.form_submit_button("💾 Save Observation")

if save:
    row = {
        "observation_date": str(d),
        "location": location,
        "latitude": float(lat),
        "longitude": float(lon),
        "habitat": habitat,
        "pollinator": pollinator,
        "observation_count": int(count),
        "temperature": float(temperature),
        "notes": notes
    }

    try:
        db.table("observations").insert(row).execute()
        st.success("✅ Observation saved successfully!")

        if photo:
            st.image(photo, caption="Observation photo", width=400)

    except Exception as e:
        st.error("❌ Could not save observation")
        st.write(str(e))

st.divider()
st.header("🗺️ Biodiversity Map")

try:
    result = (
        db.table("observations")
        .select("*")
        .order("observation_date", desc=True)
        .execute()
    )

    data = pd.DataFrame(result.data)

except Exception as e:
    st.error("❌ Could not load observations")
    st.write(str(e))
    data = pd.DataFrame()

if not data.empty:
    map_data = data[["latitude", "longitude"]].copy()
    map_data["latitude"] = pd.to_numeric(map_data["latitude"], errors="coerce")
    map_data["longitude"] = pd.to_numeric(map_data["longitude"], errors="coerce")
    map_data = map_data.dropna()

    if not map_data.empty:
        st.map(map_data, latitude="latitude", longitude="longitude", zoom=10)
else:
    st.info("No observations yet. Add your first observation above.")

st.divider()
st.header("📋 Recorded Observations")

if not data.empty:
    st.dataframe(data, use_container_width=True)
else:
    st.info("No observations recorded yet.")

st.divider()
st.header("📊 Biodiversity Dashboard")

if not data.empty:

    habitat_filter = st.selectbox(
        "🌱 Filter by habitat",
        ["All", "Natural area", "Agricultural area", "Urban area"]
    )

    if habitat_filter == "All":
        filtered = data
    else:
        filtered = data[data["habitat"] == habitat_filter]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🔎 Observations", len(filtered))

    total = pd.to_numeric(
        filtered["observation_count"], errors="coerce"
    ).fillna(0).sum()

    c2.metric("🐝 Individuals", int(total))
    c3.metric("🦋 Groups", filtered["pollinator"].nunique())
    c4.metric("🌱 Habitats", filtered["habitat"].nunique())

    st.subheader("🐝 Pollinator groups")
    st.bar_chart(filtered["pollinator"].value_counts())

    st.subheader("🌱 Habitat distribution")
    st.bar_chart(filtered["habitat"].value_counts())

else:
    st.info("Dashboard will appear after the first observation.")
