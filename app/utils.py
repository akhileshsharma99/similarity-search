import numpy as np

def calculate_similarity(vector1, vector2):
    # Calculate cosine similarity between two vectors
    dot_product = np.dot(vector1, vector2)
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)
    similarity = dot_product / (norm1 * norm2)
    return similarity

def preprocess_data(data):
    # Preprocess the data
    data['vector'] = data['vector'].apply(eval)
    return data

def search_data(data, query):
    # Search data based on query
    filtered_data = data[data['name'].str.contains(query, case=False)]
    return filtered_data
