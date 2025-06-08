from agno.agent import Agent
from agno.models.google.gemini import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

# Using Google AI Studio
agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

# Print the response in the terminal
agent.print_response("Which team won 3 June 2025 IPL match?",stream=True)