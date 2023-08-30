import os
import csv
import logging
from embeddings import embed_text
from vectorstore import VectorStore

logging.basicConfig(level=logging.ERROR)

def load_csv_in_chunks(file_path: str, column_name: str, chunksize: int = 500):
    logging.info('Starting to load CSV in chunks.')
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        objs = []
        for i, row in enumerate(reader):
            if i > 0 and i % chunksize == 0:
                yield objs
                objs = []
            embeddings = embed_text(row[column_name])
            id = row.pop('Id')
            objs.append((id, embeddings, row))
        logging.info(f'Loaded chunk with {len(objs)} rows.')
        yield objs
    
def main(index_name):
    logging.info('Starting main function.')
    vs = VectorStore(index_name)
    vs.create_index(384)

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset/Reviews.csv')
    for data in load_csv_in_chunks(file_path, 'Text', 50):
        try:
            vs.upsert_vectors(data)
            logging.info(f'Succesfully uploaded {len(data)} rows to {index_name}')
        except Exception as e:
            logging.error(f'Failed to upload data to {index_name}. Error: {str(e)}')

if __name__ == "__main__":
    index_name = 'lightning-talk'
    main(index_name)

