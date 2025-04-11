import streamlit as st

def login_page():
    st.title("Login")
    
    # Create a container for the login form
    login_container = st.container()
    
    with login_container:
        st.markdown("### Please login to continue")
        
        # Username input
        username = st.text_input("Username")
        
        # Password input
        password = st.text_input("Password", type="password")
        
        # Remember me checkbox
        remember_me = st.checkbox("Remember me")
        
        # Login button
        login_button = st.button("Login")
        
        # Handle login button click (for demonstration only)
        if login_button:
            if username and password:  # Simple check that fields aren't empty
                st.success(f"Welcome, {username}!")
                # In a real app, you would add authentication logic here
                # and redirect to the main application page
                st.session_state.logged_in = True
                st.balloons()
            else:
                st.error("Please enter both username and password")
        
        # Add a divider and forgot password/register links
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("[Forgot Password?](#)")
        with col2:
            st.markdown("[Register](#)")

# You can include this function in your main app or call it directly
if __name__ == "__main__":
    # Set page config
    st.set_page_config(
        page_title="Login",
        page_icon="🔒",
        layout="centered"
    )
    
    # Initialize session state for login status
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    # Show login page if not logged in
    if not st.session_state.logged_in:
        login_page()
    else:
        # If logged in, show a logout button
        st.title("You are logged in!")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.experimental_rerun()