import seaborn as sns
import pandas as pd


def extract():
    df = sns.load_dataset("iris")

    print(f"Extracted {len(df)} rows, {len(df.columns)} columns")

    return df