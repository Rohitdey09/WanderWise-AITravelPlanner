import streamlit as st
import base64
from PIL import Image
import os
from utils.auth import require_auth
from utils.session_state import initialize_session_state

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)


initialize_session_state()


require_auth()


st.markdown("""
<style>
    .main-title {
        font-size: 3.5rem !important;
        color: #1E88E5;
        text-align: center;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #424242;
        text-align: center;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-size: 1.2rem;
    }
    .feature-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)


st.markdown("<h1 class='main-title'>🌍 AI Travel Planner</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Your intelligent companion for seamless travel experiences</p>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    
    st.image("https://images.unsplash.com/photo-1488085061387-422e29b40080?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2942&q=80", 
             use_column_width=True)
    
    st.markdown("""
    ### Welcome to your AI-powered travel companion!
    
    Planning a trip can be overwhelming, but not anymore. Our AI agents help you create 
    personalized travel experiences with detailed itineraries, budget estimates, 
    local cuisine recommendations, and essential safety information.
    """)
    
    st.markdown("### 🚀 Get started by navigating to one of our planning tools in the sidebar!")


st.markdown("## ✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📅 Interactive Trip Planner</h3>
        <p>Create personalized day-by-day itineraries based on your interests, origin, and destination.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>💰 Smart Budget Estimator</h3>
        <p>Get detailed budget breakdowns for accommodations, transportation, food, activities, and more.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🍽️ Local Cuisine Guide</h3>
        <p>Discover must-try local dishes and recommended restaurants at your destination.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🚨 Travel Safety Assistant</h3>
        <p>Access important emergency contacts and safety tips specific to your destination.</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("## 🔍 How It Works")
st.markdown("""
Our AI Travel Planner uses advanced AI agents powered by Groq's LLama3 model to:

1. **Understand** your travel preferences and requirements
2. **Research** the best options for your trip
3. **Create** personalized recommendations and plans
4. **Deliver** comprehensive travel guidance in seconds
""")

st.markdown("---")
st.markdown("### Start planning your dream trip now by selecting a tool from the sidebar! ➡️")