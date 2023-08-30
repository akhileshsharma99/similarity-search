from langchain.embeddings import HuggingFaceEmbeddings
from typing import List

def embed_text(text) -> List[float]:
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2", cache_folder="./cache")
    data = embeddings.embed_query(text)
    return data
