import streamlit as st

def initialize_session_state():
    """Initialize key session state variables if they don't exist"""
    if 'destination' not in st.session_state:
        st.session_state['destination'] = ""
    if 'origin' not in st.session_state:
        st.session_state['origin'] = ""
    if 'days' not in st.session_state:
        st.session_state['days'] = 5
    if 'start_date' not in st.session_state:
        st.session_state['start_date'] = None
    if 'end_date' not in st.session_state:
        st.session_state['end_date'] = None
    if 'travelers' not in st.session_state:
        st.session_state['travelers'] = 2

def save_trip_details(origin, destination, start_date, end_date, travelers=None):
    """Save common trip details to session state"""
    st.session_state['origin'] = origin
    st.session_state['destination'] = destination
    st.session_state['start_date'] = start_date
    st.session_state['end_date'] = end_date
    if travelers:
        st.session_state['travelers'] = travelers
    
    
    if start_date and end_date:
        st.session_state['days'] = (end_date - start_date).days