import streamlit as st
import hmac
import hashlib


USER_CREDENTIALS = {
    "demo": "password123",
    "admin": "admin123"
}

def check_password(username, password):
    """Check if username/password is valid"""
    if username in USER_CREDENTIALS:
        
        return USER_CREDENTIALS[username] == password
    return False

def login_form():
    """Display the login form and handle authentication"""
    st.subheader("Login")
    
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if check_password(username, password):
            st.session_state['authenticated'] = True
            st.session_state['username'] = username
            st.success(f"Welcome {username}!")
            st.rerun()  
        else:
            st.error("Invalid username or password")
    
    st.markdown("---")
    st.markdown("Don't have an account? Use username: 'demo' and password: 'password123' to try out the app!")

def logout():
    """Log out the user"""
    if st.sidebar.button("Logout"):
        st.session_state['authenticated'] = False
        st.session_state['username'] = None
        st.rerun()  

def require_auth():
    """Check if user is authenticated, if not show login form"""
    if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
        login_form()
        st.stop()  
    else:
        
        st.sidebar.write(f"Logged in as: {st.session_state['username']}")
        logout()