import time
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from core.config import settings
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
pc = Pinecone(api_key=settings.PINECONE_API_KEY)
index_name=settings.PINECONE_INDEX

existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        deletion_protection="enabled",  # Defaults to "disabled"
    )
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

index = pc.Index(index_name)

def get_vector_store(namespace:str):
    vector_store = PineconeVectorStore(index=index, embedding=GoogleGenerativeAIEmbeddings(model='models/embedding-001'),namespace=namespace)
    return vector_store




