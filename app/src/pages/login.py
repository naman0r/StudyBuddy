
# naman
import streamlit as st
from pathlib import Path
from modules.nav import apply_basic_theme # Use simplified theme

def login_form():
    """Displays the login form and handles hardcoded demo login."""
    st.title("StudyBuddy Login")
    
    with st.form("login_form"):
        st.write("Log in to your account (Use demo credentials)")
        email = st.text_input("Email", placeholder="demo@example.com")
        password = st.text_input("Password", type="password", placeholder="password")
        
        submitted = st.form_submit_button("Log In")
        
        if submitted:
            if email and password:
                # Hardcoded demo authentication ONLY
                if email == "demo@example.com" and password == "password":
                    st.session_state.logged_in = True
                    # Save minimal user info
                    st.session_state.user = {"email": email, "name": "Demo User"}
                    st.switch_page("Home.py") 
                else:
                    st.error("Invalid email or password. Please use demo credentials.")
            else:
                st.error("Please enter email and password.")
    
    # Removed Create Account button

# Removed register_form function entirely

# Removed reset_password_form function entirely

# --- Main Script Execution ---
# Set page config (must be first Streamlit call)
st.set_page_config(
    page_title="StudyBuddy Login",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply basic theme (hide footer/menu)
apply_basic_theme()

# Initialize session state if needed
if "page" not in st.session_state: # Although 'page' is no longer used for routing here, keep for potential future use?
    st.session_state.page = "login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Simple Routing/Display Logic
if st.session_state.logged_in:
    # If already logged in, go to dashboard
    st.switch_page("Home.py")
    st.stop()
else:
    # Only show login form if not logged in
    login_form()
=======
import streamlit as st
import base64

def add_logo():
    logo_html = """
    <style>
    .logo-container {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    .logo {
        font-family: 'Arial', sans-serif;
        font-size: 28px;
        font-weight: bold;
        color: #3366ff;
        margin-right: 30px;
    }
    .nav-links {
        display: flex;
        gap: 20px;
        color: #505050;
        font-family: 'Arial', sans-serif;
    }
    .nav-item {
        font-size: 16px;
        color: #505050;
        text-decoration: none;
    }
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid #eaeaea;
        margin-bottom: 30px;
        width: 100%;
    }
    .icons {
        display: flex;
        gap: 15px;
    }
    .form-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        background-color: white;
    }
    .header-text {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #333;
        text-align: center;
    }
    .blue-button {
        background-color: #3366ff;
        color: white;
        padding: 10px 15px;
        border-radius: 5px;
        text-align: center;
        cursor: pointer;
        font-weight: bold;
        border: none;
        width: 100%;
        margin-top: 10px;
    }
    .links {
        display: flex;
        justify-content: space-between;
        margin-top: 15px;
        font-size: 14px;
    }
    .link {
        color: #3366ff;
        text-decoration: none;
    }
    </style>
    <div class="header">
        <div class="logo-container">
            <div class="logo">StudyBuddy</div>
            <div class="nav-links">
                <a href="#" class="nav-item">Dashboard</a>
                <a href="#" class="nav-item">Find Partners</a>
                <a href="#" class="nav-item">Study Groups</a>
                <a href="#" class="nav-item">Resources</a>
            </div>
        </div>
        <div class="icons">
            <span>🔔</span>
            <span>✉️</span>
        </div>
    </div>
    """
    st.markdown(logo_html, unsafe_allow_html=True)

def login_page():
   
    add_logo()
    
    
    form_html = """
    <div class="form-container">
        <div class="header-text">Log in to StudyBuddy</div>
    """
    st.markdown(form_html, unsafe_allow_html=True)
    
   
    with st.container():
        
        email = st.text_input("Email or Username")
        
       
        password = st.text_input("Password", type="password")
        
       
        col1, col2 = st.columns([1, 1])
        with col1:
            remember_me = st.checkbox("Remember me")
            
     
        login_btn = st.button("Log In", type="primary", use_container_width=True)
        
        
        if login_btn:
            if email and password: 
                st.success(f"Welcome to StudyBuddy!")
               
                st.session_state.logged_in = True
                st.balloons()
            else:
                st.error("Please enter both email and password")
        
     
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div style='margin-top:-15px'><a href='#' style='color:#3366ff;font-size:14px;text-decoration:none;'>Forgot Password?</a></div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div style='margin-top:-15px;text-align:right'><a href='#' style='color:#3366ff;font-size:14px;text-decoration:none;'>Sign Up</a></div>", unsafe_allow_html=True)


if __name__ == "__main__":
  
    st.set_page_config(
        page_title="StudyBuddy Login",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
   
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {
        background-color: #f8f9fa;
    }
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
  
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
   
    if not st.session_state.logged_in:
        login_page()
    else:
        
        add_logo()
        st.write("## Welcome to your StudyBuddy Dashboard!")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.experimental_rerun()

