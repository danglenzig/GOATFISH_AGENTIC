from agents import Agent, function_tool, Runner, RunResult, MessageOutputItem
from .prompt_configs import generic_agent_prompt, hypercasual_game_designer_prompt
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from dotenv import load_dotenv
from typing import Optional
import asyncio



QDRANT_ENDPOINT: str = "http://localhost:6333"
QDRANT_CLIENT: QdrantClient = QdrantClient(QDRANT_ENDPOINT)
EMBEDDING_MODEL: OpenAIEmbeddings = OpenAIEmbeddings(model="text-embedding-3-large")

@function_tool
def search_hypercasual_kb(query: Optional[str] = None) -> str:

    if query is None:
            query = "How do design an engaging hypercasual game with intuitive controls and a strong monetization strategy?"

    """
    Search the hypercasual game design knowledge base for relevant information.
    """
    vector_store: QdrantVectorStore = QdrantVectorStore.from_existing_collection(
        url=QDRANT_ENDPOINT,
        collection_name="hypercasual",
        embedding=EMBEDDING_MODEL
    )



hello_world_agent: Agent = Agent(
    name="Hello World Agent",
    instructions=generic_agent_prompt,
    model = "gpt-5.4-nano"
)

hypercasual_game_designer_agent: Agent = Agent(
    name="Hypercasual Game Designer Agent",
    instructions= hypercasual_game_designer_prompt,
    model = "gpt-5.4",
    tools=[search_hypercasual_kb]
)

async def main():
    # Example usage of the hypercasual game designer agent
    question = "Write five one-paragraph game design concepts for hypercasual games with intuitive controls and strong monetization strategies."
    result = await Runner.run(hypercasual_game_designer_agent, question)
    print("Final Output:")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())




