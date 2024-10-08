import streamlit as st

def logout_page():
    st.title("Logout")
    # Check if the user is logged out in session state
    if 'logged_out' not in st.session_state:
        st.session_state.logged_out = False

    # If user is not logged out, show confirmation message
    if not st.session_state.logged_out:
        st.write("Are you sure you want to log out?")
        if st.button("Confirm Logout"):
            st.session_state["logged_in"] = False
            st.session_state["logged_out"] = True
            st.success("Logged out successfully!")
            st.rerun()

if __name__ == "__main__":
    logout_page()
