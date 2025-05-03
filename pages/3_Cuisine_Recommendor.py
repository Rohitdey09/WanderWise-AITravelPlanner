import streamlit as st
from services.service import execute_task
from services.task import cuisine_task

st.set_page_config(
    page_title="Cuisine Guide",
    page_icon="🍽️",
    layout="wide"
)


st.markdown("""
<style>
    .page-title {
        font-size: 2.5rem !important;
        color: #1E88E5;
    }
    .cuisine-card {
        background-color: #FFF8E1;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='page-title'>🍽️ Local Cuisine Guide</h1>", unsafe_allow_html=True)
st.markdown("Discover authentic local dishes and restaurant recommendations")


destination = st.text_input("Where are you traveling to?", placeholder="e.g., Tokyo")

col1, col2 = st.columns(2)

with col1:
    dietary_restrictions = st.multiselect(
        "Dietary restrictions or preferences",
        ["Vegetarian", "Vegan", "Gluten-free", "Halal", "Kosher", "Dairy-free", "Nut allergies", "None"]
    )
    
    spice_preference = st.select_slider(
        "Spice preference",
        options=["Mild", "Medium", "Spicy", "Very Spicy"],
        value="Medium"
    )

with col2:
    price_range = st.select_slider(
        "Price range",
        options=["Budget", "Moderate", "Expensive", "Luxury"],
        value="Moderate"
    )
    
    specific_interests = st.multiselect(
        "Specific food interests",
        ["Street food", "Fine dining", "Local markets", "Cooking classes", "Food tours", 
         "Traditional cuisine", "Fusion cuisine", "Desserts & sweets", "Drinks & nightlife"]
    )


prompt = f"""
Recommend must-try food and dining experiences in {destination}.

Details:
- Dietary restrictions: {', '.join(dietary_restrictions) if dietary_restrictions else 'None'}
- Spice preference: {spice_preference}
- Price range: {price_range}
- Food interests: {', '.join(specific_interests) if specific_interests else 'All types'}

Please provide:
1. Top 10 must-try local dishes with descriptions
2. Recommended restaurants categorized by meal (breakfast, lunch, dinner)
3. Special food markets or streets known for good food
4. Local food etiquette and customs
5. Any special food festivals or events worth noting
6. Recommended food tours or cooking classes if available
"""

submit_btn = st.button("Get Cuisine Recommendations")


if submit_btn:
    if not destination:
        st.error("Please enter a destination")
    else:
        with st.spinner(f"Researching the best food experiences in {destination}..."):
            cuisine_result = execute_task(cuisine_task, prompt)
            
            
            st.session_state['cuisine_result'] = cuisine_result
            
            
            st.markdown(f"### 🍽️ Your Food Guide to {destination}")
            st.markdown(cuisine_result)
            
            
            st.download_button(
                label="Download Food Guide",
                data=f"# Cuisine Guide: {destination}\n\n{cuisine_result}",
                file_name=f"food_guide_{destination.replace(' ', '_')}.md",
                mime="text/markdown"
            )


if 'cuisine_result' in st.session_state and not submit_btn:
    st.markdown("### Your Previous Cuisine Guide")
    st.markdown(st.session_state['cuisine_result'])