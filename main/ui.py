import streamlit as st

def show_search_bar():
    search_query = st.text_input("Search", "")

def show_table(data):
    st.table(data)
