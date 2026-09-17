def validate(df):

    assert df.isnull().sum().sum() == 0, "Null values are still present"
    assert df["species"].isin([0, 1, 2]).all(), "Species column is not fully encoded"

    print("Validation Passed")