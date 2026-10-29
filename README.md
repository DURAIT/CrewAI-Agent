# CrewAI Travel Planner

A simple command-line travel planner built with [CrewAI](https://docs.crewai.com/). You enter a city, and an AI agent suggests exactly 3 places worth visiting there.

## How It Works

1. The script asks you for a city using `input()`.
2. A **Travel Planner agent** (with a role, goal and backstory) is created.
3. A **task** tells the agent to suggest exactly 3 places in that city, in a defined output format.
4. A **crew** is built from the agent and task, then run with `crew.kickoff()`.
5. The result is printed to the terminal.

## Requirements

- **Python 3.10 to 3.13** (Python 3.12 is recommended).
  CrewAI does **not** support Python 3.14 yet, so installation will fail on it.
- An API key for an LLM provider. CrewAI uses **OpenAI** by default.

## Project Structure

```
travel-planner/
├── travel_planner.py   # The main script
├── .env                # Your API key (never commit this file)
└── README.md
```

## Setup

### 1. Create a virtual environment

Using `uv` (can download the right Python version for you):

```bash
pip install uv
uv venv --python 3.12
```

Or with standard Python 3.12:

```bash
python3.12 -m venv .venv      # Windows: py -3.12 -m venv .venv
```

### 2. Activate the environment

```bash
source .venv/bin/activate     # macOS / Linux
.venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```bash
uv pip install crewai python-dotenv
# or, without uv:
pip install crewai python-dotenv
```

### 4. Add your API key

Create a file named `.env` in the project folder:

```
OPENAI_API_KEY=your-api-key-here
```

If you use a different provider, set that provider's key instead and pass an `llm=` argument to the `Agent`.

> Add `.env` to your `.gitignore` so your key is never pushed to GitHub.

## Running the Script

```bash
python travel_planner.py
```

Example session:

```
Which city would you like to visit? Paris
```

Because `verbose=True` is set, you will see the agent's reasoning in the terminal. The final answer appears under **Your Travel Recommendations**.

## Code Walkthrough

| Part | What it does |
|------|--------------|
| `load_dotenv()` | Reads the API key from the `.env` file into the environment. |
| `input()` | Asks the user for a city and rejects an empty answer. |
| `Agent(...)` | Defines the planner with a `role`, `goal`, `backstory` and `verbose=True`. |
| `Task(...)` | Describes the job (exactly 3 places) and the `expected_output` format. |
| `Crew(...)` | Combines the agent and task into one runnable unit. |
| `crew.kickoff()` | Runs the crew and returns the result, which is then printed. |

## Customizing

- **Change the number of places:** edit the `description` and `expected_output` in the `Task`.
- **Change the style of advice:** edit the agent's `role`, `goal` or `backstory` (for example, a budget backpacker guide or a luxury travel advisor).
- **Use a different model:** pass `llm="gpt-4o-mini"` (or another model name) to the `Agent`.
- **Quieter output:** set `verbose=False` on the agent and crew.
