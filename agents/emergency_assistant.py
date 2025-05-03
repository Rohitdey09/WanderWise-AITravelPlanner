from langchain_groq import ChatGroq
from crewai import Agent
from utils.config import GROQ_API_KEY

llm = ChatGroq(model="groq/llama3-8b-8192",api_key=GROQ_API_KEY)

emergency_assistant = Agent(
    name="Emergency Assistance",
    role="AI Travel Guide",
    goal="Create travel itineraries",
    backstory="An AI assistant specializing in planning seamless travel experiences.",
    llm=llm
)
