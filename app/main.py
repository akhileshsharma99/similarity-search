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
    
    raw_data = vs.query_text(text)
    
    print(raw_data)
    # Preprocess the data   
    data = []
    for item in raw_data['matches']:
        data.append({
            'id': item['id'],
            'Similiarity': item['score'],
            'ProductId': item['metadata']['ProductId'],
            'Score': item['metadata']['Score'],
            'Text': item['metadata']['Text']
        })
    
    df = pd.DataFrame(data)
    df.reset_index(drop=True, inplace=True)
    return df

if __name__ == "__main__":
    # raw_data = vs.query_text('hi')
    # print(raw_data)
    main()
