"""
LangGraph Agent with Claude Sonnet 4.5

This agent uses Claude Sonnet 4.5 and has access to a weather tool.
The ANTHROPIC_API_KEY is loaded from the .env file.
"""

from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city.

    Args:
        city: The name of the city to get weather for

    Returns:
        A string with the weather information
    """
    return f"It's always sunny in {city}!"


# Initialize the Claude model
# ANTHROPIC_API_KEY will be loaded automatically from environment
model = ChatAnthropic(
    model="claude-sonnet-4-5-20250929",
    temperature=0,
)

# Create the ReAct agent
agent = create_react_agent(
    model=model,
    tools=[get_weather],
)

