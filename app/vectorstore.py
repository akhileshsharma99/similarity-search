import os
from typing import List
import pinecone
import random
import itertools
from embeddings import embed_text

class VectorStore:

    def __init__(self, index_name):
        api_key = os.getenv("PINECONE_API_KEY") or "PINECONE_API_KEY"
        env = os.getenv("PINECONE_ENVIRONMENT") or "PINECONE_ENVIRONMENT"
        pinecone.init(api_key=api_key, environment=env)
        self.index_name = index_name
        self.index = pinecone.Index(index_name)

    def create_index(self, dimensions):
        """Method to create an index if it doesn't exist."""
        if self.index_name in pinecone.list_indexes():
            print(f"Index {self.index_name} already exists.")
        else:
            pinecone.create_index(self.index_name, dimension=dimensions, metric="dotproduct")
            print(f"Created index: {self.index_name}")

    def upsert_vectors(self, vectors):
        self.index.upsert(vectors=vectors)

    def query_vector(self, vector: List[float], top_k):
        """Method to query a vector and get top_k values back."""
        return self.index.query(vector=vector, top_k=top_k, include_values=True, include_metadata=True)

    def query_text(self, text: str, top_k=5):
        """Method to query a text and get top_k values back."""
        vector = embed_text(text)
        return self.index.query(vector=vector, top_k=top_k, include_values=True, include_metadata=True)