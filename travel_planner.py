from dotenv import load_dotenv
from crewai import Agent, Task, Crew

# Load the API key (e.g. OPENAI_API_KEY) from the .env file
load_dotenv()

# Ask the user for a city when the script starts
city = input("Which city would you like to visit? ").strip()
if not city:
    raise SystemExit("Please enter a city name.")

# One agent: role, goal and backstory are written as real sentences
travel_agent = Agent(
    role="Experienced Local Travel Planner",
    goal=(
        "Recommend memorable and well-chosen places that give travelers "
        "an authentic feel for the city they are visiting."
    ),
    backstory=(
        "You have spent fifteen years working as a travel consultant, "
        "helping thousands of visitors discover the best of cities around "
        "the world. You know how to balance famous landmarks with hidden "
        "gems, and you always explain why a place is worth the trip."
    ),
    verbose=True,
)

# One task: exactly 3 places, with a clearly described output shape
travel_task = Task(
    description=(
        f"Suggest exactly 3 places to visit in {city}. "
        "Choose a varied mix, such as one landmark, one cultural spot, "
        "and one local favorite, and make sure every place is real."
    ),
    expected_output=(
        "A numbered list of exactly 3 items. Each item contains the name of "
        "the place in bold, followed by one or two sentences explaining why "
        "it is worth visiting. No introduction and no extra items."
    ),
    agent=travel_agent,
)

# Build the crew from the agent and task
crew = Crew(
    agents=[travel_agent],
    tasks=[travel_task],
    verbose=True,
)

# Run it and print the result
result = crew.kickoff()
print("\n=== Your Travel Recommendations ===\n")
print(result)