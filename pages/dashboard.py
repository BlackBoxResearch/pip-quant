import streamlit as st

# Define the Home page
def dashboard_page():
    # Access the user's name from session state
    name = st.session_state.get("name", "User")
    st.title(f"Welcome, {name}!")
    st.markdown("This is your dashboard!")

if __name__ == "__main__":
    dashboard_page()