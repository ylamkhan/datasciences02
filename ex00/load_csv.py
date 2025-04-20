import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load data set and return dataframe"""
    try:
        if str is None:
            raise ArithmeticError("the path is bad")
        if not isinstance(path, str):
            raise AssertionError("the path don't string")
        if not path.endswith('.csv'):
            raise AssertionError("invalide format")
        df = pd.read_csv(path)
        print("Loading dataset of dimensions :", df.shape)
        print(df)
        return df
    except AssertionError as ve:
        print("AssertionError : ", ve)
        return None
    except FileNotFoundError as ve:
        print("FileNotFoundError : ", ve)
        return None
