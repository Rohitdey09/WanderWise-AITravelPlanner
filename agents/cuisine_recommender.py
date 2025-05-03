from langchain_groq import ChatGroq
from crewai import Agent
from utils.config import GROQ_API_KEY

llm = ChatGroq(model="groq/llama3-8b-8192",api_key=GROQ_API_KEY)

cuisine_recommender = Agent(
    name="Cuisine Recommender",
    role="Food Expert",
    goal="Recommend local cuisine",
    backstory="An AI assistant specializing in planning seamless travel experiences.",
    llm=llm
)
