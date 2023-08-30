import streamlit as st

def show_search_bar():
    search_query = st.text_input("Search")
    return search_query
    
def show_table(df):
    if not df.empty:
        st.dataframe(df, hide_index=True)
    else:
        st.write("No data to display.")
