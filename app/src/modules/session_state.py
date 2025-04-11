import streamlit as st

def init_session_state():
    """Initialize session state variables if they don't exist"""
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
        
    if 'first_name' not in st.session_state:
        st.session_state.first_name = None
        
    if 'last_name' not in st.session_state:
        st.session_state.last_name = None
        
    if 'major' not in st.session_state:
        st.session_state.major = None 