import pandas as pd

def get_data():
    data = {
        'name': ['John', 'Jane', 'Mike'],
        'description': ['Engineer', 'Designer', 'Developer'],
        'similarity_score': [0.8, 0.6, 0.9],
        'vector': ['[1, 2, 3]', '[4, 5, 6]', '[7, 8, 9]']
    }
    return pd.DataFrame(data)
