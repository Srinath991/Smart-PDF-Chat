import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GCS_BUCKET = os.getenv("GCS_BUCKET")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV = os.getenv("PINECONE_ENV")
    PINECONE_INDEX = os.getenv("PINECONE_INDEX")
    GOOGLE_PROJECT = os.getenv("GOOGLE_PROJECT")

settings = Settings()
