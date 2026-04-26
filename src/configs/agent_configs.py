from agents import Agent
from .prompt_configs import generic_agent_prompt

hello_world_agent: Agent = Agent(
    name="Hello World Agent",
    instructions=generic_agent_prompt,
    model = "gpt-5.4-nano"
)
