import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️"
)

st.title("ℹ️ About AI Travel Planner")

st.markdown("""
## How It Works

The AI Travel Planner uses advanced AI agents to help you plan every aspect of your trip:

1. **Trip Planner**: Creates personalized itineraries based on your preferences, including daily activities, attraction recommendations, and logistics planning.

2. **Budget Estimator**: Provides detailed cost breakdowns for your entire trip, helping you understand where your money will go and how to plan financially.

3. **Cuisine Guide**: Recommends authentic local dishes and dining experiences, taking into account your dietary preferences and food interests.

4. **Emergency Assistant**: Prepares you with important safety information, local emergency contacts, and travel advisories specific to your destination.

## Technology

This application is built using:
- **Streamlit**: For the user interface
- **CrewAI**: For coordinating AI agents to handle specific travel planning tasks
- **Groq AI**: Powering the large language models that generate personalized recommendations
- **LangChain**: For structured AI interactions and workflows

## Privacy & Data

- Your travel details are only used to generate recommendations
- We don't store your personal information
- Queries are processed securely through encrypted connections

## Feedback

We're constantly improving! If you have suggestions, feature requests, or encounter any issues, please let us know.

## Credits

Developed by Rohit - 2025
""")


st.subheader("Contact Us")

contact_form = st.form("contact_form")
with contact_form:
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit = st.form_submit_button("Send")

if submit:
    st.success("Thanks for your message! We'll get back to you soon.")