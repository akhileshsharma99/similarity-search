import streamlit as st
import pandas as pd
from ui import show_search_bar, show_table
from data import get_data

def main():
    # Load data
    data = get_data()

    # UI
    show_search_bar()
    show_table(data)

if __name__ == "__main__":
    main()
