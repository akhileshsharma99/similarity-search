from langchain.embeddings import HuggingFaceEmbeddings
from typing import List
import os

def embed_text(text) -> List[float]:
    cache_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2", cache_folder=cache_folder_path)
    data = embeddings.embed_query(text)
    return data

