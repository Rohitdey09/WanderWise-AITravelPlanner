from crewai import Task
from agents.trip_planner import trip_planner
from agents.budget_estimator import budget_estimator
from agents.cuisine_recommender import cuisine_recommender
from agents.emergency_assistant import emergency_assistant

trip_task = Task(
    description="Generate an itinerary", 
    agent=trip_planner,
    expected_output="A detailed day-by-day travel itinerary"
)

budget_task = Task(
    description="Estimate budget", 
    agent=budget_estimator,
    expected_output="A breakdown of expected expenses"
)

cuisine_task = Task(
    description="Recommend cuisines", 
    agent=cuisine_recommender,
    expected_output="List of recommended local dishes and restaurants"
)

emergency_task = Task(
    description="Provide emergency info", 
    agent=emergency_assistant,
    expected_output="Emergency contact information and safety tips"
)