import os
import csv
from embeddings import embed_text
from vectorstore import VectorStore

def load_csv(file_path: str, column_name: str):
    objs = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            embeddings = embed_text(row[column_name])
            id = row.pop('Id')
            objs.append((id, embeddings, row))
    return objs
    
def main(index_name):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset/Reviews_10.csv')
    data = load_csv(file_path, 'Text')
    vs = VectorStore(index_name)
    vs.create_index(384)
    vs.batch_insert_vectors(data)
    print(f'Succesfully uploaded {len(data)} rows to {index_name}')

if __name__ == "__main__":
    index_name = 'lightning-talk'
    main(index_name)

