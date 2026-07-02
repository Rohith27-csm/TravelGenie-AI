import os
import streamlit as st
from streamlit_option_menu import option_menu
from tools import generate_trip

st.set_page_config(
    page_title="TravelGenie AI",
    page_icon="🌍",
    layout="wide"
)

# ---------------- Session State ----------------
if "result" not in st.session_state:
    st.session_state.result = None

# ---------------- Sidebar ----------------
with st.sidebar:
    option_menu(
        menu_title="🌍 TravelGenie AI",
        options=["Home", "About"],
        icons=["house", "info-circle"],
        default_index=0,
    )

    st.markdown("---")
    st.write("### ✈️ Features")
    st.write("✅ AI Travel Planner")
    st.write("✅ Personalized Itinerary")
    st.write("✅ Budget Planning")
    st.write("✅ Hotel Suggestions")
    st.write("✅ Destination Images")
    st.write("✅ Google Maps")
    st.write("✅ Download Travel Plan")

# ---------------- Header ----------------
st.title("🌍 TravelGenie AI")
st.subheader("Your AI-Powered Smart Travel Planner ✈️")

st.markdown("---")

# ---------------- Input Section ----------------
col1, col2 = st.columns(2)

with col1:
    destination = st.text_input("📍 Destination")

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=30,
        value=3
    )

    budget = st.text_input("💰 Budget")

with col2:
    interests = st.text_area(
        "🎯 Interests",
        placeholder="Example: Beaches, Food, Adventure, Shopping"
    )

# ---------------- Destination Image ----------------
if destination:
    image_path = f"assets/{destination.lower()}.jpg"

    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    elif os.path.exists("assets/default.jpg"):
        st.image("assets/default.jpg", use_container_width=True)

st.markdown("---")

# ---------------- Generate Button ----------------
if st.button("🚀 Generate Travel Plan", use_container_width=True):

    if destination and budget and interests:

        with st.spinner("🤖 AI is planning your trip..."):

            st.session_state.result = generate_trip(
                destination,
                days,
                budget,
                interests
            )

        st.success("✅ Travel Plan Generated!")

    else:
        st.warning("⚠️ Please fill all the fields.")

# ---------------- Show Result ----------------
if st.session_state.result:

    st.markdown(st.session_state.result)

    st.download_button(
        label="📄 Download Travel Plan",
        data=st.session_state.result,
        file_name="Travel_Plan.txt",
        mime="text/plain"
    )

    if destination:
        st.link_button(
            "📍 Open in Google Maps",
            f"https://www.google.com/maps/search/{destination}"
        )