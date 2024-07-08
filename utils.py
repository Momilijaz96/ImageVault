# All utils used for various purposes
import pandas as pd

def read_csv(file_path):
    """
    Read a csv file and return a pandas dataframe
    """
    return pd.read_csv(file_path)


def df_row_to_mongo_object(df_row):
    """
    Convert a pandas dataframe row to a dictionary object
    """
    return df_row.to_dict(orient='records')[0]

def compress_image(image,new_height,new_width):
    """
    Compress an image to a new size
    """
    return image.resize((new_height, new_width))