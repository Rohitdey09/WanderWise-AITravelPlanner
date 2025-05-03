import streamlit as st
from services.service import execute_task
from services.task import emergency_task

st.set_page_config(
    page_title="Emergency Assistant",
    page_icon="🚨",
    layout="wide"
)


st.markdown("""
<style>
    .page-title {
        font-size: 2.5rem !important;
        color: #1E88E5;
    }
    .emergency-card {
        background-color: #FFEBEE;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid #E53935;
    }
    .info-card {
        background-color: #E3F2FD;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    .stButton>button {
        background-color: #E53935;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-size: 1.2rem;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='page-title'>🚨 Travel Safety Assistant</h1>", unsafe_allow_html=True)
st.markdown("Get essential safety information and emergency contacts for your destination")


default_destination = st.session_state.get('destination', '')


destination = st.text_input("Where are you traveling to?", value=default_destination, placeholder="e.g., Bangkok")

col1, col2 = st.columns(2)

with col1:
    travel_date = st.date_input("When are you traveling?")
    duration = st.number_input("Trip duration (days)", min_value=1, max_value=180, value=7)
    
    traveler_type = st.multiselect(
        "Traveler type",
        ["Solo traveler", "Family with children", "Senior citizen", "LGBTQ+", 
         "Travelers with disabilities", "Business traveler", "Student"]
    )

with col2:
    specific_concerns = st.multiselect(
        "Specific concerns",
        ["Health & medical", "Crime & safety", "Political stability", "Natural disasters", 
         "Transportation safety", "Food & water safety", "Scams", "Local laws"]
    )
    
    medical_conditions = st.text_area(
        "Medical conditions or special needs",
        placeholder="Any medical conditions the emergency services should know about"
    )


prompt = f"""
Provide comprehensive emergency and safety information for {destination}.

Details:
- Travel date: {travel_date}
- Duration: {duration} days
- Traveler type: {', '.join(traveler_type) if traveler_type else 'General'}
- Specific concerns: {', '.join(specific_concerns) if specific_concerns else 'All safety aspects'}
- Medical conditions: {medical_conditions}

Please provide:
1. Emergency contact numbers (police, ambulance, fire department, embassy)
2. Nearest hospitals and medical facilities with international standards
3. Current travel advisories and safety level
4. Common safety concerns and how to avoid them
5. Areas to avoid or exercise caution
6. Cultural norms that might impact safety
7. Health risks and recommended precautions (including required vaccinations)
8. Emergency phrases in local language
9. Tips for storing emergency information and documents

Format the information in clear sections that can be easily referenced in an emergency.
"""

col1, col2 = st.columns([2, 1])
with col1:
    submit_btn = st.button("Get Safety Information")


with col2:
    st.markdown("""
    <div class="emergency-card">
    <h3>📞 International Emergency Numbers</h3>
    <p><strong>International SOS:</strong> +1 215 942 8226</p>
    <p><strong>International Emergency:</strong> 112 (works in many countries)</p>
    </div>
    """, unsafe_allow_html=True)


if submit_btn:
    if not destination:
        st.error("Please enter a destination")
    else:
        with st.spinner(f"Gathering safety information for {destination}..."):
            safety_info = execute_task(emergency_task, prompt)
            
            
            st.session_state['safety_info'] = safety_info
            
            
            st.markdown(f"### 🚨 Safety Information for {destination}")
            st.markdown(safety_info)
            
            
            st.download_button(
                label="Download Safety Information",
                data=f"# Travel Safety: {destination}\n\n{safety_info}",
                file_name=f"safety_{destination.replace(' ', '_')}.md",
                mime="text/markdown"
            )


if 'safety_info' in st.session_state and not submit_btn:
    st.markdown("### Your Previous Safety Information")
    st.markdown(st.session_state['safety_info'])


st.markdown("## Additional Resources")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
    <h3>🌐 Useful Travel Safety Websites</h3>
    <ul>
    <li><a href="https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/" target="_blank">US Department of State Travel Advisories</a></li>
    <li><a href="https://www.gov.uk/foreign-travel-advice" target="_blank">UK Foreign Travel Advice</a></li>
    <li><a href="https://www.who.int/travel-advice" target="_blank">World Health Organization Travel Advice</a></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
    <h3>📱 Safety Apps for Travelers</h3>
    <ul>
    <li><strong>Smart Traveler</strong> - US State Department app</li>
    <li><strong>TripWhistle</strong> - Global emergency numbers</li>
    <li><strong>bSafe</strong> - Personal safety app with emergency alerts</li>
    <li><strong>First Aid by Red Cross</strong> - Emergency first aid guidance</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)