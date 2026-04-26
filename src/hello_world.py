# To run this file, use the command because it is a module in the src package:
# python3 -m src.hello_world 

from agents import Agent, Runner, RunResult, MessageOutputItem
import json
from dotenv import load_dotenv
from .configs import agent_configs
load_dotenv()


async def chat_with_agent(message: str) -> str:
    result: RunResult = await Runner.run(
        agent_configs.hello_world_agent,
        message
    )
    return result.final_output

async def hello_world():
    while True:
        user_input: str = input("--> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response: str = await chat_with_agent(user_input)
        print(f"\nAgent: {response}\n")

async def main():
    await hello_world()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())