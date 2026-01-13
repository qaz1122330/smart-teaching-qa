import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = "gpt-3.5-turbo"
    EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
    CHROMA_PERSIST_DIR = "./vector_store"
    CHROMA_COLLECTION_NAME = "teaching_knowledge"
    DATA_DIR = "./data"
    TOP_K_RESULTS = 3
    CHUNK_SIZE = 500
