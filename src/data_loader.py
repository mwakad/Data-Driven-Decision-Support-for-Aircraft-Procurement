import pandas as pd

def load_data(filepath):
    """Loads the dataset from the given filepath."""
    df = pd.read_csv("data/aviation-data.csv", encoding='latin1', low_memory=False)
    return df

def initial_inspection(df):
    """Performs initial inspection of the DataFrame."""
    print("DataFrame shape:", df.shape)
    print("DataFrame info:")
    df.info()
    print("DataFrame dtypes:")
    print(df.dtypes)
    print("Missing values:")
    print(df.isna().sum())
    return df