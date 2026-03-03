import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-east-1-aws")

# Model configurations
TARGET_MODEL = "llama-3.3-70b-versatile"
JUDGE_MODEL = "llama-3.1-8b-instant"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Experiment settings
MAX_CONCURRENT_REQUESTS = 10
SIMILARITY_THRESHOLD = 0.8