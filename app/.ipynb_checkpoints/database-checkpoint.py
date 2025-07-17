import pandas as pd

def load_database(path='data/products.csv'):
    df = pd.read_csv(path)
    df.dropna(subset=['name', 'composition', 'uses', 'side_effects', 'image_url'], inplace=True)
    df['composition'] = df['composition'].astype(str)
    df['uses'] = df['uses'].astype(str)
    return df