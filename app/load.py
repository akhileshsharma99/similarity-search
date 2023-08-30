from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceEmbeddings
import os

def load_data(file_path: str):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2",cache_folder="./cache")
    loader = CSVLoader(file_path=file_path)
    data = loader.load()
    print(len(data))
    print(data[0])

def main():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset/Reviews.csv')
    load_data(file_path)

if __name__ == "__main__":
    main()
