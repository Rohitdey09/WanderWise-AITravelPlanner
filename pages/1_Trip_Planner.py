import streamlit as st
from services.service import execute_task
from services.task import trip_task
import datetime
from utils.map_utils import display_trip_map
from utils.auth import require_auth
from utils.weather_utils import display_weather_widget


st.set_page_config(
    page_title="Trip Planner",
    page_icon="📅",
    layout="wide"
)


require_auth()


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
    .info-box {
        background-color: #E3F2FD;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='page-title'>📅 AI Trip Planner</h1>", unsafe_allow_html=True)
st.markdown("Create a personalized day-by-day itinerary for your upcoming adventure!")


input_tab, examples_tab = st.tabs(["Create Your Itinerary", "Example Itineraries"])

with input_tab:
    col1, col2 = st.columns(2)
    
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

    
    with col2:
        travel_style = st.selectbox(
            "What's your travel style?",
            ["Balanced", "Adventure", "Cultural", "Relaxation", "Food-focused", "Budget-friendly", "Luxury"]
        )
        
        interests = st.multiselect(
            "Select your interests",
            ["History", "Art", "Nature", "Shopping", "Nightlife", "Local experiences", "Architecture", 
             "Beaches", "Museums", "Photography", "Sports", "Wildlife"]
        )
        
        pace = st.slider("Travel pace", 1, 5, 3, 
                         help="1 = Very relaxed, 5 = Very active")
        
        special_requirements = st.text_area("Any special requirements?", 
                                          placeholder="e.g., wheelchair accessible, traveling with kids, etc.")


    
    prompt = f"""
    Plan a {days}-day trip from {origin} to {destination} from {start_date} to {end_date}.
    Travel style: {travel_style}
    Interests: {', '.join(interests) if interests else 'Various'}
    Pace: {pace}/5
    Special requirements: {special_requirements}
    
    Please provide a detailed day-by-day itinerary with:
    - Recommended activities for each day
    - Best times to visit attractions
    - Transportation between locations
    - Suggested break times
    - Local tips and cultural insights
    """
    
    submit_btn = st.button("Generate My Itinerary")

    
    if destination:
        st.markdown("<div class='widget-container'>", unsafe_allow_html=True)
        map_col, weather_col = st.columns(2)

        with map_col:
            st.markdown("<div class='map-card'>", unsafe_allow_html=True)
            if origin and destination:
                display_trip_map(origin, destination)
            else:
                st.info("Enter both origin and destination to see your route map")
            st.markdown("</div>", unsafe_allow_html=True)

        with weather_col:
            st.markdown("<div class='weather-card'>", unsafe_allow_html=True)
            st.markdown("### Weather at Your Destination")
            display_weather_widget(destination, min(7, days))
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)

    
    if submit_btn:
        if not destination:
            st.error("Please enter a destination")
        else:
            with st.spinner(f"Planning your dream trip to {destination}... This may take a minute"):
                itinerary = execute_task(trip_task, prompt)
                
                # Store in session state for persistence
                st.session_state['itinerary_result'] = itinerary
                
                
                st.markdown("### ✨ Your Personalized Itinerary")
                st.markdown(itinerary)
                
                
                st.download_button(
                    label="Download Itinerary",
                    data=f"# Trip Itinerary: {origin} to {destination}\n\n{itinerary}",
                    file_name=f"itinerary_{destination.replace(' ', '_')}.md",
                    mime="text/markdown"
                )

# Display previous result if available
if 'itinerary_result' in st.session_state and not submit_btn:
    st.markdown("### Your Previous Itinerary")
    st.markdown(st.session_state['itinerary_result'])
    
    # Download option
    st.download_button(
        label="Download Itinerary",
        data=f"# Trip Itinerary\n\n{st.session_state['itinerary_result']}",
        file_name="itinerary.md",
        mime="text/markdown"
    )

# Examples tab
with examples_tab:
    st.markdown("### Sample Itineraries")
    
    example_tab1, example_tab2, example_tab3 = st.tabs(["Tokyo Adventure", "Italy Road Trip", "Bali Relaxation"])
    
    with example_tab1:
        st.markdown("""
        ### 5-Day Tokyo Adventure
        
        **Day 1: Arrival & Shibuya**
        - Morning: Arrive at Narita Airport, take Narita Express to hotel
        - Afternoon: Explore Shibuya Crossing and surrounding shops
        - Evening: Dinner at Ichiran Ramen, visit Shibuya Sky for night views
        
        **Day 2: Traditional Tokyo**
        - Morning: Visit Meiji Shrine and Yoyogi Park
        - Afternoon: Explore Harajuku and Takeshita Street
        - Evening: Dinner in Shinjuku, followed by drinks in Golden Gai
        
        *... and so on ...*
        """)
    
    with example_tab2:
        st.markdown("Content for Italy Road Trip example")
    
    with example_tab3:
        st.markdown("Content for Bali Relaxation example")