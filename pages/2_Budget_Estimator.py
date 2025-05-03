import streamlit as st
from services.service import execute_task
from services.task import budget_task
import datetime
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Budget Estimator",
    page_icon="💰",
    layout="wide"
)


st.markdown("""
<style>
    .page-title {
        font-size: 2.5rem !important;
        color: #1E88E5;
    }
    .section-header {
        font-size: 1.8rem;
        color: #424242;
        margin-top: 2rem;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-size: 1.2rem;
        width: 100%;
    }
    .budget-card {
        background-color: #F1F8E9;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='page-title'>💰 Budget Estimator</h1>", unsafe_allow_html=True)
st.markdown("Plan your travel budget with our AI-powered estimator")


col1, col2 = st.columns([2, 1])

with col1:
    
    origin = st.text_input("Where are you traveling from?", placeholder="e.g., New York")
    destination = st.text_input("Where do you want to go?", placeholder="e.g., Paris")
    
    
    today = datetime.date.today()
    start_date = st.date_input("Start date", today + datetime.timedelta(days=30))
    end_date = st.date_input("End date", today + datetime.timedelta(days=35))
    
    
    if start_date and end_date:
        days = (end_date - start_date).days
        if days < 1:
            st.error("End date must be after start date")
            days = 1
    else:
        days = 5
        
    st.info(f"Trip duration: {days} days")
    
    
    travelers = st.number_input("Number of travelers", min_value=1, max_value=20, value=2)

with col2:
    
    st.markdown("### Budget Preferences")
    
    accommodation_level = st.select_slider(
        "Accommodation level",
        options=["Budget", "Economy", "Standard", "Premium", "Luxury"],
        value="Standard"
    )
    
    food_budget = st.select_slider(
        "Food budget",
        options=["Minimal", "Economy", "Standard", "Gourmet", "Fine Dining"],
        value="Standard"
    )
    
    activities_budget = st.select_slider(
        "Activities budget",
        options=["Minimal", "Basic", "Standard", "Premium", "Luxury"],
        value="Standard"
    )
    
    st.markdown("### Transportation")
    transportation_options = st.multiselect(
        "Transportation options",
        ["Public transit", "Rental car", "Taxis/Rideshares", "Domestic flights", "Walking/Biking"],
        default=["Public transit"]
    )


prompt = f"""
Estimate a detailed budget for a {days}-day trip from {origin} to {destination} for {travelers} traveler(s).
Trip dates: {start_date} to {end_date}
Accommodation level: {accommodation_level}
Food budget: {food_budget}
Activities budget: {activities_budget}
Transportation options: {', '.join(transportation_options)}

Please provide:
- Total estimated budget with breakdown
- Accommodation costs (average per night and total)
- Food costs (average per day and total)
- Transportation costs (breakdown by type)
- Activities and sightseeing costs
- Other expenses (souvenirs, etc.)
- Money-saving tips specific to this destination
- Cost comparison to similar destinations

Format the budget in a way that's easy to read and categorized.
"""

submit_budget_btn = st.button("Generate Budget Estimate")


if submit_budget_btn:
    if not destination:
        st.error("Please enter a destination")
    else:
        with st.spinner(f"Calculating budget estimates for {destination}... This may take a minute"):
            budget_result = execute_task(budget_task, prompt)
            
            
            st.session_state['budget_result'] = budget_result
            
            
            st.markdown("### 💰 Your Budget Estimate")
            
            
            result_col1, result_col2 = st.columns([3, 2])
            
            with result_col1:
                st.markdown(budget_result)
                
                
                st.download_button(
                    label="Download Budget Estimate",
                    data=f"# Trip Budget: {origin} to {destination}\n\n{budget_result}",
                    file_name=f"budget_{destination.replace(' ', '_')}.md",
                    mime="text/markdown"
                )
            
            with result_col2:
                st.markdown("### 📊 Budget Visualization")
                st.info("Sample visualization based on similar trips")
                
                
                budget_categories = {
                    'Accommodation': 35,
                    'Food': 25,
                    'Transportation': 20,
                    'Activities': 15,
                    'Misc': 5
                }
                
                
                fig = px.pie(
                    values=list(budget_categories.values()),
                    names=list(budget_categories.keys()),
                    title="Estimated Budget Breakdown",
                    color_discrete_sequence=px.colors.sequential.Blues_r
                )
                st.plotly_chart(fig)
                
                
                st.markdown("""
                <div class='budget-card'>
                <h4>💡 Budget Tips</h4>
                <ul>
                <li>Consider staying in accommodations with kitchen access to save on meals</li>
                <li>Research city passes for discounted attractions</li>
                <li>Use public transportation instead of taxis when possible</li>
                <li>Travel during shoulder season for better rates</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)


if 'budget_result' in st.session_state and not submit_budget_btn:
    st.markdown("### Your Previous Budget Estimate")
    st.markdown(st.session_state['budget_result'])