import streamlit as st

# Basic page configuration
st.set_page_config(
    page_title="PAU SIBAS Portal", 
    page_icon="🏫", 
    layout="centered"
)

st.title("🏫 SIBAS Attendance Portal")
st.write("Welcome to the Pan-Atlantic University Smart Attendance System[cite: 3, 12].")

# Session state initialization for tracking login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = None

if not st.session_state.logged_in:
    st.info("👋 Please proceed to the **Login page** in the sidebar to authenticate and access your dashboard[cite: 31].")
else:
    st.success(f"🎉 You are logged in as an **{st.session_state.user_role}**!")
    
    # Simple logout button [cite: 31]
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.user_role = None
        st.rerun()