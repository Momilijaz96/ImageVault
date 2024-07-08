# All utils used for various purposes
import pandas as pd

def read_csv(file_path):
    """
    Read a csv file and return a pandas dataframe
    """
    return pd.read_csv(file_path)