import streamlit as st
import pandas as pd
from ui import show_search_bar, show_table
from vectorstore import VectorStore

index_name = 'lightning-talk'
vs = VectorStore(index_name)


def main():
    # UI
    search_bar = show_search_bar()
    data = get_data(search_bar)
    show_table(data)


def get_data(text):
    global vs

    if not text:
        return pd.DataFrame()
    
    raw_data = vs.query_text(text, 15)
    
    # Preprocess the data   
    data = []
    for item in raw_data['matches']:
        data.append({
            'ID': item['id'],
            'ProductId': item['metadata']['ProductId'],
            'Similiarity': item['score'],
            'Text': item['metadata']['Text'],
            'Vector': item['values']
        })
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    main()
