import streamlit as st
import pandas as pd
from streamlit_extras.stylable_container import stylable_container

# Set page configuration to wide mode
st.set_page_config(layout="wide")

st.get_option("theme.base")
st.get_option("client.toolbarMode")

border_colour = 'rgba(75, 75, 75, 1)'
background_color = '#262730'
chart_pve_fill_color = '#88a4b8'
chart_nve_fill_color = '#c99797'

def homepage_page():
    # Access the user's name from session state
    name = st.session_state.get("name", "User")
    st.title(f"Welcome, {name}!")
    st.markdown("This is an overview of all connected accounts aggregated into one profile.")

    with st.container(border=False):
    # Creating rows with specified columns
        row1 = st.columns(4)
        row2 = st.columns(1)
        row3 = st.columns(2)

        with row1[0]:
            with stylable_container(
                    key="tile",
                    css_styles=f'''
                    {{
                        background-color: {background_color};
                        border: 1px solid {border_colour};
                        border-radius: 0.5rem;
                        padding: 1em;
                    }}
                    '''
            ):
                tile1 = st.container()
                tile1.metric(label="Total Profit", value="$12,201.00", delta="+$1,451.00")

        with row1[1]:
            with stylable_container(
                    key="tile",
                    css_styles=f'''
                                    {{
                                        background-color: {background_color};
                                        border: 1px solid {border_colour};
                                        border-radius: 0.5rem;
                                        padding: 1em;
                                    }}
                                    '''
            ):
                tile2 = st.container()
                tile2.metric(label="Total Gain", value="22.01%", delta="+14.51%")

        with row1[2]:
            with stylable_container(
                    key="tile",
                    css_styles=f'''
                                    {{
                                        background-color: {background_color};
                                        border: 1px solid {border_colour};
                                        border-radius: 0.5rem;
                                        padding: 1em;
                                    }}
                                    '''
            ):
                tile3 = st.container()
                tile3.metric(label="Profit Factor", value="1.21", delta="+0.05")

        with row1[3]:
            with stylable_container(
                    key="tile",
                    css_styles=f'''
                                    {{
                                        background-color: {background_color};
                                        border: 1px solid {border_colour};
                                        border-radius: 0.5rem;
                                        padding: 1em;
                                    }}
                                    '''
            ):
                tile4 = st.container()
                tile4.metric(label="PipQuant Score", value="69", delta="+2")

        # Adding individual content to the single column in row 2
        with row2[0]:
            with stylable_container(
                    key="tile",
                    css_styles=f'''
                                    {{
                                        background-color: {background_color};
                                        border: 1px solid {border_colour};
                                        border-radius: 0.5rem;
                                        padding: 1em;
                                    }}
                                    '''
            ):
                tile5 = st.container()
                tile5.subheader("Aggregated Profit")

            with row3[1]:
                with stylable_container(
                        key="tile",
                        css_styles=f'''
                                        {{
                                            background-color: {background_color};
                                            border: 1px solid {border_colour};
                                            border-radius: 0.5rem;
                                            padding: 1em;
                                        }}
                                        '''
                ):
                    tile7 = st.container()
                    tile7.subheader("Statistics")
                    col1, col2, col3, col4 = tile7.columns(4)
                    with col1:
                        st.markdown('''
                                        **Balance**:
                                        \n**Equity**:
                                        \n**Profit Factor**:
                                        
                        ''')

                    with col2:
                        st.markdown(f'''
                                        $25,120.22
                                        \n$27,125.52
                                        \n1.21
                        ''')

                    with col3:
                        st.markdown('''
                                        **Total Profit**:
                                        \n**Total Gain**:
                                        \n**Max Drawdown**:

                        ''')

                    with col4:
                        st.markdown(f'''
                                        $12,201.00
                                        \n22.01%
                                        \n10.21%
                        ''')



        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f'''
                            **Products**
                            \nTrade Copier
                            \nAI Quant
                            \nEA Builder
                            \nEconomic Calendar


                        ''')


        with col2:
            st.markdown(f'''
                            **For Businesses**
                            \nAffiliates
                            \nPartnerships
                        ''')

        with col3:
            st.markdown(f'''
                            **Socials**
                            \nInstagram
                            \nX
                        ''')

def dashboard_page():
    st.title("Dashboard")

def leaderboard_page():
    st.title(f"Leaderboard")

def trade_copier_page():
    st.title(f"Trade Copier")

def ai_quant_page():
    st.title(f"AI Quant")

def ea_builder_page():
    st.title(f"EA Builder")

def eco_calendar_page():
    st.title(f"Economic Calendar")

def support_page():
    st.title(f"Support")

def settings_page():
    st.title(f"Settings")

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

# Define pages with icons
homepage = st.Page(page=homepage_page, title="Homepage", icon=":material/home:")
dashboard = st.Page(page=dashboard_page, title="Dashboard", icon=":material/insights:")
leaderboard = st.Page(page=leaderboard_page, title="Leaderboard", icon=":material/trophy:")

trade_copier = st.Page(page=trade_copier_page, title="Trade Copier", icon=":material/sync_alt:")
ai_quant = st.Page(page=ai_quant_page, title="AI Quant", icon=":material/smart_toy:")

ea_builder = st.Page(page=ea_builder_page, title="EA Builder", icon=":material/terminal:")
eco_calendar = st.Page(page=eco_calendar_page, title="Economic Calendar", icon=":material/view_timeline:")

support = st.Page(page=support_page, title="Support", icon=":material/help:")
settings = st.Page(page=settings_page, title="Settings", icon=":material/settings:")
logout = st.Page(page=logout_page, title="Logout", icon=":material/logout:")

# Group pages into sections
pages = {
    "Accounts": [homepage, dashboard, leaderboard],
    "Tools": [trade_copier, ai_quant, ea_builder, eco_calendar],
    "Help": [support, settings],
    "Logout": [logout]  # Logout page added here
}

# Create the navigation menu
def create_navigation():
    selected_page = st.navigation(pages, position="sidebar")
    # Run the selected page
    selected_page.run()

# Function to check user credentials
def check_login(username, password):
    # Retrieve credentials from st.secrets
    users = st.secrets["users"]

    # Check if the username exists and password matches
    for user, details in users.items():
        if details["username"] == username and details["password"] == password:
            return details["name"]
    return None

# Login page function
def login():
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
            st.session_state["current_page"] = "Home"
            st.rerun()
        else:
            # Show error message when login fails
            st.error("Incorrect username or password. Please try again.")

# Main function
def main():
    # Check if user is already logged in
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # If not logged in, show login page
    if not st.session_state["logged_in"]:
        login()
    else:
        # If logged in, create the navigation and show pages
        create_navigation()

# Run the app
if __name__ == "__main__":
    main()
