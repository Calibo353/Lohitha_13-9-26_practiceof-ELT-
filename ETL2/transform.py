def transform(df):

    # Make a copy of the data
    df = df.copy()

    # Encode species
    df["species"] = df["species"].map({
        "setosa": 0,
        "versicolor": 1,
        "virginica": 2
    })

    print(f"Transformed Shape: {df.shape}")

    return df