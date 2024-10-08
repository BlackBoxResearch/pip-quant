import streamlit as st
import random
import pandas as pd
from pages import accounts, ai_quant, dashboard, ea_builder, eco_calendar, home, leaderboard, login, logout, settings, support, trade_copier

# Set page configuration to wide mode
st.set_page_config(layout="wide")

# Define pages with icons
home = st.Page(page=home.home_page, title="Home", icon=":material/home:")
login = st.Page(page=login.login_page, title="Login", icon=":material/login:")
dashboard = st.Page(page=dashboard.dashboard_page, title="Dashboard", icon=":material/insights:")
accounts = st.Page(page=accounts.accounts_page, title="Accounts", icon=":material/account_tree:")
leaderboard = st.Page(page=leaderboard.leaderboard_page, title="Leaderboard", icon=":material/trophy:")
trade_copier = st.Page(page=trade_copier.trade_copier_page, title="Trade Copier", icon=":material/sync_alt:")
ai_quant = st.Page(page=ai_quant.ai_quant_page, title="AI Quant", icon=":material/smart_toy:")
ea_builder = st.Page(page=ea_builder.ea_builder_page, title="EA Builder", icon=":material/terminal:")
eco_calendar = st.Page(page=eco_calendar.eco_calendar_page, title="Economic Calendar", icon=":material/view_timeline:")
support = st.Page(page=support.support_page, title="Support", icon=":material/help:")
settings = st.Page(page=settings.settings_page, title="Settings", icon=":material/settings:")
logout = st.Page(page=logout.logout_page, title="Logout", icon=":material/logout:")

# Group pages into sections for logged-out users
logged_out_pages = {
    "Home": [home, login]
}

# Group pages into sections for logged-in users
logged_in_pages = {
    "Home": [dashboard, accounts, leaderboard],
    "Tools": [trade_copier, ai_quant, ea_builder, eco_calendar],
    "Help": [support, settings],
    "Logout": [logout]  # Logout page added here
}

# Create the navigation menu with Home as the default page
def create_navigation(pages):
    selected_page = st.navigation(pages, position="sidebar")
    # Run the selected page
    selected_page.run()

# Main function
def main():
    # Check if user is already logged in
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.session_state["logged_in"] = False
        create_navigation(logged_out_pages)
    else:
        create_navigation(logged_in_pages)

# Run the app
if __name__ == "__main__":
    main()
