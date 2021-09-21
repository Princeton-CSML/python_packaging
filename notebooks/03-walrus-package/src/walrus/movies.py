from importlib.resources import path 
import pandas as pd


def best_movie(year):
    with path('walrus.data', 'oscars_df.csv') as csv_file:
        df = pd.read_csv(csv_file)
    df = df[(df['Oscar Year']==year) & (df['Award']=='Winner')]
    if df.shape[0]!=1:
        return None
    else:
        return df.iloc[0]['Film']
