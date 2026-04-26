# This script uses the LangChain WebBaseLoader to load data from a website and create a vector store index in Qdrant.
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

load_dotenv()

CLIENT: QdrantClient = QdrantClient("http://localhost:6333")
SPLITTER: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
EMBEDDING_MODEL: OpenAIEmbeddings = OpenAIEmbeddings(model="text-embedding-3-large")

def collection_exists(client: QdrantClient, collection_name: str) -> bool:
    try:
        client.get_collection(collection_name)
        return True
    except Exception:
        return False
    
def create_collection(client: QdrantClient, web_url: str, collection_name: str):

    if collection_exists(client, collection_name):
        append_to_collection(client, web_url, collection_name)
        return

    loader: WebBaseLoader = WebBaseLoader(web_url)
    documents = loader.load()
    chunks = SPLITTER.split_documents(documents)

    vector_store: QdrantVectorStore = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=EMBEDDING_MODEL,
        url = "http://localhost:6333",
        collection_name=collection_name
    )

    print(f"Collection '{collection_name}' created with {len(chunks)} chunks from {web_url}.")

def append_to_collection(client: QdrantClient, web_url: str, collection_name: str):
    
    if not collection_exists(client, collection_name):
        create_collection(client, web_url, collection_name)
        return
    
    loader: WebBaseLoader = WebBaseLoader(web_url)
    documents = loader.load()
    chunks = SPLITTER.split_documents(documents)

    vector_store: QdrantVectorStore = QdrantVectorStore.from_existing_collection(
        embedding=EMBEDDING_MODEL,
        url = "http://localhost:6333",
        collection_name=collection_name
    )

    vector_store.add_documents(chunks)

    print(f"Collection '{collection_name}' updated with {len(chunks)} new chunks from {web_url}.")


def main():
    web_url = input("Enter the website URL to index: ")
    collection_name = input("Enter the collection name for Qdrant: ")
    create_collection(CLIENT, web_url, collection_name)

if __name__ == "__main__":
    main()
