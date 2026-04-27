# from agents import function_tool
# from langchain_openai import OpenAIEmbeddings
# from langchain_qdrant import QdrantVectorStore
# from qdrant_client import QdrantClient
# from dotenv import load_dotenv
# from typing import Optional



# QDRANT_ENDPOINT: str = "http://localhost:6333"
# QDRANT_CLIENT: QdrantClient = QdrantClient(QDRANT_ENDPOINT)
# EMBEDDING_MODEL: OpenAIEmbeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# @function_tool
# def search_hypercasual_kb(query: Optional[str] = None) -> str:

#     if query is None:
#             query = "How do design an engaging hypercasual game with intuitive controls and a strong monetization strategy?"

#     """
#     Search the hypercasual game design knowledge base for relevant information.
#     """
#     vector_store: QdrantVectorStore = QdrantVectorStore.from_existing_collection(
#         url=QDRANT_ENDPOINT,
#         collection_name="hypercasual",
#         embedding=EMBEDDING_MODEL
#     )