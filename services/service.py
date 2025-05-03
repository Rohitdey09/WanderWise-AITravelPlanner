from crewai import Crew
from services.task import trip_task, budget_task, cuisine_task, emergency_task

travel_crew = Crew(
    agents=[trip_task.agent, budget_task.agent, cuisine_task.agent, emergency_task.agent],
    tasks=[trip_task, budget_task, cuisine_task, emergency_task]
)

'''def execute_task(task, prompt):
    return task.agent.execute(prompt)'''



def execute_task(task, prompt):
    from crewai import Task
    custom_task = Task(
        description=prompt,
        agent=task.agent,
        expected_output=task.expected_output
    )
    
  
    single_task_crew = Crew(
        agents=[task.agent],
        tasks=[custom_task]
    )
    
    
    return single_task_crew.kickoff()
