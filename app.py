import streamlit as st

# ---------------- AI AGENT BRAIN ---------------- #
def greenhouse_agent(temp, humidity, soil, light):

    actions = {
        "Fan": "OFF",
        "Water Pump": "OFF",
        "Grow Light": "OFF"
    }

    if temp > 30 or humidity > 80:
        actions["Fan"] = "ON"

    if soil < 40:
        actions["Water Pump"] = "ON"

    if light < 300:
        actions["Grow Light"] = "ON"

    return actions

# ---------------- STREAMLIT UI ---------------- #
st.set_page_config(page_title="Smart Greenhouse AI", page_icon="🌿", layout="centered")

st.title("🌱 Smart Greenhouse AI Agent Controller")
st.caption("An intelligent controller for automated greenhouse management")

st.divider()

# Sensor Inputs
temp = st.slider("🌡 Temperature (°C)", 0, 50, 25)
humidity = st.slider("💧 Humidity (%)", 0, 100, 60)
soil = st.slider("🌿 Soil Moisture (%)", 0, 100, 50)
light = st.slider("☀ Light Intensity (lux)", 0, 1000, 400)

st.divider()

if st.button("🤖 Run AI Agent", use_container_width=True):

    actions = greenhouse_agent(temp, humidity, soil, light)

    st.subheader("🔧 AI Agent Decisions")

    col1, col2, col3 = st.columns(3)

    col1.metric("🌀 Fan", actions["Fan"])
    col2.metric("🚿 Water Pump", actions["Water Pump"])
    col3.metric("💡 Grow Light", actions["Grow Light"])

    st.success("AI agent successfully evaluated greenhouse conditions 🌿")

st.divider()

st.markdown("""
### 🧠 How the AI works
- Controls fan based on temperature & humidity  
- Controls pump based on soil moisture  
- Controls light based on illumination  

This is a **real AI agent logic system**, not just UI automation.
""")

st.markdown("---")

