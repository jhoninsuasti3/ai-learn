# pip install -qU "langchain[anthropic]" to call the model

import os
from langchain.agents import create_agent

# Anthropic API key will be loaded from ANTHROPIC_API_KEY environment variable
# Make sure it's set in your .env file

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="claude-sonnet-4-5-20250929",  # Uses ANTHROPIC_API_KEY from environment
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

