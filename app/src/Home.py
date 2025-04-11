# naman
##################################################
# Main entry point for the StudyBuddy application.
# Handles routing based on login status.
##################################################

import streamlit as st

from modules.nav import setup_page # Import setup_page for the me/sidebar

# Set page config first
st.set_page_config(
    page_title="StudyBuddy Dashboard",
    page_icon="📚",
    layout="wide"
)

# Initialize session state if keys don't exist
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = {}

# --- Page Logic ---
if not st.session_state.logged_in:
    # If not logged in, show login page
    st.switch_page("pages/login.py")
    st.stop()
else:
    # If logged in, setup sidebar and check login status again
    setup_page("Dashboard") 
    
    st.header("Welcome to your StudyBuddy Dashboard!")
    
    # Layout columns
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.subheader("Your Study Groups")
        # Display study groups (example data)
        groups = [
            {"name": "CS3200 Study Group", "next_session": "Tomorrow at 3 PM"},
            {"name": "FINA2201 Study Group", "next_session": "Friday at 2 PM"}
        ]
        
        if groups:
            for group in groups:
                with st.expander(f"**{group['name']}**"):
                    st.write(f"Next Session: {group.get('next_session', 'Not scheduled')}")
                    st.button("Join Session", key=f"join_{group['name']}") # Button doesn't do anything yet
        else:
            st.write("You haven't joined any study groups yet.")
        
        st.subheader("Study Resources")
        # Display resources (example data)
        resources = [
            {"name": "Programming Basics PDF", "type": "Document"},
            {"name": "Math Formula Sheet", "type": "Document"}
        ]
        
        if resources:
            for resource in resources:
                with st.expander(f"**{resource['name']}**"):
                    st.write(f"Type: {resource.get('type', 'N/A')}")
                    st.button("Access", key=f"access_{resource['name']}") # Button doesn't do anything yet
        else:
            st.write("No study resources available yet.")
    
    with right_col:
        st.subheader("Profile Summary")
        # Show basic user info from session state
        user_info = st.session_state.user 
        st.write(f"Name: {user_info.get('name', 'N/A')}")
        st.write(f"University: {user_info.get('university', 'N/A')}")
        st.write(f"Major: {user_info.get('major', 'N/A')}")
        
        if st.button("Edit Profile", use_container_width=True):
            st.switch_page("pages/profile.py")
        
        st.subheader("Study Matches")
        # Display matches (example data)
        matches = [
            {"name": "Alex CHen", "compatibility": "95%"},
            {"name": "Emily Rodriguez", "compatibility": "88%"}
        ]
        
        if matches:
            for match in matches:
                st.write(f"**{match['name']}** - {match.get('compatibility', 'N/A')} Match")
                st.button("Connect", key=f"connect_{match['name']}") # Button doesn't do anything yet
        else:
            st.write("No recent matches found.")
=======
from modules.nav import SideBarLinks
from pathlib import Path
import pickle

# Import the login module functions
from pages.login import login_form, register_form

# streamlit supports regular and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('CS 3200 Sample Semester Project App')
st.write('\n\n')

# Create tabs for Login, Register, and Demo
login_tab, register_tab, demo_tab = st.tabs(["Login", "Register", "Demo Users"])

with login_tab:
    st.subheader("Login with your account")
    login_form()

with register_tab:
    register_form()

with demo_tab:
    st.subheader("Demo Login")
    st.write('### As which demo user would you like to log in?')

    # For each of the user personas for which we are implementing
    # functionality, we put a button on the screen that the user 
    # can click to MIMIC logging in as that mock user. 

    if st.button("Act as John, a Political Strategy Advisor", 
                type = 'primary', 
                use_container_width=True):
        # when user clicks the button, they are now considered authenticated
        st.session_state['authenticated'] = True
        # we set the role of the current user
        st.session_state['role'] = 'pol_strat_advisor'
        # we add the first name of the user (so it can be displayed on 
        # subsequent pages). 
        st.session_state['first_name'] = 'John'
        # finally, we ask streamlit to switch to another page, in this case, the 
        # landing page for this particular user type
        logger.info("Logging in as Political Strategy Advisor Persona")
        st.switch_page('pages/00_Pol_Strat_Home.py')

    if st.button('Act as Mohammad, an USAID worker', 
                type = 'primary', 
                use_container_width=True):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'usaid_worker'
        st.session_state['first_name'] = 'Mohammad'
        st.switch_page('pages/10_USAID_Worker_Home.py')

    if st.button('Act as System Administrator', 
                type = 'primary', 
                use_container_width=True):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'administrator'
        st.session_state['first_name'] = 'SysAdmin'
        st.switch_page('pages/20_Admin_Home.py')

# Display any registered users for debugging purposes (can be removed in production)
if st.sidebar.checkbox("Show Registered Users", False):
    credentials_file = Path("credentials.pkl")
    if credentials_file.exists():
        with open(credentials_file, "rb") as f:
            password_dict = pickle.load(f)
        st.sidebar.write("Registered Usernames:")
        for username, user_data in password_dict.items():
            st.sidebar.write(f"- {username} ({user_data['role']})")
    else:
        st.sidebar.write("No registered users yet.")

