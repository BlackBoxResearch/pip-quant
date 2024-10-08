import streamlit as st

# Function to check user credentials
def check_login(username, password):
    # Retrieve credentials from st.secrets
    users = st.secrets["users"]

    # Check if the username exists and password matches
    for user, details in users.items():
        if details["username"] == username and details["password"] == password:
            return details["name"]
    return None

# Define the Login page
def login_page():
    st.title("Login")

    # Create login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # If login button is clicked
    if st.button("Login"):
        # Validate credentials and retrieve name
        name = check_login(username, password)
        
        # Check if credentials are valid
        if name:
            st.session_state["logged_in"] = True
            st.session_state["name"] = name
            st.success(f"Logged in successfully as {name}!")
            
            # Redirect to the homepage by setting session state
            st.session_state["current_page"] = "Homepage"
            st.rerun()
        else:
            # Show error message when login fails
            st.error("Incorrect username or password. Please try again.")

if __name__ == "__main__":
    login_page()